#!/usr/bin/python
from bitarray import bitarray
import random
import ec_utils

WORD_LENGTH = 4
#List_A = bitarray('0000')
#List_B = bitarray('1010')
#List_C = bitarray('1001')
#List_D = bitarray('0101')
#List_E = bitarray('1111')
   
List_A = [random.choice((True, False)) for x in range(WORD_LENGTH)] 
List_B = [random.choice((True, False)) for x in range(WORD_LENGTH)] 
List_C = [random.choice((True, False)) for x in range(WORD_LENGTH)] 
List_D = [random.choice((True, False)) for x in range(WORD_LENGTH)] 
List_E = [random.choice((True, False)) for x in range(WORD_LENGTH)] 

class EvenOdd_EC():
	'''
	This class will be the full system after all the parities have
	been calculated and added into main.
	'''
	def __init__(self, matrix):
		'''
		Creates a matrix object that contains the devices, words, and parity
		arrays.
		input:
		matrix: list(list(bool)) or bitarray
		'''
	 	self.device_array = matrix
   		self.parity_array = ec_utils.get_parities(self.device_array)
   		self.syndrome = ec_utils.get_syndrome_parity(self.device_array)
   		self.syndrome_array = ec_utils.get_syndrome_array(self.device_array, self.parity_array)

   	def __str__(self):
   		'''
   		When this object gets printed, it prints out the device matrix, parity and syndrome arrays
   		as well as the syndrome itself.
   		'''
   		return_str = ''
   		for device_index in range(len(self.device_array)):
   			return_str += 'Device ' + str(device_index) + ':       ' + str(self.device_array[device_index]) + '\n'
   		return_str += 'Parity Array:   ' + str(self.parity_array) + '\n'
   		return_str += 'Syndrome Array: ' + str(self.syndrome_array) + '\n'
   		return_str += 'Syndrome Parity: ' + str(self.syndrome) + '\n'
   		return return_str

   	def bring_device_down(self, device_num):
   		'''
   		Simulates a device going down and losing the data in that device.
		input:
		device_num: int
		return:
		self: EvenOdd_EC object
   		'''
   		for word_index in range(len(self.device_array[device_num])):
   			self.device_array[device_num][word_index] = None
   		return self