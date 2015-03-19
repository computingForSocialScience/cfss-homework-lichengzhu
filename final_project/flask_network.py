from flask import Flask, render_template, request
import pymysql
from analyze_network import analyzenetwork
from database_network import write_to_database


app = Flask(__name__)

# checking if the table "network" exists in the database. If yes, drop it and create a table with same name. If no, create a table.
# this step is to make sure data will not be fed to local database twice.
db = pymysql.connect(host='localhost', user='root', passwd='hawkinszlc', db='Final')
c = db.cursor()
try:
	c.execute("DROP TABLE IF EXISTS network")
	c.execute("CREATE TABLE network (source INT (3), target INT (3), weight INT (1), layer VARCHAR (3)) ENGINE = MyISAM DEFAULT CHARSET=utf8;")
except:
	c.execute("CREATE TABLE network (source INT (3), target INT (3), weight INT (1), layer VARCHAR (3)) ENGINE = MyISAM DEFAULT CHARSET=utf8;")
db.commit()
c.close()



#adding all the data to the database by calling "write_to_database" function
write_to_database('information')
write_to_database('support')
write_to_database('collaboration')
write_to_database('financial_aid')


# the application
@app.route('/')
def index():
	
	return render_template('index.html')


@app.route('/comparasion/', methods=['GET', 'POST'])
def comparasion():

	network1 = request.args.get('Network1')
	network2 = request.args.get('Network2')
	metric = request.args.get('CompareBy')
	#print('***************************', network1, network2, metric)

	# showing and calculating the data
	result1 = analyzenetwork(network1, metric)
	result2 = analyzenetwork(network2, metric)


	# composing the file name, inorder to insert in html
	filename1 = str(network1) + "_" + str(metric) + ".png"
	filename2 = str(network2) + "_" + str(metric) + ".png"
	# filepath1 = "'/" + filename1 + "'"
	# filepath2 = "'/" + filename2 + "'"
	# print(filepath1, filepath2)


	return render_template('comparasion.html', metric = metric, myvarname1 = result1, myvarname2 = result2, filenameone = filename1, filenametwo = filename2, network1 = network1, network2 = network2)


if __name__ == '__main__':
	app.debug = True
	app.run()