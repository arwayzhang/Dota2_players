import csv
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.grid_search import GridSearchCV
from sklearn.feature_selection import RFE
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn import metrics
from sklearn import svm
from sklearn import neighbors
from sklearn import naive_bayes
from sklearn import tree
from time import time, strftime, localtime

######data importing#################################################################################################33

matchFile = open('normalized_data_sep.csv', 'r')
matchInfo = csv.reader(matchFile)

match=[]
match=list()

for info in matchInfo:
	matchline=[]
	for a in info:
		matchline.append(float(a))
	match.append(matchline)

match=np.mat(match)
#print(match)

labelFile = open('label.csv', 'r')
labelInfo = csv.reader(labelFile)

label=[]
label=list()

for info in labelInfo:
	labelline=[]
	for a in info:
		labelline.append(float(a))
	label.append(labelline)

label=np.mat(label)

########classifiers##################################################################################################

X_train, X_test, Y_train, Y_test = train_test_split(match, label, test_size=0.1,random_state=5)

Y_train=np.array(Y_train.ravel().T)

logreg = LogisticRegression()
_ = logreg.fit(X_train, Y_train)
print('Intercept:', logreg.intercept_)
print('Coefficients:\n', logreg.coef_)


print('\nPredicted type of first five organisms from test split:', logreg.predict(X_test)[:5])
print('Actual type of first five organisms from test split:', Y_test[:5])


print(classification_report(Y_test, logreg.predict(X_test)))


clf = neighbors.KNeighborsClassifier(n_neighbors=5)
clf.fit(X_train, Y_train)
y_score=clf.predict(X_test)


GB = naive_bayes.GaussianNB()
GB.fit(X_train, Y_train)
y_score_GB=GB.predict(X_test)

######ploting confusion matrix#################################################################################3

cm = confusion_matrix(Y_test, y_score_GB)

plt.matshow(cm)
plt.colorbar()


plt.ylabel('True label')        
plt.xlabel('Predicted label')
plt.title('Gaussian Naive Bayes')
plt.show()


cm = confusion_matrix(Y_test, y_score)

plt.matshow(cm)
plt.colorbar()


plt.ylabel('True label')        
plt.xlabel('Predicted label')
plt.title('K-Nearest Neighbors')
plt.show()


cm = confusion_matrix(Y_test, logreg.predict(X_test))

plt.matshow(cm)
plt.colorbar()


plt.ylabel('True label')        
plt.xlabel('Predicted label')
plt.title('Logistic Regression')
plt.show()






#####################################################################################################################3#

m,n=np.shape(Y_test)
print(m)
print(n)

actual_y = Y_test
predicted_prob = logreg.predict_proba(X_test)[:,1]


print(predicted_prob)
predicted_prob2 = clf.predict_proba(X_test)[:,1]

predicted_prob3 = GB.predict_proba(X_test)[:,1]




fpr, tpr, thresholds = metrics.roc_curve(actual_y, predicted_prob, pos_label=1)
fpr2, tpr2, thresholds2 = metrics.roc_curve(actual_y, predicted_prob2, pos_label=1)
fpr3, tpr3, thresholds3 = metrics.roc_curve(actual_y, predicted_prob3, pos_label=1)




print(' fpr={},\n tpr={},\n thresholds={}'.format(fpr, tpr, thresholds))
print(' fpr2={},\n tpr2={},\n thresholds2={}'.format(fpr2, tpr2, thresholds2))
print(' fpr3={},\n tpr3={},\n thresholds3={}'.format(fpr3, tpr3, thresholds3))




auc=metrics.auc(fpr, tpr)
auc2=metrics.auc(fpr2, tpr2)
auc3=metrics.auc(fpr3, tpr3)


plt.plot(fpr, tpr,color='darkorange',label='Logistic Regression (area = %0.2f)' % auc)
plt.plot(fpr2, tpr2,color='blue',label='K-Nearest Neighbors (area = %0.2f)' % auc2)
plt.plot(fpr3, tpr3,color='black',label='Gaussian Naive Bayes (area = %0.2f)' % auc3)




plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()


#######grid search###################################################################################################################3

# Perform grid search
param_grid = [
 {'C': [0.1, 1, 10, 100, 1000, 1e4, 1e5, 1e6, 1e7], 'penalty': ['l1', 'l2'],'class_weight': [None, 'balanced']}
]
logreg = GridSearchCV(LogisticRegression(), param_grid)
 #Y_train=Y_train.T
Y_train_list=[]
m,n=np.shape(Y_train)
for i in range(m):
        Y_train_list.append(Y_train[i,0])

 #print(Y_train_list)
 # Y_train=np.array(Y_train.ravel().T)
 # print(np.shape(Y_train))


logreg.fit(X_train, Y_train_list)

 # Print grid search results
print('Grid search mean and stdev:\n')
for params, mean_score, scores in logreg.grid_scores_:
        print("{:0.3f} (+/-{:0.03f}) for {}".format(mean_score, scores.std() * 2, params))

 # Print best params
print('\nBest parameters:', logreg.best_params_)

 #print('\nClassification report ({}):\n'.format(key))
print(classification_report(Y_test, logreg.predict(X_test)))

########feature ranking##################################################################################################3


# feature extraction
test = SelectKBest(score_func=chi2, k=5)
fit = test.fit(X_train, Y_train)
# summarize scores
np.set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(X_train)
# summarize selected features
print(features[0:10,:])

# clf = svm.SVC()
# clf.fit(X_train, Y_train)
# y_score = clf.predict(X_test)
rankinglables=['GPM','XPM','KDA','P/F','C/P']

ranking=[1,2,3,4,5]

plt.scatter(ranking,fit.scores_)
plt.plot(ranking,fit.scores_,color='red',label='scores')

plt.xticks(ranking, rankinglables, rotation=0)
plt.xlabel('Features')
plt.ylabel('Scores')
plt.title('Scores of Features')
plt.legend(loc="upper left")
plt.show()




