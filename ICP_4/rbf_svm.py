#import SVC form scikit learn
from sklearn.svm import SVC
from sklearn import datasets
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

#loading the data
irisdataset = datasets.load_iris()

x = irisdataset.data
y = irisdataset.target

#trining dataset
x_train , x_test, y_train , y_test = train_test_split(x,y, test_size= 0.2)

#creating SVC RBF Kernal Object for classification
svclassifier = SVC(kernel='rbf', gamma= "auto")

#trining the data
svclassifier.fit(x_train, y_train)

#pridicting then output
y_pred = svclassifier.predict(x_test)
print(y_pred)

#classification report to display the accuracy
print(classification_report(y_test, y_pred))