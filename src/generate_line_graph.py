import subprocess
import matplotlib.pyplot as plt
from datetime import datetime
import glob
import sys



site_comp = False
# decide whether or not to show just one website
if len(sys.argv) == 2:
	site_comp = sys.argv[1]


# plt.style.use('ggplot')

# files_to_check = ["data_for_340.txt", "data_for_343.txt", "data_for_344.txt", "data_for_345.txt", "data_for_346.txt", "data_for_347.txt", "data_for_348.txt", "data_for_349.txt", "data_for_350.txt", "data_for_351.txt", "data_for_352.txt", "data_for_353.txt", "data_for_355.txt", "data_for_357.txt", "data_for_358.txt"]

files_to_check = glob.glob("*data*")
files_to_check.sort()
master_data_set = []
master_rotated = []
data = []
site_names = []
files_to_delete = []

command_to_move = "mv {0} bad_files/{0}"

xdata = []
index_list = []

switch = 0
for file in files_to_check:
	xdata.append(int(file.split('_')[-1].split('.')[0]))
	switch = 0
	data = []
	site_names = []
	with open(file, "r") as f:
		ind = f.readlines()
	if len(ind) < 2:
		files_to_delete.append(file)
		del xdata[-1]
		continue
		# print ind
	# print ind[0:10]
	idx = -1
	idx_added = False
	for name in ind:
		if switch == 0:
			idx+=1
			# print name
			if name[0] != "=":
				site_names.append(name)
				print name
				if name.strip() == str(site_comp) and idx_added == False:
					print name
					index_list.append(idx)
					idx_added = True
				continue
			switch = 1
			continue
		if float(name) > 20:
			data.append(20)
		else:
			data.append(float(name))
	if idx_added == False:
		index_list.append(False)
	# print site_names
	# print data
	# print len(site_names)
	# print len(data)
	master_data_set.append(data)

# print '\n\n\n\n\n\n\n\n\n\n'
# print master_data_set
# print files_to_delete
# print len(files_to_delete)

print index_list

y = [k for k in range(0, len(site_names))]
x = [k for k in range(0, len(master_data_set))]

# print files_to_check

for i in range(0, len(master_data_set[0])):
	tmplist = []
	for l in master_data_set:
		try:
			tmplist.append(l[i])
		except IndexError:
			tmplist.append(0)
		master_rotated.append(tmplist)

# print master_rotated

plt.figure(1)
# for dset in master_rotated:
# 	plt.plot(xdata, dset)

avgs = []
for dset in master_data_set:
	avg = sum(dset)/(len(dset)+1)
	avgs.append(avg)

site_comp_list = []
for i, dset in enumerate(master_data_set):
	site_comp_list.append(master_data_set[i])

b = avgs[0]
diff = 0
for i in avgs:
	diff += (i-b)/float(len(avgs))
avg_end_point = b+diff


print xdata
plt.plot(xdata, avgs, linewidth=1.0, label='Data')
plt.title("Change in average website response times of 200 websites since just before Net Neutrality was voted against")
plt.plot([xdata[0], xdata[-1]], [avgs[0], avg_end_point], linewidth=2.0, label='fit')
if len(sys.argv) == 2:
	plt.plot(xdata, site_comp_list, label=sys.argv[1])
	plt.title("Change in average website response times of 200 websites since just before Net Neutrality was voted against [site: {0}]".format(sys.argv[1]))

plt.xlabel("Days since start of the data collection (Friday, Dec 8th)")
plt.ylabel("Response time, curl, seconds")
plt.legend()
plt.show()







	
