import matplotlib.pyplot as plt

f=open("Data/Negative_dataset_simpleMoves.csv","r")
i=1

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
#  channel 8: white
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


for line in f:
	array=line.strip().split(",")
	plt.plot([i], [array[1]], 'ro')
	plt.plot([i], [array[2]], 'bo')
	plt.plot([i], [array[3]], 'go')
	plt.plot([i], [array[4]], 'co')
	plt.plot([i], [array[5]], 'mo')
	plt.plot([i], [array[6]], 'yo')
	plt.plot([i], [array[7]], 'ko')
	plt.plot([i], [array[8]], 'wo')
	i+=1
f.close()

plt.axis([0, 1800, 150, -150])
plt.title("Negative data(simple movements)")
plt.xlabel("Instance")
plt.ylabel("Value")
plt.savefig("Plots/negative_simple_moves.png")
plt.close()

