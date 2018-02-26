#!/bin/bash
max=10
fileName='titanProcTime.txt'
for ((i=0; i< $max;i++))
do
	echo -e "\e[1;32mIteration=$i/$max\e[0m"
	#python test_segmentation_sequoiaMulti_30_with_finetune.py | grep 'Processing' >>$fileName;
	python test_segmentation_sequoiaMulti_30_with_finetune.py | grep 'Processing' >>$fileName;
	echo "">>$fileName
done