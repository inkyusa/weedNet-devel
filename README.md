# weedNet-devel

Development repo for weedNet, a dense semantic segmenetation framework for weed classification, based in the Caffe deep learning framework.

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
* The location of the Caffe library: `../caffe-segnet-cudnn5/tools/caffe `. If you followed the instructions in the previous section, this should be the same.
* The GPU ID to use for processing: `-gpu X`. For the `ethgpu2` workstation, X is 0 or 1 depending on [where](https://docs.google.com/spreadsheets/d/1gZWAGAnPVVMpJuJGFkoGH0O_CZ3D9u0XBBJ4nGEEEs8/edit?ts=5ac35276#gid=0) your account has been allocated.
* The optimization parameters for the network training: `-solver ../SegNet-Tutorial/Models/segnet_scientifica_solver.prototxt` (see next step below).
* The structure of the network: `-weights ../weights/VGG_ILSVRC_16_layers.caffemodel`. For weedNet, we use the VGG-16 model which you can download directly from [here](http://www.robots.ox.ac.uk/~vgg/software/very_deep/caffe/VGG_ILSVRC_16_layers.caffemodel).

3. Prepare the optimization parameters for the network in the folder `weedNet-devel/SegNet-Tutorial/Models`. Again, 
that the directories referenced in the script exist. Here's an example from the script `segnet_scientifica_solver.prototxt`, showing the values that you can change:

<p align="center"><img src="https://cdn.pbrd.co/images/HfMYY3e.png" height="180"/> </p>

In Caffe, a 'snapshot' is a configuration file capturing the solver state a particular time (in the example, every 1000 iterations). This can be used to resume learning later from a particular state.

4. Prepare the structure of the network model in the folder `weedNet-devel/SegNet-Tutorial/Models`. This file specifies the source of the input data stream and the data flow within the network architecture. An example can be found in `segnet_scientifica_train.prototxt`. Here, you need to change the `source` of the first layer to the absolute path of your data file (`train.txt` from the previous section). For weedNet, the network connectivity should be unchanged, based on the VGG-16 model. You are now ready to train!

### Training the Model

1. In a new command terminal, set up an SSH connection to the GPU. Then, navigate to the folder of your training script (from Step 2 in the previous section - `weedNet-devel/my_scripts`), and simply execute the script.

To check the GPU status, you can type the command `nvidia-smi`. The example below indicates that both GPUs on `ethgpu2` are currently in use. In this case, you need to wait until a processor frees up before starting training.

<p align="center"><img src="https://cdn.pbrd.co/images/HfN40Jn.png" height="240"/> </p>

To leave the ssh window while keeping the training the job running, the [tmux](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/) command line tool is very useful. This allows you to create virtual sessions using a remote terminal. Some useful commands:

* To *leave* a session (e.g., after starting the training job): `CTRL+B` followed by `D`.
* To *list* all sessions: `tmux list-sessions`.
* To *enter* an existing session: `tmux attach -t X`, where X is the name of your session.
* To *change the name* of a session (while inside it): `CTRL+B` followed by `SHIFT + 4`.

### Testing the Model

The Batch Normalization layers in SegNet shift the input feature maps according to their mean and variance statistics for each mini batch during training. At test time we must use the statistics for the entire dataset. The steps below explain how to do this.

1. Prepare the script in `weedNet-devel/my_scripts`. Make sure that the directories referenced in the script exist. Here's an example from the script `calc_bn_statistic_scientifica.sh`:

```
#!/bin/bash
CUR_PATH=$(pwd)
python ../SegNet-Tutorial/Scripts/compute_bn_statistics.py ../SegNet-Tutorial/Models/segnet_scientifica_train.prototxt ../SegNet-Tutorial/Models/Training/segnet_scientifica/segnet_scientifica_iter_40000.caffemodel ../SegNet-Tutorial/Models/Inference/
```
Following this format, you need to specify:
* The script for calculating the Batch Normalization statistics: `../SegNet-Tutorial/Scripts/compute_bn_statistics.py`. This should be the same. In this file, you need to change Lines 9 and 10 to the target GPU ID and folder of your Caffe installation, respectively.
* The model structure file: `../SegNet-Tutorial/Models/segnet_scientifica_train.prototxt`.
* The trained model from the snapshots: `../SegNet-Tutorial/Models/Training/segnet_scientifica/segnet_scientifica_iter_40000.caffemodel` (obtained from the previous section).

2. Navigate to the folder of your script (`weedNet-devel/my_scripts`) and simply execute it. Congratulations, you now have your model!

### Help
* [tmux cheatsheet](https://gist.github.com/MohamedAlaa/2961058)
* [Caffe training guide](http://shengshuyang.github.io/A-step-by-step-guide-to-Caffe.html)
* [SegNet tutorial](http://mi.eng.cam.ac.uk/projects/segnet/tutorial.html)

