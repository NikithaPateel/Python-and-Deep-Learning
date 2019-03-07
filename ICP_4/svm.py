#Import GaussianNB from scikit-Learn libraries
from sklearn.svm import SVC
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import KFold,cross_val_predict
import numpy as np
#loading irisdataset
irisdataset = datasets.load_iris()
#splitting for cross validation
kf = KFold(n_splits=10, random_state= 42 , shuffle= False)
# x is predictor and y is the target data
x = irisdataset.data
y = irisdataset.target
scores = []
for train_index, test_index in kf.split(x):
    #training set
    x_train, x_test, y_train, y_test = x[train_index], x[test_index], y[train_index], y[test_index]
# creating Gaussain Naive Bayes object for classification
    svclassifier = SVC(kernel='linear')
#Training the Model
    svclassifier.fit(x_train, y_train)
#Predictig the Output
    y_predict = svclassifier.predict(x_test)
    # scores.append(y_predict)
    scores.append(metrics.accuracy_score(y_test , y_predict))
    print(y_predict)
#Printing the  accuracy
for i in range(len(scores)):
    print(scores)
print(np.mean(scores))


