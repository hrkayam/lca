# Least Common Ancestor (LCA) Implementation for an N-nary Tree
Run unit tests in terminal using this command:

                                                     python test_lca.py

See test_case_1-4.jpg and test_case_5.jpg for illustrations of the tree structures tested.

# Correctness and Time Complexity

Performing a Euler Tour on an n-nary tree creates an easily traversable respresentation. 

In preprocessing, we generate 3 structures:
- a list of nodes visited in order
- a list of corresponding indicies based on traversal order
- a table of indices of the first occurrence of every node 

and store there as attributes of our tree upon its creation

The minumum value between two indicies corresponds to the LCA of the respective boundary nodes to the traversal order of a Euler Tour
This construction visits every edge twice. Thus: 

                                            2*|E| = 2*(|V| - 1) --> O(2n) --> O(n) time

where n is the number of nodes in the tree.

To find the minimum index between those of two nodes A and B, we implement the Ranged Minimum Query (RMQ) operation.
This operation utilizes a segement tree represented in a heap structure which is built in *O(log(n))* time and queried by the RMQ function in *O(log(n))* time.

The LCA algorithm uses the ascertained minimum to query from the first occurence table in *O(1)* time and returns the coreesponding Node from the node list in *O(1)* time.

Thus the total time complexity is:

With preprocessing:

                                          O(n) + O(logn) + O(logn) + O(1) + O(1) ~ O(n) time

Without preprocessing:

                                           O(logn) + O(logn) + O(1) + O(1) ~ Olog(n)) time
