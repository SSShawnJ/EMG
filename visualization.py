import matplotlib.pyplot as plt
import numpy as np

#subplot

f=open("Data/Negative_dataset_grabbing.csv","r")
f.readline()

#plot the data
#  - x axis is the sequence number the emg event happened
#  - y axis is the value of 8 channels output
#
# Different channel's value will be ploted using different colors
# Here is the channel-color table
#  channel 1: red
#  channel 2: blue 
#  chaneel 3: green
#  channel 4: cyan
#  channel 5: magenta
#  channel 6: yellow
#  channel 7: black
#  channel 8: red
#
# for j in range(1,100):
# 	array=f.readline().split(",")
# 	plt.plot([20*j], [array[1]], 'ro')
# 	plt.plot([20*j], [array[2]], 'bo')
# 	plt.plot([20*j], [array[3]], 'go')
# 	plt.plot([20*j], [array[4]], 'co')
# 	plt.plot([20*j], [array[5]], 'mo')
# 	plt.plot([20*j], [array[6]], 'yo')
# 	plt.plot([20*j], [array[7]], 'ko')
# 	plt.plot([20*j], [array[8]], 'wo')


c0=[];
c1=[];
c2=[];
c3=[];
c4=[];
c5=[];
c6=[];
c7=[];

for line in f:
	array=line.strip().split(",")

	c0.append(array[1])
	c1.append(array[2])
	c2.append(array[3])
	c3.append(array[4])
	c4.append(array[5])
	c5.append(array[6])
	c6.append(array[7])
	c7.append(array[8])
f.close()


t=np.arange(0,len(c0),1)


fig = plt.figure()
fig.suptitle('Negative_dataset_grabbing', fontsize=16)

# plt.axis([0, 1800, 150, -150])
# plt.title("Negative data(simple movements)")
# plt.xlabel("Instance")
# plt.ylabel("Value")

p1=fig.add_subplot(811)
p1.set_title('Channel 1')
p1.set_xticklabels([])
p1.set_ylim([-150,150])
p1.set_ylabel("Value")
p1.plot(t,c0,'r-')

p2=fig.add_subplot(812)
p2.set_title('Channel 2')
p2.set_xticklabels([])
p2.set_ylim([-150,150])
p2.set_ylabel("Value")
p2.plot(t,c1,'b-')

p3=fig.add_subplot(813)
p3.set_xticklabels([])
p3.set_title('Channel 3')
p3.set_ylim([-150,150])
p3.set_ylabel("Value")
p3.plot(t,c2,'g-')

p4=fig.add_subplot(814)
p4.set_xticklabels([])
p4.set_title('Channel 4')
p4.set_ylim([-150,150])
p4.set_ylabel("Value")
p4.plot(t,c3,'c-')

p5=fig.add_subplot(815)
p5.set_xticklabels([])
p5.set_title('Channel 5')
p5.set_ylim([-150,150])
p5.set_ylabel("Value")
p5.plot(t,c4,'m-')

p6=fig.add_subplot(816)
p6.set_xticklabels([])
p6.set_title('Channel 6')
p6.set_ylim([-150,150])
p6.set_ylabel("Value")
p6.plot(t,c5,'y-')

p7=fig.add_subplot(817)
p7.set_xticklabels([])
p7.set_title('Channel 7')
p7.set_ylim([-150,150])
p7.set_ylabel("Value")
p7.plot(t,c6,'k-')

p8=fig.add_subplot(818)
p8.set_title('Channel 8')
p8.set_ylim([-150,150])
p8.set_ylabel("Value")
p8.set_xlabel("Instance")
p8.plot(t,c7,'r-')

fig=plt.gcf()
default_size=fig.get_size_inches()
fig.set_size_inches((default_size[0], default_size[1]*3))

# fig.subplots_adjust(hspace=0.8,wspace=1)

fig.savefig("Plots/negative_grabbing.png")
plt.show()
plt.close()

