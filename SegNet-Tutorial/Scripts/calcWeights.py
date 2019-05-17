#!/usr/bin/env python
from __future__ import print_function
import numpy as np
import argparse
import os
from PIL import Image
from os import listdir
import sys
import collections


# Import arguments
# python ./calcWeights.py --dir /home/enddl22/workspace/SegNet-Tutorial/SequoiaMulti/trainannot
parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, help='Path to the folder containing the images with annotations')
args = parser.parse_args()

if args.dir:
    cwd = args.dir
    if not args.dir.endswith('/'): cwd = cwd + '/'
else:
    cwd = os.getcwd() + '/'

image_names = listdir(cwd)
# Keep only images and append image_names to directory
image_list = [cwd + s for s in image_names if s.lower().endswith(('.png', '.jpg', '.jpeg'))]
#del image_list[3:]
print ("Number of images:", len(image_list))
img=Image.open(image_list[0])
img_w=img.size[0]
img_h=img.size[1]
print("img_w=",img_w)
print("img_h=",img_h)

def count_all_pixels(image_list):
    dic_class_imgcount = dict()
    overall_pixelcount = dict()
    result = dict()
    for img in image_list:
        sys.stdout.write('.')
        sys.stdout.flush()
        for key, value in get_class_per_image(img).items():
            # Sum up the number of classes returned from get_class_per_image function
            overall_pixelcount[key] = overall_pixelcount.get(key, 0) + value
            # If the class is present in the image, then increase the value by one
            # shows in how many images a particular class is present
            dic_class_imgcount[key] = dic_class_imgcount.get(key, 0) + 1
    print ("Done")
    # Save above 2 variables in a list
    for (k, v), (k2, v2) in zip(overall_pixelcount.items(), dic_class_imgcount.items()):
        if k != k2: print ("This was impossible to happen, but somehow it did"); exit()
        result[k] = [v, v2]
    return result


def get_class_per_image(img):
    dic_class_pixelcount = dict()
    im = Image.open(img)
    pix = im.load()
    for x in range(img_w):
        for y in range(img_h):
            dic_class_pixelcount[pix[x, y]] = dic_class_pixelcount.get(pix[x, y], 0) + 1
    #del dic_class_pixelcount[11]
    return dic_class_pixelcount

def cal_class_weights_deeplab(data):
    total_num_pixel=img_h * img_w * len(image_list)
    total_num_pixel_sum=[]
    print("The total # of pixel = ",total_num_pixel)
    cls_num_pixel=[]
    for i,(key,val) in enumerate(data.items()):
        print("class id={}, # pixels={}, # of appeared images ={}".format(key,val[0],val[1]))
        cls_num_pixel.append(val[0])
    min_cls_num_pixel=min(cls_num_pixel)
    print("The sum of # of pixel for each class=",sum(cls_num_pixel))
    cls_weight=[]
    for pixel in cls_num_pixel:
        cls_weight.append(pixel/min_cls_num_pixel)
    print("=========================================")
    print(" pixel ratio, normalized by the number \n")
    print(" of pixels of the least frequent class")
    print(" Note that this is for deeplab loss weight")
    print("=========================================")
    for i, v in enumerate(cls_weight):
        print ("    class", i, "weight:", round(v, 4))
    print("Copy this")
    print("label_weights=", cls_weight)
    print("\n\n\n")


def cal_class_weights(image_list):
    freq_images = dict()
    weights = collections.OrderedDict()
    # calculate freq per class
    data_statistic=count_all_pixels(image_list)
    cal_class_weights_deeplab(data_statistic)
    for k, (v1, v2) in data_statistic.items():
        freq_images[k] = v1 / (v2 * img_h * img_w * 1.0)
    # calculate median of freqs
    median = np.median(freq_images.values())
    print('median=',median)
    # calculate weights
    for k, v in freq_images.items():
        weights[k] = median / v
        #print('k=',k)
        #print('v=',v)
    return weights

results = cal_class_weights(image_list)

print("=========================================")
print(" Frequency ratio for SegNet            \n")
print("=========================================")
# Print the results
for k, v in results.items():
    print("    class", k, "weight:", round(v, 4))

print("Copy this:")
for k, v in results.items():
    print("    class_weighting:", round(v, 4))