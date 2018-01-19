import subprocess
import matplotlib.pyplot as plt
from datetime import datetime
import glob

# files_to_check = ["data_for_340.txt", "data_for_343.txt", "data_for_344.txt", "data_for_345.txt", "data_for_346.txt", "data_for_347.txt", "data_for_348.txt", "data_for_349.txt", "data_for_350.txt", "data_for_351.txt", "data_for_352.txt", "data_for_353.txt", "data_for_355.txt", "data_for_357.txt", "data_for_358.txt"]

files_to_check = glob.glob("*data*")
master_data_set = []
master_rotated = []
data = []
site_names = []


switch = 0
for file in files_to_check:
	switch = 0
	data = []
	site_names = []
	with open(file, "r") as f:
		ind = f.readlines()
	print ind[0:10]
	for name in ind:
		if switch == 0:
			print name
			if name[0] != "=":
				site_names.append(name)
				continue
			switch = 1
			continue
		data.append(float(name))

	print site_names
	print data
	print len(site_names)
	print len(data)
	master_data_set.append(data)

print '\n\n\n\n\n\n\n\n\n\n'
print master_data_set

y = [k for k in range(0, len(site_names))]
x = [k for k in range(0, len(master_data_set))]

print files_to_check

for i in range(0, len(master_data_set[0])):
	tmplist = []
	for l in master_data_set:
		try:
			tmplist.append(l[i])
		except IndexError:
			tmplist.append(0)
		master_rotated.append(tmplist)

print master_rotated

plt.figure(1)
for dset in master_rotated:
	plt.plot(x, dset)

avgs = []
for dset in master_data_set:
	avg = sum(dset)/len(dset)
	avgs.append(avg)

plt.plot(x, avgs, linewidth=7.0)

plt.xlabel("Days since start of the data collection (Friday, Dec 8th)")
plt.ylabel("Response time, curl, seconds")
plt.show()







	
