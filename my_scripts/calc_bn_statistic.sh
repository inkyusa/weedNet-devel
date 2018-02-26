#!/bin/bash
CUR_PATH=$(pwd)
python ../SegNet-Tutorial/Scripts/compute_bn_statistics.py ../SegNet-Tutorial/Models/segnet_flourish_again_train.prototxt ../SegNet-Tutorial/Models/Training/segnet_flourish_again/segnet_flourish_again_iter_40000.caffemodel ../SegNet-Tutorial/Models/Inference/
