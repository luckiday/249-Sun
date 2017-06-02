commNodes = {}
tracker = 1

# this function checks to see if both nodes that are part of the edge exist in one 
# of the communitites. Returns true if they do, false otherwise
def checkInCommunity (node1, node2):
	node1Exists = False
	node2Exists = False

	#checking if node 1 exists in a community
	for i in range (1,6):
		if commNodes.get(i).count(node1) > 0:
			node1Exists = True
			break

	#checking if node 2 exists in a community 
	for j in range(1,6):
		if commNodes.get(i).count(node2) > 0:
			node2Exists = True
			break
	
	return (node1Exists and node2Exists)


#opening the read and write files here
topComm = open("top_5_communities.txt", "r")
readFile = open("com-dblp.ungraph.txt", "r")
writeFile = open("edges_clean.txt", "w")

#reading the nodes of each community and putting it into the dictionary
for line in topComm:
	commNodes[tracker] = line.strip().split()
	tracker += 1

for line in readFile:
	if line[0] == '#':
		continue

	nodes = line.strip().split('\t')

	# writing the edge to the file only if both nodes exist in the top 5 communities
	if checkInCommunity(nodes[0], nodes[1]):
		writeFile.write(line)
	
topComm.close()
readFile.close()
writeFile.close()



