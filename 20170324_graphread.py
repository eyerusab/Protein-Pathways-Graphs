#Metin Toksoz-Exley GEPHI
#THE VARIABLES TO CHANGE ARE RANGE OF T K 
#Grab a random pathway 
import csv 
import random  
import numpy as np 
import matplotlib.pyplot 
"""
def random_row(file): 
    line = next(file) 
    for num, row in enumerate(file): 
      if random.randrange(num + 2): continue 
      line = row 
    return line 
"""
plen=[]
qlen=[]
k=5
with open('SelectedPathways.csv', 'rt') as file: 
    contents = csv.reader(file) 
    pathways=list(contents)
pathways=[[protein for protein in pathway if protein!=''] for pathway in pathways]
#    [x for x in contents]
#    file.seek(0) like 
for t in range(10000):
	
	pathway = random.choice(pathways)
	#print pathways
	#print pathway
	protein=random.choice(pathway)
	#print protein

	p=[]
	for p1 in pathways:
		if protein in p1:
			p.append(p1)
	
# alternative to above p=[pathway for pathway in pathways if protein in pathway] THIS IS A LIST COMPREHENSION ABOVE IS LOOPING 
	kproteins=[]
	for i in range(k):
		randomproteins=random.choice(pathway)
		kproteins.append(randomproteins)
	#print kproteins  
	q=[]
	for p2 in p:
		usePathway=True
		for otherprotein in kproteins:
			if otherprotein not in p2:
				usePathway=False
				break

		if usePathway: q.append(p2)
	#print "q="+str(len(q)) +" and p="+str(len(p))


	plen.append(len(p))
	qlen.append(len(q))

print zip(plen, qlen)

matplotlib.pyplot.scatter(qlen, plen)
matplotlib.pyplot.show()
"""
heatmap, xedges, yedges=np.histogram2d(plen, qlen, bins=60)
extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]]
matplotlib.pyplot.clf()
matplotlib.pyplot.imshow(heatmap, extent=extent)
matplotlib.pyplot.show() 


    #assuming I don't need to limit it to the 633 actual rows because it has imported all data so 
    #random should stay within that constraint


#Grab a random set of n proteins from pathway

#Loop over all pathways 

#Report the ratio 

#Loop back to 1 to build up a sample
#Loop back to 1 with the next n to build stem and leaf plot for each n 
"""
