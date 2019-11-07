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

def rebalance(tree):
    """
    check tree's balance after inserting a node
    """
    # update height and balance of tree
    update_heights(tree, recursive=False)
    update_balances(tree, False)

    # For each node checked,
        #   if the balance factor remains −1, 0, or +1 then no rotations are necessary.
    while tree.balance < -1 or tree.balance > 1:
        # Left subtree is larger than right subtree
        if tree.balance > 1:

            # Left Right Case -> rotate y,z to the left
            if tree.node.left.balance < 0:
                #     x               x
                #    / \             / \
                #   y   D           z   D
                #  / \        ->   / \
                # A   z           y   C
                #    / \         / \
                #   B   C       A   B
                tree.node.left.rotate_left()
                tree.update_heights()
                tree.update_balances()

            # Left Left Case -> rotate z,x to the right
            #       x                 z
            #      / \              /   \
            #     z   D            y     x
            #    / \         ->   / \   / \
            #   y   C            A   B C   D
            #  / \
            # A   B
            tree.rotate_right()
            tree.update_heights()
            tree.update_balances()

        # Right subtree is larger than left subtree
        if tree.balance < -1:

            # Right Left Case -> rotate x,z to the right
            if tree.node.right.balance > 0:
                #     y               y
                #    / \             / \
                #   A   x           A   z
                #      / \    ->       / \
                #     z   D           B   x
                #    / \                 / \
                #   B   C               C   D
                tree.node.right.rotate_right() # we're in case III
                tree.update_heights()
                tree.update_balances()

            # Right Right Case -> rotate y,x to the left
            #       y                 z
            #      / \              /   \
            #     A   z            y     x
            #        / \     ->   / \   / \
            #       B   x        A   B C   D
            #          / \
            #         C   D
            tree.rotate_left()
            tree.update_heights()
            tree.update_balances()

def update_heights(tree, recursive=True): # update heights for whole tree
    """
    Update tree height

    Tree height is max height of either left or right subtrees +1 for root of the tree
    """
    if tree.node:
        if recursive:
            if tree.node.left:
                tree.node.left.update_heights()
            if tree.node.right:
                tree.node.right.update_heights()

        height = 1 + max(tree.node.left.height, tree.node.right.height)
    else:
        height = -1

def update_balances(tree, recursive=True):
    """
    Calculate tree balance factor

    The balance factor is calculated as follows:
        balance = height(left subtree) - height(right subtree).
    """
    if tree.node:
        if recursive:
            if tree.node.left:
                tree.node.left.update_balances()
            if tree.node.right:
                tree.node.right.update_balances()

        balance = tree.node.left.height - tree.node.right.height
    else:
        balance = 0

def rotate_right(tree):
    """
    Right rotation
        set self as the right subtree of left subree
    """
    new_root = tree.node.left.node
    new_left_sub = new_root.right.node
    old_root = tree.node

    tree.node = new_root
    old_root.left.node = new_left_sub
    new_root.right.node = old_root

def rotate_left(self):
    """
    Left rotation
        set self as the left subtree of right subree
    """
    new_root = tree.node.right.node
    new_left_sub = new_root.left.node
    old_root = tree.node

    tree.node = new_root
    old_root.right.node = new_left_sub
    new_root.left.node = old_root

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


def main():
    """
    creates an AVL tree from an imported data set
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
            height = -1
            balance = 0
        else:
            insert(datatree, data[0], data[1])
            rebalance(datatree)

    result = search(datatree,'8')
    print('the value of 8 is ' + str(result))


if __name__ == '__main__':
    main()
