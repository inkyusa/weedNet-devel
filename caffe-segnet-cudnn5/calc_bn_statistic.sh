#!/bin/bash
/home/enddl22/workspace/caffe-segnet-cudnn5/build/tools/caffe train -gpu 1 -solver /home/enddl22/workspace/SegNet-Tutorial/Models/segnet_solver.prototxt -weights /home/enddl22/workspace/weights/VGG_ILSVRC_16_layers.caffemodel
