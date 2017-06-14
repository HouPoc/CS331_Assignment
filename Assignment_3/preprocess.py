import string
import re
import numpy as np

######
# Purpose: Create bag of words based on data in input file
# Return: A list including words from input file.
######
def get_vocabulary(input_file):
	vocabulary = []
	stop_words = read_list("stop_word_list.txt")

	f = open(input_file, 'r')
	data_set = f.readlines()
	for sentence in data_set:
		sentence = filtrate_sentence(sentence)
		for word in sentence:
			if filtrate_word(word, vocabulary, stop_words):
				vocabulary.append(word)	
	f.close()

	return vocabulary

######
# Purpose: Build feature vectors and output them to preprcoess file
# Return: None
######
def preprocess(vocabulary, input_file, out_file):
	class_label = []
	feature_vectors = make_feature_vector(input_file, vocabulary, class_label)
	return generate_out_file(out_file, feature_vectors, vocabulary, class_label)

######
# Purpose: Filtrate some words which are repeated or stop words.
# Return: Boolean value
######
def filtrate_word(word, vocabulary, stop_words):
	if(word in vocabulary):
		return False
	if(word in stop_words):
		return False
	else:
		return True

######
# Purpose: Filtrate a sentence such as removing punctuation and digit
# Return: A list including all words in this sentence
######
def filtrate_sentence(sentence):
	sentence = sentence.lower()
	sentence = re.sub(r"what's", "what is ", sentence)
	sentence = re.sub(r"\'s", " ", sentence)
	sentence = re.sub(r"\'ve", " have ", sentence)
	sentence = re.sub(r"can't", "cannot ", sentence)
	sentence = re.sub(r"couldn't", " could not ", sentence)
	sentence = re.sub(r"n't", " not ", sentence)
	sentence = re.sub(r"i'm", "i am ", sentence)
	sentence = re.sub(r"\'re", " are ", sentence)
	sentence = re.sub(r"\'d", " would ", sentence)
	sentence = re.sub(r"\'ll", " will ", sentence)
	sentence = re.sub(r",", " ", sentence)
	sentence = "".join(l for l in sentence if l not in string.punctuation)
	sentence = "".join([l for l in sentence if not l.isdigit()])
	
	return sentence.split()

######
# Purpose: Build feature vectors
# Return: A matrix including all feature vectors and class labels
######
def make_feature_vector(input_file, vocabulary, class_label):	
	f = open(input_file, 'r')
	data_set = f.readlines()
	matrix = []

	for sentence in data_set:
		temp = sentence.split()
		class_label.append(int(temp[-1]))
		sentence = filtrate_sentence(sentence)
		row = []	
		for j in range(len(vocabulary)):
			word = vocabulary[j]
			if(word in sentence):
				row.append(1)
			else:
				row.append(0) 
		matrix.append(row)
	f.close()

	return matrix

######
# Purpose: Output feature vectors to a preprocess file
# Return: return a 2D array including preprocessed data
######
def generate_out_file(out_file, matrix, vocabulary, class_label):
	preprocessed_data = []

	v_temp = vocabulary[:]
	v_temp.append('classlabel')
	
	for index in range(len(matrix)):
		matrix[index].append(class_label[index])
		preprocessed_data.append(matrix[index])

	with open (out_file, 'w') as fo:
		fo.write(','.join(str(i) for i in v_temp))
		fo.write('\n')
		for index in range(len(preprocessed_data)):
			fo.write(','.join(str(i) for i in preprocessed_data[index]))
			fo.write('\n')

	return preprocessed_data

######
# Purpose: Read other files including words we want to filtrate
# Return: A list including words we want to filtrate
######
def read_list(input_file):
	words = []
	f = open(input_file, 'r')
	word_set = f.readlines()
	for word in word_set:
		word = word[:-1]
		words.append(word)
	f.close

	return words