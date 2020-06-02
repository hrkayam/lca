
root = Node('A')
tree1 = Tree(root)

root = Node('A')
B = Node('B')
A.add_child(B)
tree2 = Tree(root)

root = Node('A')
B = Node('B')
C = Node('C')
A.add_child([B, C])
tree3 = Tree(root)

root = Node('A')
B = Node('B')
C = Node('C')
A.add_child(B)
B.add_child(C)
tree4 = Tree(root)

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

tree5 = Tree(root)
