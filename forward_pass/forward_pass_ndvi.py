import numpy as np
import matplotlib.pyplot as plt
import os.path
import scipy
import argparse
import math
import cv2
import sys
import time

GPU_ID = 1

sys.path.append('/usr/local/lib/python2.7/site-packages')
# Make sure that caffe is on the python path:
caffe_root = '/home/mpopovic/workspace/weedNet-devel/caffe-segnet-cudnn5/'
sys.path.insert(0, caffe_root + 'python')
import caffe

model='/home/mpopovic/workspace/weedNet-devel/SegNet-Tutorial/Models/segnet_ipp_ndvi_inference_live.prototxt'

weights='/home/mpopovic/workspace/weedNet-devel/SegNet-Tutorial/Models/Inference/test_weights_3m_ndvi.caffemodel'

caffe.set_mode_gpu()
caffe.set_device(GPU_ID)

net = caffe.Net(model,
                weights,
                caffe.TEST)

input_shape = net.blobs['data'].data.shape
#output_shape = net.blobs['argmax'].data.shape
output_shape = net.blobs['prob'].data.shape

Soil = [0,0,255] # blue
Plant = [255,0,0] # red
Weed = [0,255,0] # green
label_colours = np.array([Soil, Plant, Weed])

# Directory to load images from
input_dir_rgb = "3m_ndvi_training/3m_images_test"
input_dir_ndvi = "3m_ndvi_training/3m_images_test_ndvi"
# Directory to save images to
output_dir = "3m_ndvi_training/3m_images_test_out"
if not os.path.exists(output_dir):
	os.makedirs(output_dir)
	print 'Folder does not exist, create at {}'.format(output_dir)
else:
	print 'Dir exist'

input_list_rgb = os.listdir(input_dir_rgb)
input_list_rgb.sort()
input_list_ndvi = os.listdir(input_dir_ndvi)
input_list_ndvi.sort()

if len(input_list_rgb) != len(input_list_ndvi):
    print 'Please provide the same number of input images on each channel!'

# Loop through all images in the target directories
for i in range(len(input_list_rgb)):
    filename_rgb = input_list_rgb[i]
    # Load and resize image (RGB)
    input_image_rgb = cv2.imread(os.path.join(input_dir_rgb, filename_rgb))
    #input_image_rgb = cv2.resize(input_image_rgb, (input_shape[3],input_shape[2]))
    input_image_rgb = input_image_rgb.transpose((2,0,1))
    input_image_rgb = np.asarray([input_image_rgb])

    # Load and resize image (NDVI)
    filename_ndvi = input_list_ndvi[i]
    input_image_ndvi = cv2.imread(os.path.join(input_dir_ndvi, filename_ndvi), cv2.CV_LOAD_IMAGE_GRAYSCALE)
    #input_image_ndvi = cv2.resize(input_image_ndvi, (input_shape[3],input_shape[2]))
    #input_image_ndvi = input_image_ndvi.transpose((2,0,1))
    input_image_ndvi = np.asarray([input_image_ndvi])

    # Do forward pass
    print(filename_rgb)
    print(filename_ndvi)
    net.forward(dataNDVI=input_image_ndvi, dataRGB=input_image_rgb)
    predicted = net.blobs['prob'].data
    output = np.squeeze(predicted[0,:,:,:])
    for l in range(0,3):
        str1='%d'%l
        prob_file_name = os.path.splitext(filename_rgb)[0] +'_segnet_prob'+str1+'.png'
        scipy.misc.toimage(output[l,:,:], cmin=0.0, cmax=1.0).save(os.path.join(output_dir + '_prob', prob_file_name))
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
    predic_file_name = os.path.splitext(filename_rgb)[0]+'_segnet_predic.png'
    scipy.misc.toimage(rgb, cmin=0.0, cmax=1.0).save(os.path.join(output_dir, predic_file_name))
    continue
