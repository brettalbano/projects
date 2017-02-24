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
    print 'Diagonal lists: ' + str(ec_utils.get_diagonal_lists(EvenOdd_obj.device_array))
    EvenOdd_obj = EvenOdd_obj.bring_device_down(2)
    EvenOdd_obj = EvenOdd_obj.bring_device_down(1)
    print EvenOdd_obj
    print 'Diagonal lists: ' + str(ec_utils.get_diagonal_lists(EvenOdd_obj.device_array))
    print EvenOdd_obj.decode_missing_devices()
    print 'Diagonal Lists: ' + str(ec_utils.get_diagonal_lists(EvenOdd_obj.device_array))

if __name__ == '__main__':
    main()

