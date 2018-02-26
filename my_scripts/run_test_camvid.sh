#!/bin/bash
#CUR_PATH=$(pwd)
python ../SegNet-Tutorial/Scripts/test_segmentation_camvid_save_gt_pred.py --gpu 1 --model ../SegNet-Tutorial/Models/segnet_inference.prototxt --weights ../SegNet-Tutorial/Models/Inference/segnet_test_weights.caffemodel --iter 233
