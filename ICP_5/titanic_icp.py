import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

train_data = pd.read_csv('train_preprocessed.csv')
test_data = pd.read_csv('test_preprocessed.csv')
x_train = train_data.drop("Survived",axis=1)
y_train = train_data["Survived"]

x_test = test_data.drop("PassengerId",axis=1).copy()
#print(train_df[train_df.isnull().any(axis=1)])

##SVM
svc = SVC(kernel= "rbf" , gamma = 'auto')
svc.fit(x_train, y_train)
Y_pred = svc.predict(x_test)
acc_svc = round(svc.score(x_test, Y_pred) * 100, 2)
print("svm accuracy is:", acc_svc)

#train_df.info()
print(train_data['Survived'].corr(train_data['Sex']))
print(train_data[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))
