# ECML2017_2


INTRODUCTION

This repository contains the original data and codes that were described in the paper "Integrating Prior Knowledge into Deep Learning".


DESCRIPTION


Dataset:

The dataset is downloadable from the link https://drive.google.com/file/d/0BxXW4upKVdaRR3dGWFk3X1Nhemc/view?usp=sharing
and when unzipped, the user should get a folder named ImageNetSubset. This folder should be placed in the current user directory   depending where the user wants to put all the images. The images belongs to animals from 7 different classes downloaded from Imagenet(http://www.image-net.org/). They have been cleaned manually to remove images which got downloaded by the name of an animal to which it didnt belong. For ex. sometimes an image of an airplane is tagged as a bird. All these unwanted and unrelated images are deleted and the dataset is cleaned. After this initial pre-processing, the dataset contains 715 images from each of the 7 classes(total of 5005 images). The 7 classes are namely:

	    1. albatross
	    2. cheetah
	    3. giraffe
	    4. ostrich
	    5. penguin
	    6. tiger
	    7. zebra

   			
 Code Folders:
 
According to the paper submitted, the semantic based regularizer(SBRS) code is present in SBRS_CAFFE.tar.7z. This semantic based regularizer is integrated with the caffe C++ API and hence needs gpu enabled caffe to be built in the machine before using the semantic based regularizer. The semantic based regularizer have two pre-requisite dependencies:

1. gpu enabled caffe
2. gflags
 
The installation instructions of gpu enabled caffe can be found here http://caffe.berkeleyvision.org/install_apt.html. Caffe itself is built using gflags, and hence the second requirement of SBRS is fulfilled automatically. 
Now, the SBRS_CAFFE code can be built in a GPU machine to obtain the executable.

To run the experiments as mentioned in the paper, the user also needs to prepare the data files in the format that SBRS_CAFFE can recognize.
   Each of the folders mentioned below contains C++ code to perform different kinds of operation for preprocessing the datasets and building 
   different configurations for the SBRS setup. The zip folders are namely
 
      	    1. Image_conversion.tar.gz
            2. Image_conversion_nontrans.tar.gz
           
    	
    Detailed description about each of these folders are present inside the .tar.gz of that folder.

 


