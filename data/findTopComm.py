topCommunities = {}
communityNum = 1

#opening the read and write files here
read = open("com-dblp.all.cmty.txt", "r")
writeFile = open("top_5_communities.txt", "w")

for line in read:
	
	#getting the number of nodes in the community
	numOfNodes = len(line.strip().split('\t'))

	if len(topCommunities) < 5:
		topCommunities[communityNum] = numOfNodes

	else:
		#finding the smallest community in the top 5
		minNum = min(topCommunities, key = lambda x: topCommunities.get(x))
		
		#if the curent community has more than the min in the top 5, we need to do replacement.
		if numOfNodes > topCommunities.get(minNum):
			del topCommunities[minNum]
			topCommunities[communityNum] = numOfNodes

	communityNum += 1

read.seek(0)
communityNum = 1

#looping again and extracting the nodes of the 5 biggest communities
for line in read:
	
	#if we have arrived at a top community in the file, write it to the output file
	if topCommunities.has_key(communityNum):
		writeFile.write(line) 

	communityNum += 1

writeFile.close()
read.close()

print (topCommunities)