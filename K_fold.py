import sys
sys.path.append("Functions")
import functions as fun 
from loadData import load_data
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.utils import shuffle
import svm
import matplotlib.pyplot as plt

def K_fold(K=10,C=0.1,SEGMENT_SIZE=30,thresh=1):
	from numpy import genfromtxt
	path1="Data/Positive_dataset_typing.csv"
	path2="Data/Negative_dataset_noMoves.csv"
	path3="Data/Negative_dataset_drinking.csv"
	path4="Data/Negative_dataset_grabbing.csv"
	path5="Data/Negative_dataset_eating.csv"


	feature,y=load_data(path1,SEGMENT_SIZE=SEGMENT_SIZE,thresh=thresh)
	feature2,y2=load_data(path2,SEGMENT_SIZE=SEGMENT_SIZE,thresh=thresh)
	feature3,y3=load_data(path3,SEGMENT_SIZE=SEGMENT_SIZE,thresh=thresh)
	feature4,y4=load_data(path4,SEGMENT_SIZE=SEGMENT_SIZE,thresh=thresh)
	feature5,y5=load_data(path5,SEGMENT_SIZE=SEGMENT_SIZE,thresh=thresh)


	feature+=(feature2+feature3+feature4+feature5)
	y+=(y2+y3+y4+y5)
	# path="Extracted_features/S_"+str(SEGMENT_SIZE)+"_T_"+str(thresh)+".csv"


	feature = np.array(feature)
	y= np.array(y)

	filename="S_"+str(SEGMENT_SIZE)+"_T_"+str(thresh)
	np.savetxt("Features_"+filename+".csv", feature, delimiter=",")
	np.savetxt("Labels_"+filename+".csv", y, delimiter=",")

	feature,y=shuffle(feature,y)
	
	# feature = genfromtxt('Features.csv', delimiter=',')
	# y= genfromtxt('Labels.csv', delimiter=',')


	kf = KFold(n_splits=K)
	score=0.0

	iteration=1
	for train, test in kf.split(feature):

		print "iteration:", iteration
		X_train, X_test, y_train, y_test = feature[train], feature[test], y[train], y[test]

		score+= (svm.train(X_train, y_train,  X_test, y_test,c=C))*1.0/K

		iteration+=1

	return score



if __name__ == '__main__':
	score=K_fold(K=10,C=0.1,SEGMENT_SIZE=30,thresh=15)
	print score

	# t1 = []
	# t2 = []
	# xlabel=[]

	# thresh=[1,5,10,20,30,35]
	# SEGMENT_SIZE=[15,20,25,30,35,40]


	# index=1
	# for thr in thresh:
	# 	for seg in SEGMENT_SIZE:

	# 		l='T='+str(thr)+'\nS='+str(seg)
	# 		print 'T='+str(thr)+', S='+str(seg)
	# 		t1.append(index)
	# 		t2.append(K_fold(K=10,C=0.1,SEGMENT_SIZE=seg,thresh=thr))
	# 		xlabel.append(l)
	# 		index+=1



	# t1=np.array(t1)
	# t2=np.array(t2)

	# fig = plt.figure()                                                               
	# p = fig.add_subplot(1,1,1)  
	# p.plot(t1,t2,'bo') 
	# p.plot(t1,t2,'g')
	# p.grid(which='both')
	# plt.xticks(xrange(len(t1)),xlabel)  
	# default_size=fig.get_size_inches()
	# fig.set_size_inches((default_size[0]*3, default_size[1]*3))
	# p.set_xlabel("test")
	                                                                                                                           



	# fig.savefig("plot.png")
	# plt.show()
	# plt.close()







