#!/usr/bin/python

from bitarray import bitarray
import os
import sys

def setup_python_path():
    '''
    Sets the working directory to the library directory
    '''
    sys.path.append('../lib')

setup_python_path()

from EvenOdd_EC import EvenOdd_EC
import ec_utils

def main():
	EvenOdd_obj = EvenOdd_EC(ec_utils.get_EvenOdd_EC())
	print EvenOdd_obj
	EvenOdd_obj = EvenOdd_obj.bring_device_down(3)
	print EvenOdd_obj
	print ec_utils.find_missing_word_diagonal(EvenOdd_obj)

if __name__ == '__main__':
    main()

