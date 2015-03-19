import os
import sys
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
#from convert_txt_to_csv import converttxt
import pymysql
from database_network import write_to_database


def analyzenetwork(networkname, metric):
	"""this function calculates and graphs the network coording to related metrics, including betweenness and closeness, for selected network"""

	networkname = str(networkname)
	networkbriefname = str(networkname)[0:3]

	db = pymysql.connect(host='localhost', user='root', passwd='hawkinszlc', db='Final')
	c = db.cursor()

	query = """SELECT * FROM network WHERE layer = '%s'""" % networkbriefname #get selected network (contrained by the "layer" name) from the databate
	c.execute(query)
	data = c.fetchall()
	#print data

	# adding data to graph "g"
	g = nx.DiGraph() 
	g.clear()
	for i in data:
		sender = i[0]
	 	receiver = i[1]
	 	g.add_edge(sender, receiver)
	 	#print(sender, receiver, networkbriefname)
	#print(networkname, " has:", g.nodes())

	# creating the directory if does not exist
	static = 'static/pics/'
	if not os.path.exists(static):
		os.makedirs(static)


	# draw the network with matplotlib by closeness or betweeness; alternatively one can choose to draw and compare regular networks
	if str(metric) == "none": # drawing regular networks

		# calculating related metrics
		betweenness = nx.betweenness_centrality(g)
		closeness = nx.closeness_centrality(g)

		#lyt = nx.layout.spring_layout(g) # making sure the node positions are the same
		nx.draw(g, with_labels=True, node_color='blue', font_size=9)

		filename = "static/pics/" + str(networkname) + "_" + str(metric) + '.png'
		plt.savefig(filename)

		return(betweenness, closeness)

	elif str(metric) == "closeness": # node size adjusted according to closeness
		# calculating related metrics
		closeness = nx.closeness_centrality(g)

		d = closeness
		#lyt = nx.layout.spring_layout(g) # making sure the node positions are the same
		nx.draw(g, with_labels=True, node_color='blue', nodelist=d.keys(), node_size=[v * 500 for v in d.values()], font_size=9)

		filename = "static/pics/" + str(networkname) + "_" + str(metric) + '.png'
		plt.savefig(filename)


		return(closeness)

	elif str(metric) == "betweenness": # node size adjusted according to betweenness
		# calculating related metrics
		betweenness = nx.closeness_centrality(g)

		z = betweenness
		#lyt = nx.layout.spring_layout(g) # making sure the node positions are the same
		nx.draw(g, with_labels=True, node_color='blue', nodelist=z.keys(), node_size=[v * 2000 for v in z.values()], font_size=9)

		filename = "static/pics/" + str(networkname) + "_" + str(metric) + '.png'
		plt.savefig(filename)
	
		return(betweenness)




if __name__ == "__main__":
	analyzenetwork(sys.argv[1], sys.argv[2])

