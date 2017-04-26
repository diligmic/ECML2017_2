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
 
According to the paper submitted, the semantic based regularizer(SBRS) code is present in SBRS_CAFFE.tar.7z. 

Step 1:

This semantic based regularizer is integrated with the caffe C++ API and hence needs gpu enabled caffe to be built in the machine before using the semantic based regularizer. The semantic based regularizer have two pre-requisite dependencies:

	1. gpu enabled caffe
	2. gflags
 
The installation instructions of gpu enabled caffe can be found here http://caffe.berkeleyvision.org/install_apt.html. Caffe itself is built using gflags, and hence the second requirement of SBRS is fulfilled automatically. 

Step 2:

Now, the SBRS_CAFFE code can be built in a GPU machine to obtain the executable.

Step 3:

To run the experiments as mentioned in the paper, the user also needs to prepare the data files in the format that SBRS_CAFFE can recognize. SBRS_CAFFE in the transductive mode (as mentioned in the paper : all the images are seen during training) requires all the pixel values of all the patterns (5005 images) placed in the data file, and there corresponding labels in the examples files. Some of the examples are seen during the training (3325 examples), some during validation (770 examples) and the remaining labels are used only for the testing purposes (910 examples). 

To prepare the datafiles, the code Image_conversion.tar.7z is provided. This code should be unzipped and built using the following dependencies:

	1.opencv (Installation instructions: http://docs.opencv.org/trunk/d7/d9f/tutorial_linux_install.html)
	2.boost_regex(Installation instruction: http://www.boost.org/)
	
Step 4:

Three different configurations are derived while building the code Image_conversion. The first configuration refers to the transductive mode with fully labelled examples (as mentioned in the paper) while the second configuration refers to the same mode with partially labelled examples (as mentioned in the paper). There is also a third configuration which refers to the transductive mode but the patterns are not randomnly sampled as in the fully labelled mode, but instead the examples of the first 475 patterns of each class are placed in the training example file, the next 130 examples of each class are placed in the test example file whereas the last 110 examples of each class are placed in the validation example file.  To run the executable for Image_conversion the following command line can be used depending on the image size that the user wants to use as input to the SBRS:

./Image_conversion  --input_dir=<path_of_the_input_directory_where_the_folder_ImageNetSubset_with_all_the_images_reside>  --output_dir=<path_where_all_data_and_examples_files_are_created>  --image_size=<32/64/128/227/256>

Step 5:

After running the above step, the following files will be created like TransData.dat, TrainExamples.dat, TestExamples.dat,ValidationExamples.dat. These files can then be used as inputs to the SBRS. Some of the sample files are also provided in the zipped folder Input_files.tar.7z which can also be used as inputs to the SBRS.

Step 6:

Finally, the SBRS_CAFFE executable can be used with the following commandline to perform the experiments

1. (When rules or constraints are not used)
./SBRS_CAFFE --transductive --training_data_file=DataTrans.txt --training_examples_file=TrainExamples.txt --test_examples_file=TestExamples.txt --validation_examples_file=ValidationExamples.txt --predicates_file=Predicates.txt --rules_file= --max_iterations=<no_of_iterations_for_training> --lambda_labeled_values=1 --lambda_regularization_values=0.001 --learning_rate=0.001 --learning_type=RGD --function_type=NEURAL_NETWORK --model_file=model_file.prototxt --output_dir=./out --input_dir=. --nn_pre_built_inputs=true 

2. (When rules or constraints are used)
./SBRS_CAFFE --transductive --training_data_file=DataTrans.txt --training_examples_file=TrainExamples.txt --test_examples_file=TestExamples.txt --validation_examples_file=ValidationExamples.txt --predicates_file=Predicates.txt --rules_file=Rules.txt  --max_iterations=<no_of_iterations_for_training> --lambda_labeled_values=1 --lambda_regularization_values=0.001 --learning_rate=0.001 --learning_type=RGD --function_type=NEURAL_NETWORK --model_file=model_file.prototxt --output_dir=./out --input_dir=. --nn_pre_built_inputs=true --lambda_constraint_values=0.1 --iteration_start_constraints=<iterations_after_which_contraints_are_applied> --learning_rate_for_constraints=0.000005 --run_collective_classification_after_train

All the other required files that were used in the paper like the Predicates.txt, Rules.txt and model_file.prototxt(that defines the caffe neural network model) are all placed in the Input_files.tar.7z folder. 

Step 7:

The output folder of the SBRS_CAFFE gives the classification outputs for all predicates. The output folder in turn contains two sub folders: one that gives the normal classification output of the clasification task and the other that gives the collective classification output for all the predicates.

Step 8:

In order to evaluate the classification output of only the final classes or predicates (7 animal categories) the python evaluate_results_05_10.py script is used.
 


