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


def insert(root, key, value=None):
    """
    Inserts a node into the tree. Works down from the root.
    """
    # print('type root.key ' + str(type(root.key)))
    # print('type key ' + str(type(key))) --> both strings, all good
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

def main():  # eventually make this a tree function that you call elsewhere 
    """
    creates a binary search tree from an imported data set
    """

    file = 'commasep_testdata.csv'

    isfirstline = True
    for line in open(file, 'r'):
        data = line.rstrip().split(',')
        # print(data[0])
        # print(data[1])
        if isfirstline is True:
            datatree = Node(data[0], data[1])
            isfirstline = False
        else:
            insert(datatree, data[0], data[1])

    result = search(datatree,'8')
    print('the value of 8 is ' + str(result))


if __name__ == '__main__':
    main()
