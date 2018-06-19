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

model='/home/mpopovic/workspace/weedNet-devel/SegNet-Tutorial/Models/segnet_ipp_rit18_inference_live.prototxt'

weights='/home/mpopovic/workspace/weedNet-devel/SegNet-Tutorial/Models/Inference/test_weights_rit18_10m_15m_20m_asphalt.caffemodel'

caffe.set_mode_gpu()
caffe.set_device(GPU_ID)

net = caffe.Net(model,
                weights,
                caffe.TEST)

input_shape = net.blobs['data'].data.shape
output_shape = net.blobs['prob'].data.shape

# Directory to load images from
input_dir_rgb = "rit-18/10m_15m_20m/10m_images_test"
input_dir_ir1 = "rit-18/10m_15m_20m/10m_images_test_ir1"
input_dir_ir2 = "rit-18/10m_15m_20m/10m_images_test_ir2"
input_dir_ir3 = "rit-18/10m_15m_20m/10m_images_test_ir3"
# Directory to save images to
output_dir = "rit-18/10m_15m_20m_asphalt_training/10m_images_test_out"
if not os.path.exists(output_dir):
	os.makedirs(output_dir)
	print 'Folder does not exist, create at {}'.format(output_dir)
else:
	print 'Dir exist'

input_list_rgb = os.listdir(input_dir_rgb)
input_list_rgb.sort()
input_list_ir1 = os.listdir(input_dir_ir1)
input_list_ir1.sort()
input_list_ir2 = os.listdir(input_dir_ir2)
input_list_ir2.sort()
input_list_ir3 = os.listdir(input_dir_ir3)
input_list_ir3.sort()

# Loop through all images in the target directories
for i in range(len(input_list_rgb)):
    filename_rgb = input_list_rgb[i]
    # Load and resize image (RGB).
    input_image_rgb = cv2.imread(os.path.join(input_dir_rgb, filename_rgb))
    input_image_rgb = input_image_rgb.transpose((2,0,1))
    input_image_rgb = np.asarray([input_image_rgb])

    # Load and resize image (IR1).
    filename_ir1 = input_list_ir1[i]
    input_image_ir1 = cv2.imread(os.path.join(input_dir_ir1, filename_ir1), cv2.CV_LOAD_IMAGE_GRAYSCALE)
    input_image_ir1 = np.asarray([input_image_ir1])
    # Load and resize image (IR2).
    filename_ir2 = input_list_ir2[i]
    input_image_ir2 = cv2.imread(os.path.join(input_dir_ir2, filename_ir2), cv2.CV_LOAD_IMAGE_GRAYSCALE)
    input_image_ir2 = np.asarray([input_image_ir2])
    # Load and resize image (IR3).
    filename_ir3 = input_list_ir3[i]
    input_image_ir3 = cv2.imread(os.path.join(input_dir_ir3, filename_ir3), cv2.CV_LOAD_IMAGE_GRAYSCALE)
    input_image_ir3 = np.asarray([input_image_ir3])

    # Do forward pass.
    print(filename_rgb)
    net.forward(dataIR1=input_image_ir1, dataIR2=input_image_ir2, dataIR3=input_image_ir3, dataRGB=input_image_rgb)
    predicted = net.blobs['prob'].data
    output = np.squeeze(predicted[0,:,:,:])
    ind = np.argmax(output, axis=0)
    predic_file_name = os.path.splitext(filename_rgb)[0]+'_segnet_predic.png'
    scipy.misc.toimage(ind, low=0.0, high=output_shape[1]-1).save(os.path.join(output_dir, predic_file_name))
    continue
