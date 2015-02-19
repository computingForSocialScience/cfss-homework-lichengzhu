import pandas as pd
import numpy as np 
import networkx as nx

def readEdgeList(filename):
	edge_df = pd.read_csv(filename)
	if len(edge_df.columns) > 2:
		print "Error: more than 2 columns" 
		edge_df = pd.read_csv(filename, usecols = [0,1])
		dataframe = pd.DataFrame(edge_df)
	else:
		dataframe = pd.DataFrame(edge_df)
	return dataframe

#filename = 'edgelist.csv'
#readEdgeList(filename)

def degree(edgeList, in_or_out):
	#print len(edgeList)
	if in_or_out == 'out':
		df = edgeList['artist'].value_counts()
	elif in_or_out == 'in':
		df = edgeList['related_artist'].value_counts()
	else:
		print "you have to tell it in or out, stupid"
	return df

#in_or_out = 'out'
#filename = 'edgelist.csv'
#edgeList = readEdgeList(filename)
#print degree(edgeList, in_or_out)

def combineEdgeLists(edgeList1, edgeList2):
	pieces = [edgeList1, edgeList2]
	concatenated = pd.concat(pieces)
	combined = concatenated.drop_duplicates()
	#combined = DataFrame.drop_duplicates(concatenated)
	return combined

def pandasToNetworkX(edgeList): 
	g = nx.DiGraph()
	for artist, related_artist in edgeList.to_records(index=False):
		g.add_edge(artist, related_artist)
	return g

"""def randomCentralNode(inputDiGraph):
	centrality_dict = nx.eigenvector_centrality(inputDiGraph)
	normalization = float(sum(centrality_dict.itervalues()))
	for key, value in centrality_dict.items():
		centrality_dict[key] = value #/ normalization
	random_node = np.random.choice(centrality_dict.keys()#, p=centrality_dict.values())
	return random_node"""

def randomCentralNode(inputDiGraph):
	centrality_dict = nx.eigenvector_centrality(inputDiGraph)
	normalization = sum(centrality_dict.values())
	for key in centrality_dict:
		try:
			centrality_dict[key] = centrality_dict[key]/float(normalization)
		except ZeroDivisionError:
			centrality_dict[key] = 1.0/len(centrality_dict)
	random_node = np.random.choice(centrality_dict.keys(), p=centrality_dict.values())
	return random_node