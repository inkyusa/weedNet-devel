import numpy as np
import matplotlib.pyplot as plt
import os.path
import json
import scipy
import argparse
import math
import pylab
import Image
from sklearn.preprocessing import normalize
caffe_root = '/home/enddl22/workspace/caffe-segnet-cudnn5/' 			# Change this to the absolute directoy to SegNet Caffe
import sys
from timeit import default_timer as timer

sys.path.insert(0, caffe_root + 'python')


IMAGE_FILE='/home/enddl22/workspace/SegNet-Tutorial/Results/seg_camvid_results/'
gt_path=IMAGE_FILE+'gt'
pred_path=IMAGE_FILE+'pred'
if not (os.path.exists(IMAGE_FILE) and os.path.exists(gt_path) and os.path.exists(pred_path)):
	os.makedirs(IMAGE_FILE)
	os.makedirs(gt_path)
	os.makedirs(pred_path)
	print 'Folder does not exist, create at {}'.format(IMAGE_FILE)
else:
	print 'Dir exist'


import caffe
# Import arguments
parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, required=True)
parser.add_argument('--weights', type=str, required=True)
parser.add_argument('--iter', type=int, required=True)
parser.add_argument('--gpu', type=int, required=True)
args = parser.parse_args()

caffe.set_mode_gpu()
caffe.set_device(args.gpu) #set GPU id

net = caffe.Net(args.model,
                args.weights,
                caffe.TEST)

processing_time=np.array(np.zeros(args.iter))
for i in range(0, args.iter):
	start = timer()
	net.forward()
	end = timer()
	processing_time[i]=(end-start)

	image = net.blobs['data'].data
	label = net.blobs['label'].data
	
	label=label.astype(np.uint8)
	print 'dtype=',label.dtype
	predicted = net.blobs['prob'].data
	image = np.squeeze(image[0,:,:,:])
	output = np.squeeze(predicted[0,:,:,:])

	#print label.shape
	output
	ind = np.argmax(output, axis=0)
	ind=ind.astype(np.uint8)
	r = ind.copy()
	g = ind.copy()
	b = ind.copy()
	r_gt = label.copy()
	g_gt = label.copy()
	b_gt = label.copy()

	Sky = [128,128,128]
	Building = [128,0,0]
	Pole = [192,192,128]
	Road_marking = [255,69,0]
	Road = [128,64,128]
	Pavement = [60,40,222]
	Tree = [128,128,0]
	SignSymbol = [192,128,128]
	Fence = [64,64,128]
	Car = [64,0,128]
	Pedestrian = [64,64,0]
	Bicyclist = [0,128,192]
	Unlabelled = [0,0,0]

	label_colours = np.array([Sky, Building, Pole, Road, Pavement, Tree, SignSymbol, Fence, Car, Pedestrian, Bicyclist, Unlabelled])
	for l in range(0,11):
		r[ind==l] = label_colours[l,0]
		g[ind==l] = label_colours[l,1]
		b[ind==l] = label_colours[l,2]
		r_gt[label==l] = label_colours[l,0]
		g_gt[label==l] = label_colours[l,1]
		b_gt[label==l] = label_colours[l,2]

	rgb = np.zeros((ind.shape[0], ind.shape[1], 3))
	rgb[:,:,0] = r/255.0
	rgb[:,:,1] = g/255.0
	rgb[:,:,2] = b/255.0
	rgb_gt = np.zeros((ind.shape[0], ind.shape[1], 3))
	rgb_gt[:,:,0] = r_gt/255.0
	rgb_gt[:,:,1] = g_gt/255.0
	rgb_gt[:,:,2] = b_gt/255.0

	image = image/255.0

	image = np.transpose(image, (1,2,0))
	output = np.transpose(output, (1,2,0))
	image = image[:,:,(2,1,0)]
	str='%04d'%(i,)
	predic_file_name=IMAGE_FILE+str+'_segnet_predic.png'
	inputImg_file_name=IMAGE_FILE+str+'_segnet_rgb.png'
	gt_file_name=IMAGE_FILE+str+'_segnet_gt.png'
	
	scipy.misc.toimage(rgb, cmin=0.0, cmax=1.0).save(predic_file_name)
	scipy.misc.toimage(image, cmin=0.0, cmax=1.0).save(inputImg_file_name)
	scipy.misc.toimage(rgb_gt, cmin=0.0, cmax=1.0).save(gt_file_name)

	# i have them as np.uint8 typed arrays
	#print label.shape()
	label = np.squeeze(label[0,:,:,:])
	idxLabel = Image.fromarray(label, 'L')
	name= '%04d'%i
	idxLabel.save(gt_path+'/gt_test_' + name + '.ppm') #or another format

	idxPred = Image.fromarray(ind, 'L')
	idxPred.save(pred_path+'/pred_test_' + name + '.ppm') #or another format
	#scipy.misc.toimage(image, cmin=0.0, cmax=255).save(file_name)

	# plt.figure()
	# plt.imshow(image,vmin=0, vmax=1)
	# plt.figure()
	# plt.imshow(rgb_gt,vmin=0, vmax=1)
	# plt.figure()
	# plt.imshow(rgb,vmin=0, vmax=1)
	# plt.show()

print 'Processing time per image = %f'%np.average(processing_time)
print 'Success!'

