"""
Main file to compare different data structures for storing key, value pairs
"""
import argparse
import sys
import binary_tree
sys.path.insert(1, './hash-tables-alisoncleonard')
import hash_tables as ht
import time


def main():
    """
    test data structures for storing key, value pairs

    Arguments
    ---------
    --datastructure: the datastructure to build storing desired key, value
    pairs. Choose from 'hash', 'binary_tree', or 'avl_tree'.

    --dataset: a tab-separated txt file containing lines of key, value
    pairs to store

    Returns
    -------


    """
    parser = argparse.ArgumentParser(description='Store key, value pairs in '
                                     'data structures',
                                     prog='insert_key_value_pairs')

    parser.add_argument('--datastructure', type=str, help='Name of '
                        "datastructure to use. Choose from 'hash', "
                        "'binary_tree', or 'avl_tree'", required=True)

    parser.add_argument('--dataset', type=str, help='Name of txt file with key'
                        ', value pairs', required=True)

    args = parser.parse_args()

    datastructure = args.datastructure
    filename = args.dataset

    if datastructure == 'hash':
        # call hash tables submodule
        hashtable = ht.ChainedHash(10000000, ht.hash_functions.h_rolling)
        # measure time to insert all keys in file
        insert_t0 = time.time()
        for line in open(filename, 'r'):
            data = line.rstrip().split('\t')
            hashtable.add(data[0], data[1])
        insert_t1 = time.time()
        # measure time to search for all keys
        search_t0 = time.time()
        for line in open(filename, 'r'):
            data = line.rstrip().split('\t')
            hashtable.search(data[0])
        search_t1 = time.time()
        print('time to insert: ' + str(insert_t1 - insert_t0))
        print('time to search: ' + str(search_t1 - search_t0))

    elif datastructure == 'binary_tree':
        # call binary_tree tree function
        print('initialize binary tree')
        # measure time to insert all keys in file
        insert_t0 = time.time()
        datatree = binary_tree.create_tree(filename)
        insert_t1 = time.time()
        # measure time to search for keys
        search_t0 = time.time()
        result = binary_tree.search(datatree, '8')
        search_t1 = time.time()
        print('the value of 8 is ' + str(result))
        print('time to insert: ' + str(insert_t1 - insert_t0))
        print('time to search: ' + str(search_t1 - search_t0))

    elif datastructure == 'avl_tree':
        # call avl_tree tree function
        pass

    else:
        print('does not recognize datastructure name')


if __name__ == '__main__':
    main()


# python insert_key_value_pairs.py --datastructure 'binary_tree' --dataset 'commasep_testdata.csv'
