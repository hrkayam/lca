# lca
LCA implementation for an n-nary tree: Euler Tour with Ranged Minimal Query (RMQ) using segment trees
- See tree.py comments for preliminary time complexity explanations and basic subroutine testing

# Correctness and Time Complexity

Performing a Euler Tour on an n-nary tree creates an easily traversable respresentation. 

We generate 3 structures:
- a list of nodes visited in order
- a list of corresponding indicies based on traversal order
- a table of indices of the first occurrence of every node 

The minumum value between two indicies corresponds to the LCA of the respective boundary nodes to the traversal order of a Euler Tour
This construction visits every edge twice. Thus: 

                                              2*|E| = 2*(|V| - 1) --> O(2n) --> O(n) time
where n is the number of nodes in the tree.
