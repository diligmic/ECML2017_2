# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:15:31 2015

@author: vincenzo
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 09:01:50 2015

@author: vincenzo
"""

"""
Computing confusion matrix and performance index
"""
import sys
import numpy as np
# to convert a string in a dictionary
import ast
import re


def find_classes(line):
    my_regex = "(ALBATROSS|CHEETAH|GIRAFFE|OSTRICH|PENGUIN|TIGER|ZEBRA):((-\d\.\d*)|(\d\.\d*)|(\d))"
    it = re.finditer(my_regex, line)
    # print line_split[2]
    k = 0
    for match in it:
        if k == 0:
            classes_string = match.group()
            k += 1
        else:
            classes_string += "," + match.group()
            # print classes_labels
            # print classes_values
            # print classes_labels
    return classes_string


def compute_confusion_matrix():
    # input parameters
    result_file = sys.argv[1]
    out_file = sys.argv[2]
    labels_file = sys.argv[3]

    ofile = open(out_file, "w")
    # load the the labels
    # dictionary to store the labels
    labels = {}
    labels_temp = {}
    with open(labels_file, "r") as source:
        for line in source:
            labels_line = line
            labels_temp[labels_line.split("\t")[0]] = labels_line.split("\t")[1]
    print("Length : %d" % len(labels_temp))
    # dictionay to store the predictions
    labels_temp
    predictions = {}
    # confusion_matrix indexing: 0) albatross 1)cheetah 2)giraffe 3)ostrich 4)penguin 5)tiger 6)zebra
    confusion_dict = {'ALBATROSS': 0, 'CHEETAH': 1, 'GIRAFFE': 2, 'OSTRICH': 3, 'PENGUIN': 4, 'TIGER': 5, 'ZEBRA': 6}
    confusion_matrix = np.zeros((7, 7))
    # index evaluation for each class
    table_confusion = np.zeros((7, 4))
    # used to calcualte TN
    n_pattern = 0
    with open(result_file, 'r') as infile:
        for line in infile:
            if "ALBATROSS" in line:
                n_pattern += 1
                # list_split[0] = id_pattern , list_split[1] = labels, list_split[2] = classification_results
                line_split = line.split("\t")
                print("id_data :" + str(line_split[0]) + "\n")
                print("key_exctracted:" + str(line_split[0]) + str(labels_temp[line_split[0]]))
                line_split[1] = find_classes(labels_temp[line_split[0]]).replace("ALBATROSS", "'ALBATROSS'").replace(
                    "CHEETAH", "'CHEETAH'").replace("GIRAFFE", "'GIRAFFE'").replace("OSTRICH", "'OSTRICH'").replace(
                    "PENGUIN", "'PENGUIN'").replace("TIGER", "'TIGER'").replace("ZEBRA", "'ZEBRA'")
                line_split[2] = find_classes(line_split[2]).replace("ALBATROSS", "'ALBATROSS'").replace("CHEETAH",
                                                                                                        "'CHEETAH'").replace(
                    "GIRAFFE", "'GIRAFFE'").replace("OSTRICH", "'OSTRICH'").replace("PENGUIN", "'PENGUIN'").replace(
                    "TIGER", "'TIGER'").replace("ZEBRA", "'ZEBRA'")
                groudTruth = re.findall(r"'[A-Z]+':[0-9]", str(line_split[1]))
                # print type(line_split[1])
                # print "line_split2: " + str(line_split[2])
                # labels
                # print str(line_split[1]) + "\n" + str(line_split[2])
                labels1 = "{" + ','.join(str(e) for e in groudTruth) + "}"
                labels = ast.literal_eval(labels1)
                print("Labels: " + str(labels1))
                # print type(labels1)
                predictions = ast.literal_eval("{" + line_split[2] + "}")
                # print type(predictions)
                # retrive the class with label 1. The output will be a list with one elemet
                print("Predictions: " + str(predictions))
                for name, correct_class in labels.items():
                    if correct_class == 1:
                        corr = confusion_dict[name]
                # extract the classe predicted
                # It is returned the index of the element with the maximum value among all the values
                # in the list composed from all the values predicted for all the predicates
                print("MAX : " + str(max(predictions.values())) + " " + str(predictions.values()))
                
                for key, value in predictions.items():
                    if value == max(predictions.values()):
                        predicted_class = value
                # pred =  predictions.keys()[confusion_dict.values().index(int(predicted_class))]
                pred = [key for key, value in predictions.items() if value == max(predictions.values())][0]
                confusion_matrix[int(corr)][int(confusion_dict[pred])] += 1
                print('Real class: ' + str(correct_class) + '\t' + 'corr: ' + str(
                    corr) + '\t' + 'Predicted class: ' + str(predicted_class) + '\t' + 'Pred class: ' + str(pred) + '\n')
    col_idx = 0
    for x in confusion_matrix:
        tp = x[col_idx]
        fn = np.sum(x) - tp
        fp = np.sum(confusion_matrix[:, col_idx]) - tp
        tn = n_pattern - (tp + fn) - fp
        class_confusion = [tp, fp, tn, fn]
        table_confusion[col_idx] = class_confusion
        col_idx += 1
    # Computing micro and macro statistics:
    micro_accuracy = float(table_confusion[:, 0].sum() + table_confusion[:, 2].sum()) / float(
        table_confusion[:, 0].sum() + table_confusion[:, 1].sum() + table_confusion[:, 2].sum() + table_confusion[:,
                                                                                                  3].sum())

    micro_precision = float(table_confusion[:, 0].sum()) / (
    float(table_confusion[:, 0].sum() + table_confusion[:, 1].sum()))
    # print str(table_confusion[:,0]) +"\n"+str(table_confusion[:,1].sum()) +"\n"+ str(table_confusion[:,3].sum())
    micro_recall = float(table_confusion[:, 0].sum()) / float(table_confusion[:, 0].sum() + table_confusion[:, 3].sum())
    micro_f1 = float(2 * micro_precision * micro_recall) / float(micro_precision + micro_recall)
    micro_spec = float(table_confusion[:, 2].sum()) / float(table_confusion[:, 2].sum() + table_confusion[:, 1].sum())
    print("Confusion matrix:\n" + str(confusion_matrix))
    print("Table of confusion:[TP, FP, TN, FN]\n" + str(table_confusion))
    # evaluating performances index
    print("--------- Classes results ---------")
    macro_acc = 0
    macro_prec = 0
    macro_rec = 0
    macro_f1 = 0
    macro_spec = 0
    for x in table_confusion:
        if ((x[0] + x[1] + x[2] + x[3]) != 0):
            acc = float((x[0] + x[2]) / (x[0] + x[1] + x[2] + x[3]))
        else:
            acc = 10e10
        if (x[0] + x[1]) != 0:
            prec = float(x[0] / (x[0] + x[1]))
        else:
            prec = 10e10
        if (x[0] + x[3]) != 0:
            rec = float(x[0] / (x[0] + x[3]))
        else:
            rec = 10e10
        if (2 * x[0] + x[1] + x[3]) != 0:
            fscore = float(2 * x[0] / (2 * x[0] + x[1] + x[3]))
        else:
            fscore = 10e10
        if (x[2] + x[1]) != 0:
            spec = float(x[2] / (x[2] + x[1]))
        else:
            spec=10e10
        macro_acc += acc
        macro_prec += prec
        macro_rec += rec
        macro_f1 += fscore
        macro_spec += spec
        print("----------------------------------\n" +
              "TP: " + str(x[0]) + " FP: " + str(x[1]) + " TN: " + str(x[2]) + " FN: " + str(x[3]) + "\n"
                                                                                                     "Accuracy: " + str(
            acc) + "\n" +
              "Precision: " + str(prec) + "\n" +
              "Recall: " + str(rec) + "\n" +
              "F1: " + str(fscore) + "\n" +
              "Specificity: " + str(spec) + "\n" +
              "----------------------------------")
        ofile.write("----------------------------------\n" +
                    "TP: " + str(x[0]) + " FP: " + str(x[1]) + " TN: " + str(x[2]) + " FN: " + str(x[3]) + "\n"
                                                                                                           "Accuracy: " + str(
            acc) + "\n" +
                    "Precision: " + str(prec) + "\n" +
                    "Recall: " + str(rec) + "\n" +
                    "F1: " + str(fscore) + "\n" +
                    "Specificity: " + str(spec) + "\n" +
                    "----------------------------------")
    macro_acc = macro_acc / 7
    macro_prec = macro_prec / 7
    macro_rec = macro_rec / 7
    macro_f1 = macro_f1 / 7
    macro_spec = macro_spec / 7
    ofile.write("----------------------------------\n" +
                "####### MICRO STATISTICS #######\n" +
                "Accuracy: " + str(micro_accuracy) + "\n" +
                "Precision: " + str(micro_precision) + "\n" +
                "Recall: " + str(micro_recall) + "\n" +
                "F1: " + str(micro_f1) + "\n" +
                "Specificity: " + str(micro_spec) + "\n" +
                "################################\n" +
                "----------------------------------\n" +
                "----------------------------------\n" +
                "####### MACRO STATISTICS #######\n " +
                "Accuracy: " + str(macro_acc) + "\n" +
                "Precision: " + str(macro_prec) + "\n" +
                "Recall: " + str(macro_rec) + "\n" +
                "F1: " + str(macro_f1) + "\n" +
                "Specificity: " + str(macro_spec) + "\n" +
                "################################\n" +
                "----------------------------------")
    print("----------------------------------\n" +
          "####### MICRO STATISTICS #######\n" +
          "Accuracy: " + str(micro_accuracy) + "\n" +
          "Precision: " + str(micro_precision) + "\n" +
          "Recall: " + str(micro_recall) + "\n" +
          "F1: " + str(micro_f1) + "\n" +
          "Specificity: " + str(micro_spec) + "\n" +
          "################################\n" +
          "----------------------------------\n" +
          "----------------------------------\n" +
          "####### MACRO STATISTICS #######\n" +
          "Accuracy: " + str(macro_acc) + "\n" +
          "Precision: " + str(macro_prec) + "\n" +
          "Recall: " + str(macro_rec) + "\n" +
          "F1: " + str(macro_f1) + "\n" +
          "Specificity: " + str(macro_spec) + "\n" +
          "################################\n" +
          "----------------------------------")
    ofile.close()


def main():
    compute_confusion_matrix()


if __name__ == "__main__":
    main()
