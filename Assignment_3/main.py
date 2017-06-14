import sys
from preprocess import *
from classifier import *

def main():
    train = str(sys.argv[1])
    preprocessed_train_file = str(sys.argv[2])
    test = str(sys.argv[3])
    preprocessed_test_file = str(sys.argv[4])

    # generate bag of words by train data
    vocabulary = sorted(get_vocabulary(train))
    
    # preprocess data to preprocessed file
    preprocessed_train = preprocess(vocabulary, train, preprocessed_train_file)
    preprocessed_test = preprocess(vocabulary, test, preprocessed_test_file)

    # use Naive Bayes
    train_accuracy = naive_bayes(preprocessed_train, preprocessed_train)
    test_accuracy = naive_bayes(preprocessed_train, preprocessed_test)

    fo = open("results.txt", "wb")
    fo.write("Training Data: " + preprocessed_train_file)
    fo.write(" Testing Data: " + preprocessed_train_file + '\n')
    fo.write("Accuracy: " + train_accuracy + '\n')
    fo.write("Training Data: " + preprocessed_train_file)
    fo.write(" Testing Data: " + preprocessed_test_file + '\n')
    fo.write("Accuracy: " + test_accuracy + '\n')
    fo.close()

if __name__ == '__main__':
    main()
