#import SVC From Scikit- Learn library
from sklearn.svm import SVC
from sklearn import datasets
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

#Loading iris data
irisdataset = datasets.load_iris()

x = irisdataset.data
y = irisdataset.target

#training set
x_train , x_test, y_train , y_test = train_test_split(x,y, test_size= 0.2)

#using linear SVC Classification Object
svclassifier = SVC(kernel='linear')

#training the data
svclassifier.fit(x_train, y_train)

#pridicting the output
y_pred = svclassifier.predict(x_test)
print(y_pred)
list = y_pred
for i in list:
    print(irisdataset.target_names[i])
#classification report to display the accuracy
print(classification_report(y_test, y_pred))