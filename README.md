# weedNet-devel

Development repo for weedNet, a dense semantic segmenetation framework for weed classification, based on the Caffe deep learning framework.

<p align="center"><img src="https://cdn.pbrd.co/images/HfMjJye.png" height="240"/> </p>

## Instructions

This tutorial describes how to set up the repo for training weedNet on your computer. Before starting this tutorial, you need to have access to a GPU. Information about the `ethgpu2` workstation is available [here](https://docs.google.com/spreadsheets/d/1gZWAGAnPVVMpJuJGFkoGH0O_CZ3D9u0XBBJ4nGEEEs8/edit?ts=5ac35276#gid=0). To create a user account, please contact one of the admins: Inkyu (inkyu.sa@mavt.ethz.ch) or Zetao (chenze@ethz.ch).

### Compiling Caffe

Please consult the [official documentation](http://caffe.berkeleyvision.org/installation.html) on detailed instructions about how to install the software packages required for running Caffe. If you are using `ethgpu2`, the relevant software should already be installed, and you only need to compile using the steps below.

1. Clone this repo into the workspace of your GPU machine.

2. In a new command window, navigate to the folder `weedNet-devel/caffe-segnet-cudnn5`. Then, type:

```
ccmake .
```

3. Check that the advanced configuration setup matches the one found in [these screenshots](https://docs.google.com/document/d/1kk-9-stN8oUGd4jZauGp7Yfj81iwxsJ4Kfxs8zKYq_A/edit). Note that the paths are relative. Then, using this configuration, generate the `Makefile` in the directory. You can open the folder browser to check that this file is there with the correct time stamp.

4. Compile the Caffe framework and run the tests by typing:

```
make -j8
make test
make runtest
```

The compilation process may output some warnings, but no errors should be present here. The testing process may output an error, and this is fine. ;)

5. Finally, compile the Caffe python wrapper by typing:

```
make pycaffe
```

### Setting Up Training Scripts

1. Prepare your training data (RGB + annotated ground truth images) and the training script, `train.txt`. Examples can be found in the folder `weedNet-devel/SegNet-Tutorial/train_and_test_data` (e.g., sub-folder `Scientifica`).

2. Prepare your training script in the folder `weedNet-devel/my_scripts`. Make sure that the directories referenced in the script exist. Here's an example from the script `train_scientifica.sh`:

```
#!/bin/bash
../caffe-segnet-cudnn5/tools/caffe train -gpu 0 -solver ../SegNet-Tutorial/Models/segnet_scientifica_solver.prototxt -weights ../weights/VGG_ILSVRC_16_layers.caffemodel
```

Following this format, you need to specify:
* The location of the Caffe library: `../caffe-segnet-cudnn5/tools/caffe `. If you followed the instructions in the previous sub-section, this should be the same.
* The GPU ID to use for processing: `-gpu X`. For the `ethgpu2` workstation, X is 0 or 1 depending on [where](https://docs.google.com/spreadsheets/d/1gZWAGAnPVVMpJuJGFkoGH0O_CZ3D9u0XBBJ4nGEEEs8/edit?ts=5ac35276#gid=0) your account has been allocated.
* The optimization parameters of the network: `-solver ../SegNet-Tutorial/Models/segnet_scientifica_solver.prototxt` (see next step below).
* The structure of the network: `-weights ../weights/VGG_ILSVRC_16_layers.caffemodel`. For weedNet, we use the VGG-16 model which you can download directly from [here](http://www.robots.ox.ac.uk/~vgg/software/very_deep/caffe/VGG_ILSVRC_16_layers.caffemodel).

