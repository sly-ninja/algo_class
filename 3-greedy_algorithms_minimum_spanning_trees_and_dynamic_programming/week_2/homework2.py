"""
In this programming problem and the next you'll code up the clustering algorithm 
from lecture for computing a max-spacing k-clustering.

Download the text file below.
clustering1.txt

This file describes a distance function (equivalently, a complete graph with 
edge costs). It has the following format:

[number_of_nodes]

[edge 1 node 1] [edge 1 node 2] [edge 1 cost]

[edge 2 node 1] [edge 2 node 2] [edge 2 cost]

...

There is one edge (i,j) for each choice of 1 ≤ i < j ≤ n, where nnn is the 
number of nodes.

For example, the third line of the file is "1 3 5250", indicating that the 
distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 
5250. You can assume that distances are positive, but you should NOT assume 
that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on 
this data set, where the target number k of clusters is set to 4. What is the 
maximum spacing of a 4-clustering?

"""
