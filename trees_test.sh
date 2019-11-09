#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
source ssshtest


run test_hash python insert_key_value_pairs.py --datastructure 'hash' --dataset 'random_keys.txt' --number_keys 100
assert_in_stdout
assert_no_stderr
assert_exit_code 0

run test_binary python insert_key_value_pairs.py --datastructure 'binary_tree' --dataset 'sorted_keys.txt' --number_keys 1000
assert_in_stdout
assert_no_stderr
assert_exit_code 0

run test_avl python insert_key_value_pairs.py --datastructure 'avl_tree' --dataset 'random_keys.txt' --number_keys 10000
assert_in_stdout
assert_no_stderr
assert_exit_code 0

run test_keys_not_in_table python insert_key_value_pairs.py --datastructure 'binary_tree' --dataset 'keys_not_in_table.txt' --number_keys 100
assert_in_stdout
assert_no_stderr
assert_exit_code 0
