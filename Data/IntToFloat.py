f=open("Negative_dataset_grabbing.csv","r")
fw=open("Negative_dataset_grabbingF.csv","w")


fw.write(f.readline())

for line in f:
	array=line.strip().split(",")
	s=array[0]+','+str(float(array[1]))+','+str(float(array[2]))+','+str(float(array[3]))+','+str(float(array[4]))+','+str(float(array[5]))+','+str(float(array[6]))+','+str(float(array[7]))+','+str(float(array[8]))+','+array[9]
	fw.write(s+"\n")


f.close()
fw.close()
print "Complete!"