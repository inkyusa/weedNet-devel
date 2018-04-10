import numpy as np
import matplotlib.pyplot as plt
import os.path
import scipy
import argparse
import math
import cv2
import sys
import time

sys.path.append('/usr/local/lib/python2.7/site-packages')
# Make sure that caffe is on the python path:
caffe_root = '/home/mpopovic/workspace/weedNet-devel/caffe-segnet-cudnn5/'
sys.path.insert(0, caffe_root + 'python')
import caffe

#model='../../Models/segnet_scientifica_inference_live.prototxt'
model='/home/mpopovic/workspace/weedNet-devel/SegNet-Tutorial/Models/segnet_ipp_inference_live.prototxt'

#weights='../../caffeModels/segnet_IW_Bonn_3m_5m_wo_cls_balc_weights.caffemodel'
#weights='../../caffeModels/segnet_IW_Bonn_3m_wo_cls_balc_weights.caffemodel'
#weights='../../caffeModels/segnet_IW_Bonn_3m_weights.caffemodel'
#weights='../../caffeModels/segnet_IW_Bonn_5m_weights.caffemodel'
weights='/home/mpopovic/workspace/weedNet-devel/SegNet-Tutorial/Models/Inference/test_weights.caffemodel'
net = caffe.Net(model,
                weights,
                caffe.TEST)

caffe.set_mode_gpu()

input_shape = net.blobs['data'].data.shape
#output_shape = net.blobs['argmax'].data.shape
output_shape = net.blobs['prob'].data.shape

Soil = [0,0,255]
Plant = [255,0,0]
Weed = [0,255,0]
label_colours = np.array([Soil, Plant, Weed])

# Directory to load images from
input_dir = "10m_images_test"
# Directory to save images to
output_dir = "10m_images_test_out"
if not os.path.exists(output_dir):
	os.makedirs(output_dir)
	print 'Folder does not exist, create at {}'.format(output_dir)
else:
	print 'Dir exist'

# Loop through all images in the target directory
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"): 
        print(os.path.join(input_dir, filename))
        # Load and resize image
        input_image = cv2.imread(os.path.join(input_dir, filename))
        input_image = cv2.resize(input_image, (input_shape[3],input_shape[2]))
        input_image = input_image.transpose((2,0,1))
        input_image = np.asarray([input_image])
        # Do forward pass
        net.forward(data=input_image)
        predicted = net.blobs['prob'].data
        output = np.squeeze(predicted[0,:,:,:])
#        for l in range(0,3):
#            str1='%d'%l
#            prob_file_name = os.path.splitext(filename)[0] +'_segnet_prob'+str1+'.png'
#            scipy.misc.toimage(output[l,:,:], cmin=0.0, cmax=1.0).save(os.path.join(output_dir, prob_file_name))
        ind = np.argmax(output, axis=0)
        r = ind.copy()
        g = ind.copy()
        b = ind.copy()
        for l in range(0,3):
            r[ind==l] = label_colours[l,0]
            g[ind==l] = label_colours[l,1]
            b[ind==l] = label_colours[l,2]
        rgb = np.zeros((ind.shape[0], ind.shape[1], 3))
        rgb[:,:,0] = r/255.0
        rgb[:,:,1] = g/255.0
        rgb[:,:,2] = b/255.0
        predic_file_name = os.path.splitext(filename)[0]+'_segnet_predic.png'
        scipy.misc.toimage(rgb, cmin=0.0, cmax=1.0).save(os.path.join(output_dir, predic_file_name))
        continue
    else:
        continue
