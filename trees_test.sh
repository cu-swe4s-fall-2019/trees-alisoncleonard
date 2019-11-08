#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
source ssshtest

echo 'testing exception for FileNotFoundError'

run test_find_file python get_column_stats.py --file_name test.txt --column_number 2
assert_in_stdout 'Could not find test.txt'
assert_no_stderr
assert_exit_code 1
