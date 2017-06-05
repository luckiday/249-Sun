rm(list = ls())
library('igraph')
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
fastgreedy.community(g)
