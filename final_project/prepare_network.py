import sys as sys
import os as os

def converttxt(networkname):
	"""this is a function to read processed .txt file and convert it to an equivalent .csv file for future analysis"""
	
	filename = str(networkname) + ".txt"
	newfilename = networkname + ".csv"

	path = os.getcwd()   #get current working directory
	filepath = path + "/Data/" + filename
	newfilepath = path + "/Data/" + newfilename

	f = open(filepath, 'r')   #open the original file
	f_new = open(newfilepath, 'w')   #create a new file
	
	f_new.write("sender")  # write the headers to the file
	f_new.write(",")
	f_new.write("receiver")
	f_new.write(",")
	f_new.write("count")
	f_new.write("\n")

	for i in iter(f):  # read line and and write data to the new file

		n = 0   # controling number of "," written into file
		
		line = i.split()
		
		for element in line:
			f_new.write(element)
			n += 1
			if n != 3:
				f_new.write(",")
			else:
				f_new.write("\n")
		

	#print("conversion done!")


	f.close()
	f_new.close()


if __name__ == "__main__":
	converttxt(sys.argv[1])

