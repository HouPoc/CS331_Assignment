from preprocess import *
from math import log
import numpy

######
# Purpose: Implement Naive Bayes algorithm
# Return: Accuracy of this data set
######
def naive_bayes(train_data, test_data):
	P_class = []
	distribution = []
	
	training_phase(train_data, distribution, P_class)	
	return testing_phase(test_data, distribution, P_class)

######
# Purpose: Calculate distribution of train data
# Return: None
######
def training_phase(matrix, distribution, P_class):
	num_C1 = 0.

	for i in matrix:
		if i[-1] == 1:
			num_C1 += 1.

	num_C0 = len(matrix) - num_C1
	
	P_class.append(num_C0 / len(matrix))	# P(C=0)
	P_class.append(num_C1 / len(matrix))	# P(C=1)

	size = len(matrix[0]) - 1

	for i in range(size):
		num_A0C0 = 0.
		num_A1C0 = 0.
		num_A0C1 = 0.
		num_A1C1 = 0.
		result = []
		for row in matrix:
			if row[-1] == 0:
				if row[i] == 0:	
					num_A0C0 += 1.
				else:
					num_A1C0 += 1.
			else:
				if row[i] == 0:
					num_A0C1 += 1.
				else:
					num_A1C1 += 1.
		# Dirichlet Priors
		result.append((num_A0C0 + 1.)/(num_C0 + 2.))	# P(A=0|C=0)
		result.append((num_A1C0 + 1.)/(num_C0 + 2.))	# P(A=1|C=0) 
		result.append((num_A0C1 + 1.)/(num_C1 + 2.))	# P(A=0|C=1)
		result.append((num_A1C1 + 1.)/(num_C1 + 2.))	# P(A=1|C=1)
	
		distribution.append(result)

######
# Purpose: Predict classlabel of each instance in test data according to distribution
# Return: Accuracy of this data set
######
def testing_phase(data, distribution, P_class):
	answer_class_label = []
	test_class_label = []
	correct = 0.

	for features in data:
		PC0 = 0.
		PC1 = 0.
		for i in range(len(features)-1):
			if (features[i] == 1):
				PC0 = PC0 + log(distribution[i][1])
				PC1 = PC1 + log(distribution[i][3])
			else:
				PC0 = PC0 + log(distribution[i][0])
				PC1 = PC1 + log(distribution[i][2])
	
		PC0 = PC0 + log(P_class[0])
		PC1 = PC1 + log(P_class[1])
		
		if PC0 > PC1:
			test_class_label = 0
		else:
			test_class_label = 1

		if features[-1] == test_class_label:
			correct += 1. 
	
	return "{0:.2f}%".format(correct / len(data) * 100)