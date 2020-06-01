import math

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

def seg_tree(arr):
    segment_tree = [None] * len(arr)
    segment_tree.extend(arr)
    for i in range(len(arr) - 1, 1):
        print('HELLO')
        print(min((segment_tree[2*i], segment_tree[2*i + 1])))
        segment_tree[i] = min((segment_tree[2*i], segment_tree[2*i + 1]))
    return segment_tree

def rmq(left, right, arr):
    seg_tree = seg_tree(arr)
    left += len(arr)
    right += len(arr)
    minimum = math.inf
    while left < right:
        if left % 2 == 1:
            minimum = min(minimum, seg_tree(left))
            left += 1
        if right % 2 == 1:
            right -= 1
            minimum = min(minimum, seg_tree(right))
        left /= 2
        right /= 2
    return minimum

# def lca(Tree, a, b):
#     node_list = []
#     index_list = []
#     first_occ = []
#
#     nl, il, fo, _ = euler_tour(self.root, node_list, index_list, first_occ, 0
#
#     return 0

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

class Tree(object):

    def __init__(self, root):
        self.root = root

        nl, il, fo, _ = euler_tour(self.root, [], [], [], 0)
        self.node_list = nl
        self.index_list = il
        self.first_occ = fo

if __name__== "__main__":
     root = Node('A')

     B = Node('B')
     C = Node('C')

     D = Node('D')
     E = Node('E')
     F = Node('F')
     G = Node('G')

     H = Node('H')
     I = Node('I')
     J = Node('J')

     root.add_child([B, C])

     B.add_child([D, E, F])
     C.add_child(G)

     D.add_child(H)
     E.add_child([I, J])

     tree = Tree(root)

     print("EULER TOUR TEST")
     print(tree.node_list)
     print(tree.index_list)
     print(tree.first_occ)

     print("SEG TREE TEST")
     arr = [1,5,3,7,3,6,5,7]
     print(seg_tree(arr))
