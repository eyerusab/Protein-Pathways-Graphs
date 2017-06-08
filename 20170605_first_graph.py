#This file is one that illustrates the original networkx graph of the protein distribution with description of each line running 
#Eyerusalem Abebe
#

#packages imported
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
#This file calls on a previous file that organized the pathways file to make it readable into our code for the graph
execfile('20170209_duplicate.py')

#creating the graph
graph = []
for pathway in network: #depends on network variable from 20170209
	for p1 in pathway: # p is the pathway in the pathway if protein is in the pathway 
		for p2 in pathway:
			graph.append((p1,p2))

#creating networkx graph, by adding edges to the graph from previous protein pathway loop, and plottig the graph through draw and plt functions

G=nx.Graph()
G.add_edges_from(graph)
nx.draw(G)
plt.show()

#run this file after running 20170209_duplicate or tack this onto that file or have this file call other file

#if this graph doesn't work try running the code from '20170216.py'
