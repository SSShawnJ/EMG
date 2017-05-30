import functions as fun

def load_data(path_to_file,SEGMENT_SIZE=30):
	features=[]
	y=[]

	f=open(path_to_file,"r")
	f.readline()

	ch1=[]
	ch2=[]
	ch3=[]
	ch4=[]
	ch5=[]
	ch6=[]
	ch7=[]
	ch8=[]
	gyroX=[]
	gyroY=[]
	gyroZ=[]
	AcceX=[]
	AcceY=[]
	AcceZ=[]
	element_count=0
	active_num=0

	# last_mav=[]


	for line in f:
		array=line.strip().split(",")
		ch1.append(float(array[1]))
		ch2.append(float(array[2]))
		ch3.append(float(array[3]))
		ch4.append(float(array[4]))
		ch5.append(float(array[5]))
		ch6.append(float(array[6]))
		ch7.append(float(array[7]))
		ch8.append(float(array[8]))
		gyroX.append(float(array[9]))
		gyroY.append(float(array[10]))
		gyroZ.append(float(array[11]))
		AcceX.append(float(array[12]))
		AcceY.append(float(array[13]))
		AcceZ.append(float(array[14]))

		active_num+=int(array[15])
		element_count+=1

		if(element_count==SEGMENT_SIZE):
			active=0
			if(active_num>=(SEGMENT_SIZE/2)):
				active=1

			mav=[fun.mav(ch1),fun.mav(ch2),fun.mav(ch3),fun.mav(ch4),fun.mav(ch5),fun.mav(ch6),fun.mav(ch7),fun.mav(ch8),fun.mav(gyroX),fun.mav(gyroY),fun.mav(gyroZ),fun.mav(AcceX),fun.mav(AcceY),fun.mav(AcceZ)]
			features.append(
						[mav[0],mav[1],mav[2],mav[3],mav[4],mav[5],mav[6],mav[7],mav[8],mav[9],mav[10],mav[11],mav[12],mav[13],
					     fun.ssc(ch1),fun.ssc(ch2),fun.ssc(ch3),fun.ssc(ch4),fun.ssc(ch5),fun.ssc(ch6),fun.ssc(ch7),fun.ssc(ch8),fun.ssc(gyroX),fun.ssc(gyroY),fun.ssc(gyroZ),fun.ssc(AcceX),fun.ssc(AcceY),fun.ssc(AcceZ),
					     fun.wl(ch1),fun.wl(ch2),fun.wl(ch3),fun.wl(ch4),fun.wl(ch5),fun.wl(ch6),fun.wl(ch7),fun.wl(ch8),fun.wl(gyroX),fun.wl(gyroY),fun.wl(gyroZ),fun.wl(AcceX),fun.wl(AcceY),fun.wl(AcceZ),
					     fun.rms(ch1),fun.rms(ch2),fun.rms(ch3),fun.rms(ch4),fun.rms(ch5),fun.rms(ch6),fun.rms(ch7),fun.rms(ch8),fun.rms(gyroX),fun.rms(gyroY),fun.rms(gyroZ),fun.rms(AcceX),fun.rms(AcceY),fun.rms(AcceZ),
					     fun.activity(ch1),fun.activity(ch2),fun.activity(ch3),fun.activity(ch4),fun.activity(ch5),fun.activity(ch6),fun.activity(ch7),fun.activity(ch8),fun.activity(gyroX),fun.activity(gyroY),fun.activity(gyroZ),fun.activity(AcceX),fun.activity(AcceY),fun.activity(AcceZ),
					     fun.mobility(ch1),fun.mobility(ch2),fun.mobility(ch3),fun.mobility(ch4),fun.mobility(ch5),fun.mobility(ch6),fun.mobility(ch7),fun.mobility(ch8),fun.mobility(gyroX),fun.mobility(gyroY),fun.mobility(gyroZ),fun.mobility(AcceX),fun.mobility(AcceY),fun.mobility(AcceZ),
					     fun.complexity(ch1),fun.complexity(ch2),fun.complexity(ch3),fun.complexity(ch4),fun.complexity(ch5),fun.complexity(ch6),fun.complexity(ch7),fun.complexity(ch8),fun.complexity(gyroX),fun.complexity(gyroY),fun.complexity(gyroZ),fun.complexity(AcceX),fun.complexity(AcceY),fun.complexity(AcceZ)
						])
			y.append(active)

			ch1=[]
			ch2=[]
			ch3=[]
			ch4=[]
			ch5=[]
			ch6=[]
			ch7=[]
			ch8=[]
			gyroX=[]
			gyroY=[]
			gyroZ=[]
			AcceX=[]
			AcceY=[]
			AcceZ=[]
			element_count=0
			active_num=0

	f.close()
	return features,y


##### unit test #####
if __name__ == '__main__':
	import numpy as np
	from sklearn.model_selection import train_test_split
	from sklearn import datasets
	from sklearn import svm
	from sklearn.metrics import accuracy_score

	path1="../Data/Negative_dataset_noMoves.csv"
	path2="../Data/Positive_dataset_typing.csv"

	feature1,y1=load_data(path1)
	feature2,y2=load_data(path2)

	feature1+=feature2
	y1+=y2


	X_train, X_test, y_train, y_test = train_test_split(feature1, y1, test_size=0.2, random_state=0)

	clf = svm.SVC(kernel='rbf',C=1000)
	clf.fit(X_train,y_train)

	pred=clf.predict(X_test)

	print(accuracy_score(y_test,pred))

	

	
	
