import math

# performing a Euler Tour on an n-nary tree creates an easily traversable respresentation
# the minumum value of a between two indicies corresponds to the LCA of the respective boundary nodes
# Visits every edge twice --> 2*|E| = 2*(|V| - 1) --> O(2n) --> O(n) time
# where n is the number of nodes
def euler_tour(root, node_list, index_list, first_occ, counter):
    node_list.append(root)
    if root.index == None:
        root.index = counter
        counter += 1
        first_occ.append(len(index_list))

    index_list.append(root.index)
    for child in root.children:
        node_list, index_list, first_occ, counter = euler_tour(child, node_list, index_list, first_occ, counter)
        node_list.append(root)
        index_list.append(root.index)
    return node_list, index_list, first_occ, counter

# segment tree represents minima of all power of 2 subarrays in a heap strcuture
# construction: O(log(n)) time
def seg_tree(arr):
    segment_tree = [None] * len(arr)
    segment_tree.extend(arr)
    for i in range(len(arr) - 1, 0, -1):
        segment_tree[i] = min((segment_tree[2*i], segment_tree[2*i + 1]))
    return segment_tree

#traverses segment tree in O(log(n)) since by theory at each level we visit <=4 nodes
#and the height of this tree is log(n)
def rmq(arr, left, right):
    segment_tree = seg_tree(arr)
    left += len(arr)
    right += len(arr)
    if left == right:
        return segment_tree[int(left)]
    if left > right:
        temp = right
        right = left
        left = temp
    minimum = math.inf
    while left < right:
        if left % 2 == 1:
            minimum = min(minimum, segment_tree[int(left)])
            left += 1
        if right % 2 == 1:
            right -= 1
            minimum = min(minimum, segment_tree[int(right)])
        left /= 2
        right /= 2
    return int(minimum)

#performs rmq on euler walk tree respresentation to determine the index of and return the LCA
def lca(tree, a, b):

    min_idx = rmq(tree.index_list, tree.first_occ[a.index], tree.first_occ[b.index])
    return tree.node_list[tree.first_occ[min_idx]]

class Node(object):
    def __init__(self, name):
        self.name = name
        self.index = None
        self.children = []

    def __str__(self):
        return self.name

    __repr__ = __str__

    def add_child(self, children):
        if type(children) is list:
            self.children.extend(children)
        else:
            self.children.append(children)

#preprocessing in O(n) time
#arrays for traversal order, assigned, indices and first occurences of nodes stored as Tree attributes
class Tree(object):

    def __init__(self, root):
        self.root = root

        nl, il, fo, _ = euler_tour(self.root, [], [], [], 0)
        self.node_list = nl
        self.index_list = il
        self.first_occ = fo
