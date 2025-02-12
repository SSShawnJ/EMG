import functions as fun

def extract_feature(path_to_file,SEGMENT_SIZE=30,thresh=1):
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
	index=0 #element count in feature array


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
					     fun.ssc(ch1,thresh=thresh),fun.ssc(ch2,thresh=thresh),fun.ssc(ch3,thresh=thresh),fun.ssc(ch4,thresh=thresh),fun.ssc(ch5,thresh=thresh),fun.ssc(ch6,thresh=thresh),fun.ssc(ch7,thresh=thresh),fun.ssc(ch8,thresh=thresh),fun.ssc(gyroX,thresh=thresh),fun.ssc(gyroY,thresh=thresh),fun.ssc(gyroZ,thresh=thresh),fun.ssc(AcceX,thresh=thresh),fun.ssc(AcceY,thresh=thresh),fun.ssc(AcceZ,thresh=thresh),
					     fun.wl(ch1),fun.wl(ch2),fun.wl(ch3),fun.wl(ch4),fun.wl(ch5),fun.wl(ch6),fun.wl(ch7),fun.wl(ch8),fun.wl(gyroX),fun.wl(gyroY),fun.wl(gyroZ),fun.wl(AcceX),fun.wl(AcceY),fun.wl(AcceZ),
					     fun.rms(ch1),fun.rms(ch2),fun.rms(ch3),fun.rms(ch4),fun.rms(ch5),fun.rms(ch6),fun.rms(ch7),fun.rms(ch8),fun.rms(gyroX),fun.rms(gyroY),fun.rms(gyroZ),fun.rms(AcceX),fun.rms(AcceY),fun.rms(AcceZ),
						])

			y+=[active]  

			# fun.activity(ch1),fun.activity(ch2),fun.activity(ch3),fun.activity(ch4),fun.activity(ch5),fun.activity(ch6),fun.activity(ch7),fun.activity(ch8),fun.activity(gyroX),fun.activity(gyroY),fun.activity(gyroZ),fun.activity(AcceX),fun.activity(AcceY),fun.activity(AcceZ),
			# fun.mobility(ch1),fun.mobility(ch2),fun.mobility(ch3),fun.mobility(ch4),fun.mobility(ch5),fun.mobility(ch6),fun.mobility(ch7),fun.mobility(ch8),fun.mobility(gyroX),fun.mobility(gyroY),fun.mobility(gyroZ),fun.mobility(AcceX),fun.mobility(AcceY),fun.mobility(AcceZ),
			# fun.complexity(ch1),fun.complexity(ch2),fun.complexity(ch3),fun.complexity(ch4),fun.complexity(ch5),fun.complexity(ch6),fun.complexity(ch7),fun.complexity(ch8),fun.complexity(gyroX),fun.complexity(gyroY),fun.complexity(gyroZ),fun.complexity(AcceX),fun.complexity(AcceY),fun.complexity(AcceZ)

			#add diff_max feature
			if (index>=1):
				diff_max=[mav[0]-features[index-1][0],mav[1]-features[index-1][1],mav[2]-features[index-1][2],mav[3]-features[index-1][3],mav[4]-features[index-1][4],mav[5]-features[index-1][5],mav[6]-features[index-1][6],mav[7]-features[index-1][7],mav[8]-features[index-1][8],mav[9]-features[index-1][9],mav[10]-features[index-1][10],mav[11]-features[index-1][11],mav[12]-features[index-1][12],mav[13]-features[index-1][13]]
				features[index-1]=features[index-1]+diff_max


			index+=1


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

	F=features[index-2]
	diff_max=[F[56],F[57],F[58],F[59],F[60],F[61],F[62],F[63],F[64],F[65],F[66],F[67],F[68],F[69]]
	features[index-1]=features[index-1]+diff_max
	f.close()

	return features, y
	


##### unit test #####
if __name__ == '__main__':
	import sys
	sys.path.append('../Data/')
	import numpy as np
	from sklearn.model_selection import train_test_split
	from sklearn import datasets
	from sklearn import svm
	from sklearn.metrics import accuracy_score
	from sklearn.utils import shuffle

	path1="../Data/Positive_dataset_typing.csv"
	path2="../Data/Negative_dataset_noMoves.csv"
	path3="../Data/Negative_dataset_drinking.csv"
	path4="../Data/Negative_dataset_grabbing.csv"
	path5="../Data/Negative_dataset_eating.csv"



	thresh=[1,5,10,20,30,35]
	SEGMENT_SIZE=[15,20,25,30,35,40]

	for thr in thresh:
		for seg in SEGMENT_SIZE:
			path_to_save="../Extracted_features/ExtractedData_S_"+str(seg)+"_T_"+str(thr)+".csv"

			feature,y=extract_feature(path1,SEGMENT_SIZE=seg,thresh=thr)
			feature2,y1=extract_feature(path2,SEGMENT_SIZE=seg,thresh=thr)
			feature3,y2=extract_feature(path3,SEGMENT_SIZE=seg,thresh=thr)
			feature4,y3=extract_feature(path4,SEGMENT_SIZE=seg,thresh=thr)
			feature5,y4=extract_feature(path5,SEGMENT_SIZE=seg,thresh=thr)

			feature+=(feature2+feature3+feature4+feature5)
			y+=(y1+y2+y3+y4)
			feature = np.array(feature)
			y=np.array(y)

			data=np.c_[feature,y]
			
			np.savetxt(path_to_save, data, delimiter=",")

	print "Done!"




