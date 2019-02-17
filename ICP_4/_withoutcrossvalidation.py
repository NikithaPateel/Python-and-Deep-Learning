from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn.model_selection import train_test_split

irisdataset = datasets.load_iris()
x = irisdataset.data
y = irisdataset.target

model = GaussianNB()
model.fit(x,y)
predicted = model.predict([[2, 3, 4, 5],[5, 3, 1, 2]])
list = predicted
print(predicted)
for i in list:
    print(irisdataset.target_names[i])
print(model.score(x,y,sample_weight = None))

