import subprocess
import matplotlib.pyplot as plt
from datetime import datetime

# website_list = ["google.com", "bbc.com", "cnn.com", "verizon.com", "comcast.com", "hulu.com", "youtube.com", "reddit.com", "twitter.com", "comcastroturf.com", "netflix.com"]

ping_command = "ping -c 4 {0} | tail -1| awk '{{print $4}}' | cut -d '/' -f 2"
curl_command = "curl -s -w %{{time_total}}\\n -o /dev/null {0}"

data_list = []
unique_website_list = []
w_list_short = []

date_string = datetime.now().timetuple().tm_yday

with open("website_list.csv", "r") as website_csv:
	website_list = website_csv.readlines()

for item in website_list:
	a = item.split(",")[1]
	if len(a) < 20:
		w_list_short.append(a)

for website in w_list_short:
	url = website.lower()
	if url not in unique_website_list:
		unique_website_list.append(website)

print len(unique_website_list)

for website in unique_website_list:
	url = website
	print 'Trying:', url
	try:
		data_list.append(float(subprocess.check_output(curl_command.format(url), shell=True)[:-1]))
	except:
		print 'Could not connect to site. Moving on. '
		unique_website_list.pop(unique_website_list.index(website))

with open("data_for_{0}.txt".format(date_string), "w") as database:
	for website in unique_website_list:
 		database.write("%s" % website)
 	database.write("======================\n")
 	for element in data_list:
 		database.write("%s\n" % str(element))


print data_list
y_pos = [x for x in range(0, len(data_list))]
plt.bar(y_pos, data_list, align='center', alpha=0.5)
plt.xticks(y_pos, website_list)
plt.ylabel('Response time based on curl')
plt.title("Website responsivess before/after Net Neutrality was demolished, date is: {0}".format(date_string))
plt.show()
