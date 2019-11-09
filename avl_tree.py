"""
Module to build and search through an AVL tree
"""

import csv


class Node:
    def __init__(self, key, value=None, parent=None, left=None, right=None,
                 height=-1):
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
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right
        self.height = height


def update_height(node):
    """
    Updates the value of self.height for a given node
    """
    if node.left is None:
        node.height = node.right.height + 1
    elif node.right is None:
        node.height = node.left.height + 1
    else:
        node.height = max(node.left.height, node.right.height) + 1


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
            root.left.parent = root.key
        else:
            # try insert again at the next node down
            insert(root.left, key, value)
            update_height(root)
    else:
        if root.right is None:
            root.right = Node(key, value)
            root.right.parent = root.key
        else:
            insert(root.right, key, value)
            update_height(root)
    return root


def left_rotate(node):
    """
    Perform a left rotation from a specified node when the tree is unbalanced
    """
    y = node.right
    y.parent = node.parent
    if y.parent.left is node:
        y.parent.left = y
    elif y.parent.right is node:
        y.parent.right = y
    node.right = y.left
    node.right.parent = node
    y.left = node
    node.parent = y
    update_height(node)
    update_height(y)


def right_rotate(node):
    """
    Perform a right rotation from a specified node when the tree is unbalanced
    """
    y = node.left
    y.parent = node.parent
    if y.parent.left is node:
        y.parent.left = y
    elif y.parent.right is node:
        y.parent.right = y
    node.left = y.right
    node.left.parent = node
    y.right = node
    node.parent = y
    update_height(node)
    update_height(y)


def rebalance(node):
    """
    Rebalance the tree. Compares the heights of two child nodes to determine
    what rotation is needed
    """
    while node is not None:
        if node.left.height >= 2 + node.right.height:
            if node.left.left.height >= node.left.right:
                right_rotate(node)
            else:
                left_rotate(node.left)
                right_rotate(node)
        elif node.right.height >= 2 + node.left.height:
            if node.right.right.height >= node.right.left:
                left_rotate(node)
            else:
                right_rotate(node.right)
                left_rotate(node.right)
        node = node.parent


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


def create_AVLtree(datafile, N):
    """
    creates an AVL search tree from an imported data set

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
