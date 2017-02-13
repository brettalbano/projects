'''
Misc. utility functions for this implimentation of Erasure Coding
'''

import logging
import EvenOdd_EC
from bitarray import bitarray

def get_EvenOdd_EC():
	list_1 = EvenOdd_EC.List_A
	list_2 = EvenOdd_EC.List_B
	list_3 = EvenOdd_EC.List_C
	list_4 = EvenOdd_EC.List_D
	list_5 = EvenOdd_EC.List_E
	
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
	reverse_device_list = range(len(device_matrix)-1 , -1, -1)
	num_words_in_device = len(device_matrix[0])
	num_devices = len(device_matrix)
	diagonal_list = []
	for diagonal_index in range(num_devices):
		temp_diag_list = []
		word_index = 0
		device_index = diagonal_index
		while len(temp_diag_list) < num_words_in_device:
			temp_diag_list.append(device_matrix[device_index][word_index])
			word_index += 1
			device_index = (device_index-1) % num_devices
		diagonal_list.append(temp_diag_list)
	return diagonal_list

def get_syndrome_array(device_matrix, syndrome_parity):
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
	diagonals_list = get_diagonal_lists(device_matrix)
	syndrome_diagonal = diagonals_list.pop()
	temp_syndrome_array = [ device+[syndrome_parity] for device in diagonals_list]
	return [get_array_parity(device) for device in temp_syndrome_array]

def find_missing_word_diagonal(ec_obj):
	'''
	Will find the diagonal of the device matrix with at most missing one word
	input:
	ec_obj: EvenOdd_EC
	output:
	result_diagonal: list(bool) or bitarray
	'''
	diagonals = get_diagonal_lists(ec_obj.device_array)
	for diag in diagonals:
		down_count = 0
		for word in diag:
			if word is None:
				down_count += 1
		if down_count == 1:
			return diag
	return None
	