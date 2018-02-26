# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.6

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/enddl22/workspace/caffe-segnet-cudnn5

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/enddl22/workspace/caffe-segnet-cudnn5

# Utility rule file for docs.

# Include the progress variables for this target.
include docs/CMakeFiles/docs.dir/progress.make

docs/CMakeFiles/docs:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/enddl22/workspace/caffe-segnet-cudnn5/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Launching doxygen..."
	/usr/bin/doxygen /home/enddl22/workspace/caffe-segnet-cudnn5/.Doxyfile

docs: docs/CMakeFiles/docs
docs: docs/CMakeFiles/docs.dir/build.make
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Copying notebook examples/00-classification.ipynb to /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/00-classification.ipynb"
	/usr/bin/cmake -E make_directory /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples
	/usr/bin/python2.7 scripts/copy_notebook.py examples/00-classification.ipynb /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/00-classification.ipynb
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Copying notebook examples/01-learning-lenet.ipynb to /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/01-learning-lenet.ipynb"
	/usr/bin/cmake -E make_directory /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples
	/usr/bin/python2.7 scripts/copy_notebook.py examples/01-learning-lenet.ipynb /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/01-learning-lenet.ipynb
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Copying notebook examples/02-fine-tuning.ipynb to /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/02-fine-tuning.ipynb"
	/usr/bin/cmake -E make_directory /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples
	/usr/bin/python2.7 scripts/copy_notebook.py examples/02-fine-tuning.ipynb /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/02-fine-tuning.ipynb
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Copying notebook examples/brewing-logreg.ipynb to /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/brewing-logreg.ipynb"
	/usr/bin/cmake -E make_directory /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples
	/usr/bin/python2.7 scripts/copy_notebook.py examples/brewing-logreg.ipynb /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/brewing-logreg.ipynb
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Copying notebook examples/detection.ipynb to /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/detection.ipynb"
	/usr/bin/cmake -E make_directory /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples
	/usr/bin/python2.7 scripts/copy_notebook.py examples/detection.ipynb /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/detection.ipynb
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Copying notebook examples/net_surgery.ipynb to /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/net_surgery.ipynb"
	/usr/bin/cmake -E make_directory /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples
	/usr/bin/python2.7 scripts/copy_notebook.py examples/net_surgery.ipynb /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/net_surgery.ipynb
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Copying notebook examples/pascal-multilabel-with-datalayer.ipynb to /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/pascal-multilabel-with-datalayer.ipynb"
	/usr/bin/cmake -E make_directory /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples
	/usr/bin/python2.7 scripts/copy_notebook.py examples/pascal-multilabel-with-datalayer.ipynb /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/pascal-multilabel-with-datalayer.ipynb
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Copying notebook examples/siamese/mnist_siamese.ipynb to /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/siamese/mnist_siamese.ipynb"
	/usr/bin/cmake -E make_directory /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/siamese
	/usr/bin/python2.7 scripts/copy_notebook.py examples/siamese/mnist_siamese.ipynb /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/siamese/mnist_siamese.ipynb
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Creating symlink /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/cifar10.md -> /home/enddl22/workspace/caffe-segnet-cudnn5/examples/cifar10/readme.md"
	/usr/bin/cmake -E make_directory /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples
	ln -sf /home/enddl22/workspace/caffe-segnet-cudnn5/examples/cifar10/readme.md /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/cifar10.md
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Creating symlink /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/cpp_classification.md -> /home/enddl22/workspace/caffe-segnet-cudnn5/examples/cpp_classification/readme.md"
	/usr/bin/cmake -E make_directory /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples
	ln -sf /home/enddl22/workspace/caffe-segnet-cudnn5/examples/cpp_classification/readme.md /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/cpp_classification.md
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Creating symlink /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/feature_extraction.md -> /home/enddl22/workspace/caffe-segnet-cudnn5/examples/feature_extraction/readme.md"
	/usr/bin/cmake -E make_directory /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples
	ln -sf /home/enddl22/workspace/caffe-segnet-cudnn5/examples/feature_extraction/readme.md /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/feature_extraction.md
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Creating symlink /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/finetune_flickr_style.md -> /home/enddl22/workspace/caffe-segnet-cudnn5/examples/finetune_flickr_style/readme.md"
	/usr/bin/cmake -E make_directory /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples
	ln -sf /home/enddl22/workspace/caffe-segnet-cudnn5/examples/finetune_flickr_style/readme.md /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/finetune_flickr_style.md
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Creating symlink /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/imagenet.md -> /home/enddl22/workspace/caffe-segnet-cudnn5/examples/imagenet/readme.md"
	/usr/bin/cmake -E make_directory /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples
	ln -sf /home/enddl22/workspace/caffe-segnet-cudnn5/examples/imagenet/readme.md /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/imagenet.md
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Creating symlink /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/mnist.md -> /home/enddl22/workspace/caffe-segnet-cudnn5/examples/mnist/readme.md"
	/usr/bin/cmake -E make_directory /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples
	ln -sf /home/enddl22/workspace/caffe-segnet-cudnn5/examples/mnist/readme.md /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/mnist.md
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Creating symlink /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/siamese.md -> /home/enddl22/workspace/caffe-segnet-cudnn5/examples/siamese/readme.md"
	/usr/bin/cmake -E make_directory /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples
	ln -sf /home/enddl22/workspace/caffe-segnet-cudnn5/examples/siamese/readme.md /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/siamese.md
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Creating symlink /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/web_demo.md -> /home/enddl22/workspace/caffe-segnet-cudnn5/examples/web_demo/readme.md"
	/usr/bin/cmake -E make_directory /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples
	ln -sf /home/enddl22/workspace/caffe-segnet-cudnn5/examples/web_demo/readme.md /home/enddl22/workspace/caffe-segnet-cudnn5/docs/gathered/examples/web_demo.md
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Creating symlink /home/enddl22/workspace/caffe-segnet-cudnn5/docs/doxygen -> /home/enddl22/workspace/caffe-segnet-cudnn5/doxygen/html"
	cd /home/enddl22/workspace/caffe-segnet-cudnn5/docs && ln -sfn /home/enddl22/workspace/caffe-segnet-cudnn5/doxygen/html doxygen
.PHONY : docs

# Rule to build all files generated by this target.
docs/CMakeFiles/docs.dir/build: docs

.PHONY : docs/CMakeFiles/docs.dir/build

docs/CMakeFiles/docs.dir/clean:
	cd /home/enddl22/workspace/caffe-segnet-cudnn5/docs && $(CMAKE_COMMAND) -P CMakeFiles/docs.dir/cmake_clean.cmake
.PHONY : docs/CMakeFiles/docs.dir/clean

docs/CMakeFiles/docs.dir/depend:
	cd /home/enddl22/workspace/caffe-segnet-cudnn5 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/enddl22/workspace/caffe-segnet-cudnn5 /home/enddl22/workspace/caffe-segnet-cudnn5/docs /home/enddl22/workspace/caffe-segnet-cudnn5 /home/enddl22/workspace/caffe-segnet-cudnn5/docs /home/enddl22/workspace/caffe-segnet-cudnn5/docs/CMakeFiles/docs.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : docs/CMakeFiles/docs.dir/depend

