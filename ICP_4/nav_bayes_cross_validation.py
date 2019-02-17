#Import GaussianNB from scikit-Learn libraries
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split

#loading irisdataset
irisdataset = datasets.load_iris()

# x is predictor and y is the target data
x = irisdataset.data
y = irisdataset.target

#training set
x_train , x_test, y_train , y_test = train_test_split(x,y)

# creating Gaussain Naive Bayes object for classification
model = GaussianNB()

#Training the Model
model.fit(x_train, y_train)

#Predictig the Output
y_predict = model.predict(x_test)
print(y_predict)

#Printing the  accuracy
print("Accuracy", metrics.accuracy_score(y_test, y_predict))



