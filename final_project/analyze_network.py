import os
import sys
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from convert_txt_to_csv import converttxt

def drawnetwork(networkname):
	""" this function calls convertxt function, drawing a network based on the converted csv file. Notice each time only one network will be drawn."""

	converttxt(str(networkname))

	path = str(os.getcwd()) # getting current path
	datapath = path + '/Data/'

	# reading file
	edgeList = pd.read_csv((datapath + str(networkname) + ".csv"))

	# getting data to edgeList
	g = nx.DiGraph()
	t = nx.DiGraph().to_undirected(g) # converting the digraph to undigraph for future use, the variable name "t" is the first letter of Chinese pinyin (tupian) for graph 
	for sender,receiver,count in edgeList.to_records(index=False):
		g.add_edge(sender,receiver,count=count)


	# draw the network with matplotlib
	#nx.draw(g,with_labels=True)
	nx.draw(g,pos=nx.layout.spring_layout(g),with_labels=True,node_color='blue')
	filename = str(networkname) + '.png'
	plt.savefig(filename)


def calculatenetwork(networkname):
	"""this function calculates related metrics, including density, degree, betweenness, clustering_coefficient and closeness, for selected network"""

	converttxt(str(networkname))

	path = str(os.getcwd()) # getting current path
	datapath = path + '/Data/'

	# reading file
	edgeList = pd.read_csv((datapath + str(networkname) + ".csv"))

	# getting data to edgeList
	g = nx.DiGraph()
	t = nx.DiGraph().to_undirected(g) # converting the digraph to undigraph for future use, the variable name "t" is the first letter of Chinese pinyin (tupian) for graph 
	for sender,receiver,count in edgeList.to_records(index=False):
		g.add_edge(sender,receiver,count=count)

	# related metrics
	density = nx.density(g)
	degree = nx.degree(g)
	in_degree = g.in_degree(g)
	out_degree = g.out_degree(g)
	betweenness = nx.betweenness_centrality(g)
	clustering_coefficient = nx.clustering(t)
	closeness = nx.closeness_centrality(g)

	#return(in_degree, out_degree, betweenness,clustering_coefficient, closeness)
	print(in_degree, out_degree, betweenness,clustering_coefficient, closeness)




if __name__ == "__main__":
	drawnetwork(sys.argv[1])
	calculatenetwork(sys.argv[1])

