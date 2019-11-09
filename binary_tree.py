"""
Module to build and search through an AVL tree
"""

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

        Returns
        -------
        A node

        """
        self.key = key
        self.value = value
        self.left = left
        self.right = right


def insert(root, key, value=None):
    """
    Inserts a node into the tree. Works down from the root.

    Parameters
    ----------
    root: the tree to insert into. called root because the function will start
    at the root of this tree, and then work its way down comparing to
    successive nodes
    key: the key to insert from a key, value pair
    value: the value to insert from a key, value pair
    """

    if key < root.key:
        if root.left is None:
            root.left = Node(key, value)  # create node here
        else:
            # try insert again at the next node down
            insert(root.left, key, value)
    else:
        if root.right is None:
            root.right = Node(key, value)
        else:
            insert(root.right, key, value)
    return root


def search(root, key):
    """
    Search for the node with specified key

    Parameters
    ----------
        root: root of tree, starting point of search
        key: the key of the node we want to find

    Returns
    -------
        The node with this key
    """
    if key == root.key:
        return root.value
    elif key < root.key:
        if root.left is None:
            print('key is not in tree')
            return None  # means the key is not in the tree
        else:
            return search(root.left, key)
    else:
        if root.right is None:
            print('key is not in tree')
            return None
        else:
            return search(root.right, key)


def create_tree(datafile, N):
    """
    creates a binary search tree from an imported data set

    Parameters
    ----------
    datafile: a tab-separated txt file containing key, value pairs
    N: the number of keys to insert from the file, starting from the top

    Returns
    -------
    A tree containing the specified number of key, value pairs

    """

    file = datafile

    isfirstline = True
    counter = 0
    for line in open(file, 'r'):
        data = line.rstrip().split('\t')
        if isfirstline is True:
            datatree = Node(data[0], data[1])
            isfirstline = False
        else:
            insert(datatree, data[0], data[1])
        counter += 1
        if counter == N:
            break

    return datatree
