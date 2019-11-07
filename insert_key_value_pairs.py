"""
Main file to compare different data structures for storing key, value pairs
"""
import argparse
import binary_tree

def main():
    """
    test data structures for storing key, value pairs

    Arguments
    ---------
    --datastructure: the datastructure to build storing desired key, value
    pairs. Choose from 'hash', 'binary_tree', or 'avl_tree'.

    --dataset: a CSV file containing lines of key, value pairs to store

    Returns
    -------


    """
    parser = argparse.ArgumentParser(description='Store key, value pairs in '
                                     'data structures',
                                     prog='insert_key_value_pairs')

    parser.add_argument('--datastructure', type=str, help='Name of '
                        "datastructure to use. Choose from 'hash', "
                        "'binary_tree', or 'avl_tree'", required=True)

    parser.add_argument('--dataset', type=str, help='Name of CSV file with key'
                        ', value pairs', required=True)

    args = parser.parse_args()

    datastructure = args.datastructure
    filename = args.dataset

    if datastructure is 'hash':
        # call hash tables submodule
        pass

    if datastructure is 'binary_tree':
        # call binary_tree tree function
        pass

    if datastructure is 'avl_tree':
        # call avl_tree tree function
        pass

    


if __name__ == '__main__':
    main()
