import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC  #importing svm classifier from sklearn
from sklearn.tree import DecisionTreeClassifier   #importing DecisionTreeClassifier from sklearn
from sklearn.naive_bayes import BernoulliNB    #importing BernoulliNB from sklearn
from sklearn.naive_bayes import GaussianNB    #importing GaussianNB from sklearn

classifier = SVC()
classifier2 = DecisionTreeClassifier()
classifier3 = BernoulliNB()
classifier4 = GaussianNB()

df1 = pd.read_csv('training_data.txt')
df1 = df1.sample(n=400)

print(df1.head())

x = zip(df1['name1'].values.tolist(), df1['name2'].values.tolist(), df1['address1'].values.tolist(), df1['address2'].values.tolist(), df1['phone1'].values.tolist(), df1['phone2'].values.tolist(), df1['bin'].values.tolist())
list_x = []
for i in x:
    list_x.append(list(i))
train_x = [j[:6] for j in list_x[:360]]   #training data for x
train_y = [int(k[6]) for k in list_x[:360]]   #training y

print("train_x : ", train_x)
print("train_y : ", train_y)

classifier.fit(train_x, train_y)
classifier2.fit(train_x, train_y)
classifier3.fit(train_x, train_y)
classifier4.fit(train_x, train_y)

test_x = [j[:6] for j in list_x[360:]]  #test data for x
test_y = [int(k[6]) for k in list_x[360:]]  #test data for y
print("test_x : ", test_x)
print("test_y      : ", test_y)

prediction = classifier.predict(test_x)  #predictions using various classifiers
prediction2 = classifier2.predict(test_x)
prediction3 = classifier3.predict(test_x)
prediction4 = classifier4.predict(test_x)


print("SVC         :", prediction)
print("DecisionTre :", prediction2)
print("BernoulliNB :", prediction3)
print("GaussianNB  :", prediction4)

score1 = accuracy_score(test_y, prediction)   #accuracy of test case
score2 = accuracy_score(test_y, prediction2)
score3 = accuracy_score(test_y, prediction3)
score4 = accuracy_score(test_y, prediction4)
print(score1, score2, score3, score4)

