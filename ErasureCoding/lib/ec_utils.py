'''
Misc. utility functions for this implimentation of Erasure Coding
'''

import logging
import Matrix
from bitarray import bitarray

def get_Matrix():
	list_1 = Matrix.List_A
	list_2 = Matrix.List_B
	list_3 = Matrix.List_C
	list_4 = Matrix.List_D
	list_5 = Matrix.List_E
	
	return [list_1, list_2, list_3, list_4, list_5]

def get_parities(device_matrix):
	'''
	Will take the given device matrix and return an array of parities to each
	corresponding word in each device.
	inputs:
	device_matrix : list(list(bool))
	return:
	parity: list(bool)
	'''
	parity = []
	temp_parity = []
	for word in range(len(device_matrix[0])):
		for device in device_matrix:
			temp_parity.append(device[word])
		parity.append(get_array_parity(temp_parity))
	return parity

def get_array_parity(truth_array):
	'''
	Will take an array of truth values and return True if odd number of
	True's are present and False if even number of True's are present
	input:
	truth_array: list(bool)
	output: bool
	'''
	count = 0
	for truth in truth_array:
		if truth == True:
			count += 1
		else:
			continue
	if count % 2 == 0:
		return False
	else:
		return True

def get_syndrome_parity(device_matrix):
	'''
	Will find the syndrome value from a diagonal in the device_matrix.
	Input:
	device_matrix: list(list(bool))
	Output:
	syndrome_parity: bool
	'''
	diagonal_array = []
	reversed_element_list = range(len(device_matrix[0])-1, -1, -1)
	for device, word in zip(device_matrix,reversed_element_list):
		diagonal_array.append(device[word])
	syndrome_parity = get_array_parity(diagonal_array)
	return syndrome_parity

def get_diagonal_lists(device_matrix):
	'''
	Will find the corresponding diagonals to the device matrix.
	Input:
	device_matrix: list(list(bool))
	Output:
	diagonals_list: list(list(bool))
	'''
	
def get_syndrome_array(device_matrix, parity_array):
	'''
	Will find the syndrome value from a diagonal in the device_matrix.
	It will then use this syndrome value and find the parity of all the
	other diagonals in the device_matrix with the Syndrome.
	Input:
	device_matrix: list(list(bool))
	parity_array: list(bool)
	output:
	synd_array: list(bool)
	'''
	syndrome_parity = get_syndrome_parity(device_matrix)
	diagonals_list = get_diagonal_lists(device_matrix)
	