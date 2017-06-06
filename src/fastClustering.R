rm(list = ls())
library('igraph')
library("fcd")
library("hashmap")
edges = read.csv("../data/top5CommunitiesEdges.csv", header = FALSE, sep = ",")
# read communities
con  <- file("../data/top5Communities.txt", open = "r")
communities <- list()
while (length(oneLine <- readLines(con, n = 1, warn = FALSE)) > 0) {
  myVector <- (strsplit(oneLine, ","))
  myVector <- list(as.numeric(myVector[[1]]))
  communities <- c(communities,myVector)
} 
close(con)

#form the graph based on the edgelist
edges = as.matrix(edges)
g=graph.data.frame(edges,directed = FALSE)
# am = as_adj(g)
# clusters = spectral.clustering(am, K = 5)
communities = fastgreedy.community(g) # 289 communities

distable = distances(g)
nameList = V(g)$name
nameMap = hashmap(nameList,1:length(nameList))
write.table(communities, "fastGreedy.txt")

for(i in 1:289){
  lapply(communities[i], write, "test.txt", append=TRUE, ncolumns=5000)
}


data = read.table("communityDistanceMatrix.csv",sep = ",")
data = as.matrix(data)
communities2 = spectral.clustering(data, K = 5, adj = TRUE)

lapply(communities2, write, "communities2.txt", append=TRUE, ncolumns=5000)
