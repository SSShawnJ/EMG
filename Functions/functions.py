import math
import numpy as np

##Mean Absolute Value (MAV): 
##Estimate of the MAV of the signal Si, in segment i which is N samples in length
#S - Signal S
#i - ith segment in S(starting from segment 0 )
#T - Total number of segments over S (T>= 1)
def mav(S):
	# l=len(S)
	# n= int(math.ceil(l*1.0/T))
	# lowerbound= i*n
	# upperbound= (i+1)*n
	# if(upperbound>l):
	# 	upperbound=l

	# N=upperbound-lowerbound
	# mav=0
	# for i in range(lowerbound,upperbound):
	# 	mav+=abs(S[i])*1.0/N

	N=len(S)
	mav=0
	for i in range(0,N):
		mav+=abs(S[i])*1.0/N

	return mav


##Difference MAV: 
##Represents the difference in mean absolute value between the segment 
##of interest and the subsequent segment
#S - Signal S
#i - ith segment in S(starting from segment 0 )
#T - Total number of segments over S (T>0)
def diff_mav(S1, S2):
	# if(i<T-1):
	# 	return mav(S, i+1, T)-mav(S, i, T)
	# else:
	# 	raise Exception('segment index out of bound')
	return mav(S2)-mav(S1)



##Slope Sign Changes (SSC):
##Number of times the slope of the waveform changes signs (from positive to negative, or vice versa). 
##A suitable threshold must be chosen to reduce noise induced slope sign changes
#S      - Signal S
#thresh - predefined threshold value
def ssc(S, thresh=1):
	l= len(S)
	if(l<3):
		return 0
	
	NofC=0
	indexLow=0
	indexMid=1
	indexHigh=2

	while(indexHigh<l):
		v1=S[indexMid]-S[indexLow]
		v2=S[indexMid]-S[indexHigh]

		c1=(v1>0 and v2>0)
		c2=(v1<0 and v2<0)
		c3=(abs(v1)>=thresh or abs(v2)>=thresh)

		if((c1 or c2) and c3):
			NofC+=1

		indexLow+=1
		indexMid+=1
		indexHigh+=1


	return NofC




def wl(V):
	N=len(V)
	if(N<=1):
		raise Exception('Error! Only one sample in the data array.')
	wl=0;
	for i in range(1,N):
		wl+=abs(V[i-1]-V[i])

	return wl

def rms(S):
	N=len(S)
	if(N==0):
		raise Exception('Error! Data array is empty')

	rms=0
	for i in range(0,N):
		rms+=S[i]**2*1.0/N
	rms=math.sqrt(rms)

	return rms


def activity(S):
	return np.var(S)

def mobility(S):
	return 1

def complexity(S):
	return 1



####Unit Test####
if __name__ == '__main__':
	S=[2,4,3,4]
	print mav(S)

	print wl(S)

	print rms(S)

	pvvariance = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]


	print "population variance: ",np.var(pvvariance)




