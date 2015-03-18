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

	edgeList = []
	g = nx.DiGraph() 

	query = """SELECT * FROM network WHERE layer = '%s'""" % networkbriefname
	c.execute(query)
	data = c.fetchall()

	# checking if the retrived data is empty or not. If yes, write it to the database; if no, then add the retrived data to the edgeList
	if len(data) == 0:
	 	write_to_database(networkname)   # wrte the data to the database first
	 	query = """SELECT * FROM network WHERE layer = '%s'""" % networkbriefname
	 	c.execute(query)
	 	data = c.fetchall()

	 	for i in data:
	 		sender = i[0]
	 		receiver = i[1]
	 		weight = i [2]
	 		g.add_edge(sender, receiver, count = weight)
	else:
	 	for i in data:
	 		sender = i[0]
	 		receiver = i[1]
	 		weight = i [2]
	 		g.add_edge(sender, receiver, count = weight)


	# related metrics
	#density = nx.density(g)
	#degree = nx.degree(g)
	#in_degree = g.in_degree(g)
	#out_degree = g.out_degree(g)
	betweenness = nx.betweenness_centrality(g)
	closeness = nx.closeness_centrality(g)

	static = 'static'  # creating the directory
	if not os.path.exists(static):
		os.makedirs(static)


	# draw the network with matplotlib by closeness or betweeness; alternatively one can choose to draw and compare regular networks
	if str(metric) == "none": # drawing regular networks

		lyt = nx.layout.spring_layout(g) # making sure the node positions are the same
		nx.draw(g, pos=lyt, with_labels=True, node_color='blue', font_size=9)

		filename = "static/" + str(networkname) + "_" + str(metric) + '.png'
		plt.savefig(filename)

		return(betweenness, closeness)

	if str(metric) == "closeness": # node size adjusted according to betweenness
		d = closeness
		lyt = nx.layout.spring_layout(g) # making sure the node positions are the same
		nx.draw(g, pos=lyt, with_labels=True, node_color='blue', nodelist=d.keys(), node_size=[v * 1000 for v in d.values()], font_size=9)

		filename = "static/" + str(networkname) + "_" + str(metric) + '.png'
		plt.savefig(filename)

		return(closeness)

	if str(metric) == "betweenness": # node size adjusted according to betweenness
		d = betweenness
		lyt = nx.layout.spring_layout(g) # making sure the node positions are the same
		nx.draw(g, pos=lyt, with_labels=True, node_color='blue', nodelist=d.keys(), node_size=[v * 10000 for v in d.values()], font_size=9)

		filename = "static/" + str(networkname) + "_" + str(metric) + '.png'
		plt.savefig(filename)

		return(betweenness)




if __name__ == "__main__":
	analyzenetwork(sys.argv[1], sys.argv[2])

