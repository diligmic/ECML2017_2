# ECML2017_2
Introduction

This repository contains the original data and codes that were described in the paper "Integrating Prior Knowledge into Deep Learning".

------------------------------------------------  DESCRIPTION --------------------------------------------------------------
DATASET:

The dataset is downloadable from the link https://drive.google.com/file/d/0BxXW4upKVdaRR3dGWFk3X1Nhemc/view?usp=sharing
and when unzipped, you should get a folder named ImageNetSubset. This folder should be placed in the current user directory   depending on where the user wants to put all the images. The images belongs to animals from 7 different classes downloaded from Imagenet(http://www.image-net.org/). They have been cleaned manually to remove images which got downloaded by the name of an animal to which it didnt belong. For ex. sometimes an image of an airplane is tagged as a bird. All these unwanted and unrelated images are deleted and the dataset is cleaned. After this initial pre-processing, the dataset contains 715 images from each of the 7 classes(total of 5005 images). The 7 classes are namely:

	    1. albatross
	    2. cheetah
	    3. giraffe
	    4. ostrich
	    5. penguin
	    6. tiger
	    7. zebra

   			
   CODE FOLDERS:
   Each of the folders mentioned below contains C++ code to perform different kinds of operation for preprocessing the datasets and building 
   different configurations for the SBRS setup. The zip folders are namely
 
      	    1. Image_conversion.tar.gz
            2. Image_conversion_nontrans.tar.gz
           
    	
    Detailed description about each of these folders are present inside the .tar.gz of that folder.

 


