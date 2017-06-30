import functions as fun

def load_data(path_to_data):

	features=[]
	y=[]

	f=open(path_to_data,"r")
	f.readline()
	for line in f:
		array=line.strip().split(",")
		for i in range(len(array)-1):
			array[i]=float(array[i])
		features.append(array[:-1])
		y.append(float(array[-1]))
	f.close()

	return features,y


##### unit test #####
if __name__ == '__main__':
	import sys
	sys.path.append('../Extracted_features/')
	import numpy as np
	from sklearn.model_selection import train_test_split
	from sklearn import datasets
	from sklearn import svm
	from sklearn.metrics import accuracy_score
	from sklearn.utils import shuffle

	

	SEGMENT_SIZE=20
	thresh=5

	print "SEGMENT_SIZE:",SEGMENT_SIZE
	print "thresh:",thresh

	path1="../Extracted_features/ExtractedData_S_20_T_5.csv"


	feature,y=load_data(path1)
	

	feature = np.array(feature)
	y= np.array(y)

	feature,y=shuffle(feature,y)

	# np.savetxt("Features.csv", feature, delimiter=",")
	# np.savetxt("Labels.csv", y, delimiter=",")


	X_train, X_test, y_train, y_test = train_test_split(feature, y, test_size=0.2, random_state=0)

	clf = svm.SVC(kernel='rbf',C=1000)
	clf.fit(X_train,y_train)

	pred=clf.predict(X_test)

	print(accuracy_score(y_test,pred))

	

	
	
