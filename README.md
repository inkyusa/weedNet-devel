# weedNet-devel

Development repo for weedNet, a dense semantic segmenetation framework for weed classification, based on the Caffe deep learning framework.

## Instructions

This tutorial describes how to set up the repo for training weedNet on your computer. Before starting this tutorial, you need to have access to a GPU. Information about the `ethgpu2` workstation is available [here](https://docs.google.com/spreadsheets/d/1gZWAGAnPVVMpJuJGFkoGH0O_CZ3D9u0XBBJ4nGEEEs8/edit?ts=5ac35276#gid=0). To create a user account, please contact one of the admins: Inkyu (inkyu.sa@mavt.ethz.ch) or Zetao (chenze@ethz.ch).

### Compiling Caffe

Please consult the [official documentation](http://caffe.berkeleyvision.org/installation.html) on detailed instructions about how to install the software packages required for running Caffe. If you are using `ethgpu2`, the relevant software should already be installed, and you only need to compile using the steps below.

1. Clone this repo into the workspace of your GPU machine.

2. In a new command window, navigate to the folder `weedNet-devel/caffe-segnet-cudnn5`. Then, type:

```
ccmake .
```

3. Check that the advanced configuration setup matches the one found in [these screenshots](https://docs.google.com/document/d/1kk-9-stN8oUGd4jZauGp7Yfj81iwxsJ4Kfxs8zKYq_A/edit). Note that the paths are relative. Then, using this configuration, generate the `Makefile` in the directory. You can open the folder browser to check.

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

