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

import Matrix
import ec_utils

def main():
   device_array = ec_utils.get_Matrix()
   parity_array = ec_utils.get_parities(device_array)
   syndrome_array = ec_utils.get_syndrome_array(device_array, parity_array)

if __name__ == '__main__':
    main()

