import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris() # load the dataset that is iris
test_idx = [0, 50, 100] # the indexes we save for testing

# training data
train_target = np.delete(iris.target, test_idx) # remove the indexes for the testing labels and return the whole list
train_data = np.delete(iris.data, test_idx, axis=0) # do the same but for the data instead.

# testing data
test_target = iris.target[test_idx] # take the labels from the indexes above
test_data = iris.data[test_idx] # take the data from the indexes above

clf = tree.DecisionTreeClassifier() # create a tree with rules
clf = clf.fit(train_data, train_target) # train our program to see the difference between the flowers

print("Testing: ")
desired_result = test_target # print the target labels for the test 
prediction = clf.predict(test_data)
if prediction.all() == desired_result.all():
    print("test successful")
else:
    print("goddammit something wrong")

# im supposed to code something to visualize a tree but i dont feel like installing dependencies and such