import sys
sys.path.append("Functions")
import functions as fun 
from loadData import load_data
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.metrics import accuracy_score


def train(X_train,y_train,X_test,y_test,c=1,k='linear'):
	clf = svm.LinearSVC(C=c)
	clf.fit(X_train,y_train)
	pred=clf.predict(X_test)
	return accuracy_score(y_test,pred)








if __name__ == '__main__':
	path1="Data/Negative_dataset_noMoves.csv"
	path2="Data/Positive_dataset_typing.csv"

	feature1,y1=load_data(path1)
	feature2,y2=load_data(path2)
	feature1+=feature2
	y1+=y2


	X_train, X_test, y_train, y_test = train_test_split(feature1, y1, test_size=0.3)

	clf = svm.LinearSVC(C=100)
	clf.fit(X_train,y_train)

	pred=clf.predict(X_test)

	print(accuracy_score(y_test,pred))

	

	
	
