#!/bin/bash
../caffe-segnet-cudnn5/build/tools/caffe train -gpu 0 -solver ../SegNet-Tutorial/Models/segnet_flourish_again_solver.prototxt -weights ../weights/VGG_ILSVRC_16_layers.caffemodel
