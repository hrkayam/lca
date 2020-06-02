import unittest
from tree import *

class TestLCA(unittest.TestCase):

    def test_case1(self):
        A = Node('A')
        tree = Tree(A)

        self.assertEqual(lca(tree, A, A), A)

    def test_case2(self):
        A = Node('A')
        B = Node('B')
        A.add_child(B)
        tree = Tree(A)

        self.assertEqual(lca(tree, A, B), A)
        self.assertEqual(lca(tree, B, A), A)
        self.assertEqual(lca(tree, B, B), B)

    def test_case3(self):
        A = Node('A')
        B = Node('B')
        C = Node('C')
        A.add_child([B, C])
        tree = Tree(A)

        self.assertEqual(lca(tree, A, C), A)
        self.assertEqual(lca(tree, A, B), A)
        self.assertEqual(lca(tree, B, C), A)

    def test_case4(self):
        A = Node('A')
        B = Node('B')
        C = Node('C')
        A.add_child(B)
        B.add_child(C)
        tree = Tree(A)

        self.assertEqual(lca(tree, A, C), A)
        self.assertEqual(lca(tree, A, B), A)
        self.assertEqual(lca(tree, B, C), B)

    def test_case5(self):
        A = Node('A')

        B = Node('B')
        C = Node('C')

        D = Node('D')
        E = Node('E')
        F = Node('F')
        G = Node('G')

        H = Node('H')
        I = Node('I')
        J = Node('J')

        A.add_child([B, C])

        B.add_child([D, E, F])
        C.add_child(G)

        D.add_child(H)
        E.add_child([I, J])

        tree = Tree(A)

        self.assertEqual(lca(tree, B, C), A)
        self.assertEqual(lca(tree, B, G), A)
        self.assertEqual(lca(tree, H, D), D)
        self.assertEqual(lca(tree, H, F), B)
        self.assertEqual(lca(tree, I, G), A)
        self.assertEqual(lca(tree, H, D), D)
        self.assertEqual(lca(tree, I, I), I)

if __name__ == '__main__':
    unittest.main()
