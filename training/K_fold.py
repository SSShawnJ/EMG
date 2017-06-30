import sys
sys.path.append("../Functions")
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
	
	# path to files
	path_data="../Extracted_features/ExtractedData_S_"+str(SEGMENT_SIZE)+"_T_"+str(thresh)+".csv"

	# load and shuffle data
	feature,y=load_data(path_data)
	feature = np.array(feature)
	y= np.array(y)
	feature,y=shuffle(feature,y)
	

	# start k-fold
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
	##unit teset##
	score=K_fold(K=10,C=0.1,SEGMENT_SIZE=20,thresh=5)
	print score


	##train multipule k-fold with different threshold and segment size
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


###############################
# plot results in a single graph
################################

	# fig = plt.figure()                                                               
	# p = fig.add_subplot(1,1,1)  
	# p.plot(t1,t2,'bo') 
	# p.plot(t1,t2,'g')
	# p.grid(which='both')
	# plt.xticks(xrange(len(t1)),xlabel)  
	# default_size=fig.get_size_inches()
	# fig.set_size_inches((default_size[0]*3, default_size[1]*3))
	# p.set_xlabel("test")
	# fig.savefig("Plots/k-fold_Results.png")
	# plt.show()
	# plt.close()



###############################
# plot results in a multipule subgraph
################################
	# t1=np.array(range(0,36))
	# t2=np.array(range(0,36))

	# fig = plt.figure()
	# fig.suptitle('K-fold results', fontsize=16)

	# p1=fig.add_subplot(611)
	# p1.set_title('Thresh='+str(thresh[0]))
	# p1.set_xticklabels([15,20,25,30,35,40])
	# p1.set_xlabel("Segment Size")
	# p1.set_ylabel("Accuracy Score")
	# p1.plot(t1[0:6],t2[0:6],'bo') 
	# p1.plot(t1[0:6],t2[0:6],'g')

	# p2=fig.add_subplot(612)
	# p2.set_title('Thresh='+str(thresh[1]))
	# p2.set_xticklabels([15,20,25,30,35,40])
	# p2.set_xlabel("Segment Size")
	# p2.set_ylabel("Accuracy Score")
	# p2.plot(t1[6:12],t2[6:12],'bo') 
	# p2.plot(t1[6:12],t2[6:12],'g')

	# p3=fig.add_subplot(613)
	# p3.set_title('Thresh='+str(thresh[2]))
	# p3.set_xticklabels([15,20,25,30,35,40])
	# p3.set_xlabel("Segment Size")
	# p3.set_ylabel("Accuracy Score")
	# p3.plot(t1[12:18],t2[12:18],'bo') 
	# p3.plot(t1[12:18],t2[12:18],'g')

	# p4=fig.add_subplot(614)
	# p4.set_title('Thresh='+str(thresh[3]))
	# p4.set_xticklabels([15,20,25,30,35,40])
	# p4.set_xlabel("Segment Size")
	# p4.set_ylabel("Accuracy Score")
	# p4.plot(t1[18:24],t2[18:24],'bo') 
	# p4.plot(t1[18:24],t2[18:24],'g')

	# p5=fig.add_subplot(615)
	# p5.set_title('Thresh='+str(thresh[4]))
	# p5.set_xticklabels([15,20,25,30,35,40])
	# p5.set_xlabel("Segment Size")
	# p5.set_ylabel("Accuracy Score")
	# p5.plot(t1[24:30],t2[24:30],'bo') 
	# p5.plot(t1[24:30],t2[24:30],'g')

	# p6=fig.add_subplot(616)
	# p6.set_title('Thresh='+str(thresh[5]))
	# p6.set_xticklabels([15,20,25,30,35,40])
	# p6.set_xlabel("Segment Size")
	# p6.set_ylabel("Accuracy Score")
	# p6.plot(t1[30:36],t2[30:36],'bo') 
	# p6.plot(t1[30:36],t2[30:36],'g')


	# fig=plt.gcf()
	# default_size=fig.get_size_inches()
	# fig.set_size_inches((default_size[0]*3, default_size[1]*3))

	# fig.subplots_adjust(hspace=0.8,wspace=1)

	# fig.savefig("Plots/K-fold_Results_AllinOne.png")
	# plt.show()
	# plt.close()







