import unittest
from node import Node
from tree import Tree

class TestTreeFind(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        for value in [10, 5, 15, 3, 7]:
            self.tree.add(value)

    def test_find_existing_node(self):
        node = self.tree.find(7)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 7)
        self.assertIsInstance(node, Node)

    def test_find_nonexistent_node(self):
        node = self.tree.find(20)
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()
