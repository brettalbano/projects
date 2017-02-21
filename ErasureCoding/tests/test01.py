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

if __name__ == '__main__':
    main()

