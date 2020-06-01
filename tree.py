def euler_tour(root, node_list, index_list, counter):
    node_list.append(root)
    if root.index == None:
        root.index = counter
        counter += 1
    index_list.append(root.index)
    for child in root.children:
        node_list, index_list, counter = euler_tour(child, node_list, index_list, counter)
        node_list.append(root)
        index_list.append(root.index)
    return node_list, index_list, counter

def LCA(Tree, a, b):
    node_list = []
    index_list = []
    first_occ = []

    nl, il, _ = euler_tour(self.root, node_list, self.index_list, 0)

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
     print(tree.index_list)
     print(tree.node_list)
