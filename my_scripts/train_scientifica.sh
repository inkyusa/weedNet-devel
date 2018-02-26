#!/bin/bash
../caffe-segnet-cudnn5/tools/caffe train -gpu 0 -solver ../SegNet-Tutorial/Models/segnet_scientifica_solver.prototxt -weights ../weights/VGG_ILSVRC_16_layers.caffemodel
