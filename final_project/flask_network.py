from flask import Flask, render_template, request
import pymysql
from analyze_network import analyzenetwork


app = Flask(__name__)

# # connecting to the local database
# conn = pymysql.connect(host='localhost', user='root', passwd='hawkinszlc', db='Final',charset='utf8')
# cur = conn.cursor()


@app.route('/')
def index():
	
	return render_template('index.html')


@app.route('/comparasion/', methods=['GET', 'POST'])
def comparasion():

	network1 = request.args.get('Network1')
	network2 = request.args.get('Network2')
	#print(network1)
	metric = request.args.get('CompareBy')

	# calling the "analyzenetwork" function to do the calculation and the drawing
	analyzenetwork(network1, metric)
	analyzenetwork(network2, metric)

	# show the data
	result1 = analyzenetwork(network1, metric)
	#print("hahahahahahahahahahaha", result1)
	# resultlist1 = []
	# for k, v in result1.iteritems():
	# 	item1 = str(k) + " :" + str(v)
	# 	resultlist1.append(item1)

	result2 = analyzenetwork(network2, metric)
	# resultlist2 = []
	# for k, v in result2.iteritems():
	# 	item2 = str(k) + " :" + str(v)
	# 	resultlist2.append(item2)

	#print(result1)


	# composing the file name
	filename1 = str(network1) + "_" + str(metric) + ".png"
	filename2 = str(network2) + "_" + str(metric) + ".png"


	return render_template('comparasion.html', myvarname1 = result1, myvarname2 = result2, filename1 = filename1, filename2 = filename2, network1 = network1, network2 = network2)



if __name__ == '__main__':
	app.debug = True
	app.run()




















if __name__ == '__main__':
	app.debug = True
	app.run()