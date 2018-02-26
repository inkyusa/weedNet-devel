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

print "Number of images:", len(image_list)

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
    print "Done"
    # Save above 2 variables in a list
    for (k, v), (k2, v2) in zip(overall_pixelcount.items(), dic_class_imgcount.items()):
        if k != k2: print ("This was impossible to happen, but somehow it did"); exit()
        result[k] = [v, v2]
    return result


def get_class_per_image(img):
    dic_class_pixelcount = dict()
    im = Image.open(img)
    pix = im.load()
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            dic_class_pixelcount[pix[x, y]] = dic_class_pixelcount.get(pix[x, y], 0) + 1
    #del dic_class_pixelcount[11]
    return dic_class_pixelcount


def cal_class_weights(image_list):
    freq_images = dict()
    weights = collections.OrderedDict()
    # calculate freq per class
    for k, (v1, v2) in count_all_pixels(image_list).items():
        freq_images[k] = v1 / (v2 * 360 * 480 * 1.0)
    # calculate median of freqs
    median = np.median(freq_images.values())
    # calculate weights
    for k, v in freq_images.items():
        weights[k] = median / v
    return weights

results = cal_class_weights(image_list)

# Print the results
for k, v in results.items():
    print "    class", k, "weight:", round(v, 4)

print "Copy this:"
for k, v in results.items():
    print "    class_weighting:", round(v, 4)