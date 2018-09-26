#Eyerusalem Abebe

#This file allows for the organization and reading of the pathways dataset

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


with open('SelectedPathways.csv', 'rb') as f:
	ncols = len(next(f).split(','))
	
x=np.genfromtxt('SelectedPathways.csv', delimiter=',', dtype=None, names=None,
		usecols=range(0,ncols)
		)

network =[]
for row in x:
	newrow=[]
	for col in row:
		if col!='':
			newrow.append(col)
	network.append(newrow)
	
