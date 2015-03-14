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
	for sender,receiver,count in edgeList.to_records(index=False):
		g.add_edge(sender,receiver,count=count)

	#g.in_degree()
	#nx.betweenness_centrality(g)

	# draw the network with matplotlib
	nx.draw(g,with_labels=True)
	filename = str(networkname) + '.png'
	plt.savefig(filename)


if __name__ == "__main__":
	drawnetwork(sys.argv[1])

