import pymysql
import unicodecsv
from convert_txt_to_csv import converttxt
import sys
import os

def write_to_database(networkname):

	networkname = str(networkname)
	converttxt(str(networkname))

	path = str(os.getcwd()) # getting current path
	datapath = path + '/Data/'

	db = pymysql.connect(host='localhost', user='root', passwd='hawkinszlc', db='Final')
	c = db.cursor()

	# reading file
	f= open(datapath + networkname + '.csv')
	csv = unicodecsv.reader(f)

	# feeding the data to the database
	header = True
	for i in csv:    # getting data for each line
		if header:
			header=False
			continue
		sender = i[0]
		receiver = i[1]
		count = i[2]
		layer = networkname[:3]

		sql = "INSERT INTO network (source, target, weight, layer) VALUES ('%s','%s','%s', '%s')" % (sender, receiver, count, layer)
		c.execute(sql)

	db.commit()
	c.close()


#if __name__ == "__main__":
	#write_to_database(sys.argv[1])