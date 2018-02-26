#!/bin/bash
CUR_PATH=$(pwd)
python ../SegNet-Tutorial/Scripts/compute_bn_statistics.py ../SegNet-Tutorial/Models/segnet_scientifica_train.prototxt ../SegNet-Tutorial/Models/Training/segnet_scientifica/segnet_scientifica_iter_40000.caffemodel ../SegNet-Tutorial/Models/Inference/
