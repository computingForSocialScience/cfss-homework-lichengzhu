import matplotlib.pyplot as plt
import csv
import sys

def readCSV(filename):

	with open(filename,'r') as f:
		rdr = csv.reader(f)
		lines = list(rdr)
	return(lines)

### enter your code below


def get_avg_latlng(filename):
	""" Computing the means of latitude and longitude"""
	
	jump_count = 0
	lines = readCSV(filename)    #import and read the file, export it to a list
	sum_lag = 0
	sum_lng = 0
	for i in lines:
		if i[-3] == "": 
			jump_count += 1
			continue
		if i[27] == "NJ": 
			jump_count += 1
			continue
		sum_lag = sum_lag + float(i[-3])
		sum_lng = sum_lng + float(i[-2])

	avg_lag = sum_lag / float(len(lines) - jump_count)  #skipped rows with empty data and  HYDE PARK in NJ
	avg_lng = sum_lng / float(len(lines) - jump_count)  #skipped rows with empty data and  HYDE PARK in NJ

	print("average latitude: ", avg_lag, "average longitude: ", avg_lng)


def zip_code_barchat(filename):
	""" Drawing a bar chart of freqency distribution for zip code captured """
	
	lines = readCSV(filename)
	zipcodes = []
	for i in lines:
		thiszipcode = i[28]
		if not thiszipcode.startswith("6"): continue  #getting all zipcodes starting with "6"
		zipcodes.append(int(thiszipcode[:5]))
	
	plt.hist(zipcodes, bins = len(zipcodes), facecolor = "yellow", edgecolor = "grey")   # making a histogram of the data
	
	plt.xlabel("Contractor Zip Code")  # marking label for x-axis
	plt.ylabel("Frequency")  # marking label for y-axis
	plt.title("Frequency Distribution of Zip Codes") # marking the title of the bar chart
	
	# please do not put terminal into the full screen mode!!!
	
	plt.savefig("contractor_zip_code_frequency_distribution.png") # save the figure before .show() is called
	print("A file 'contractor_zip_code_frequency_distribution.png' has been added to your current directory")
	
	plt.show() # print the plot


sys_arg = sys.argv  # getting the argument from the command line input


# syntax error control and combining functions into an executable program
try:
	first_arg = sys_arg[1]
	if first_arg == "latlong": get_avg_latlng("permits_hydepark.csv")
	elif first_arg == "hist": zip_code_barchat("permits_hydepark.csv")
	else: print("Sorry, argument not recognized")
except:
	print("Error: Please specify at least one argument in your command, such as 'latlong' or 'hist'")
