import csv

class Node:
    def __init__(self, key, value=None, left=None, right=None):
        """
        creates a node

        Parameters
        ----------
            key: the key of the node
            value: the value associated with key
            left: the left child of the node
            right: the right child of the node

        """
        self.key = key
        self.value = value
        self.left = left
        self.right = right
