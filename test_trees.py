"""
unit test file for binary_tree.py
"""

import unittest
import binary_tree


class TestBinaryTree(unittest.TestCase):

    def test_search_in_tree(self):
        datatree = binary_tree.create_tree('tabsep_testdata.txt')
        self.assertEqual(binary_tree.search(datatree, '30068'), '22623')

    def test_search_not_in_tree(self):
        datatree = binary_tree.create_tree('tabsep_testdata.txt')
        self.assertEqual(binary_tree.search(datatree, '2'), None)


if __name__ == '__main__':
    unittest.main()
