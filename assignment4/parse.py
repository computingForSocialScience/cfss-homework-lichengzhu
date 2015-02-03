#%matplotlib inline
import matplotlib as plt
from matplotlib.pyplot import plot, hist
import csv
import sys

def readCSV(filename):

	with open(filename,'r') as f:
		rdr = csv.reader(f)
		lines = list(rdr)
	return(lines)

### enter your code below

# counting the sum
def get_avg_latlng(filename):
	
	lines = readCSV(filename)    #import and read the file, export it to a list
	sum_lag = 0
	sum_lng = 0
	for i in lines:
		if i[-3] == "": continue
		if i[27] == "NJ": continue
		sum_lag = sum_lag + float(i[-3])
		sum_lng = sum_lng + float(i[-2])

	avg_lag = sum_lag / float(len(lines) - 3)  #skipped one row with empty data and two HYDE PARK in NJ
	avg_lng = sum_lng / float(len(lines) - 3)

	print("average latitude: ", avg_lag, "average longitude: ", avg_lng)


def zip_code_barchat(filename):
	lines = readCSV(filename)
	zipcodes = []
	for i in lines:
		thiszipcode = i[27]
		zipcodes.append(int(thiszipcode[:5]))
	zip_graph = hist(zipcodes)
	zip_graph.show()
	


if __name__ == '__main__':
	#print "we're in main, here"
	get_avg_latlng("permits_hydepark.csv")
	zip_code_barchat