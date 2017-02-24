#!/usr/bin/python
from bitarray import bitarray
import random
import ec_utils

WORD_LENGTH = 4
#List_A = [0, 0, 0, 0]
#List_B = [1, 0, 1, 0]
#List_C = [1, 0, 1, 1]
#List_D = [0, 1, 0, 1]
#List_E = [1, 1, 1, 1]
#lists = [List_A, List_B, List_C, List_D, List_E]
# List_A = [0, 0, 0, 0, 1]
# List_B = [1, 0, 1, 0, 0]
# List_C = [1, 0, 1, 1, 1]
# List_D = [0, 1, 0, 1, 0]
# List_E = [1, 1, 1, 1, 1]
# List_F = [0, 1, 1, 1, 1]
# lists = [List_A, List_B, List_C, List_D, List_E, List_F]
'''
   		0 1 1 0 1	
   		0 0 0 1 1
   		0 1 1 0 1
   		0 0 1 1 1
'''
List_A = [random.choice((True, False)) for x in range(WORD_LENGTH)] 
List_B = [random.choice((True, False)) for x in range(WORD_LENGTH)] 
List_C = [random.choice((True, False)) for x in range(WORD_LENGTH)] 
List_D = [random.choice((True, False)) for x in range(WORD_LENGTH)] 
List_E = [random.choice((True, False)) for x in range(WORD_LENGTH)]
lists = [List_A, List_B, List_C, List_D, List_E]

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

    def find_missing_word_diagonal(self):
        '''
        Will find the diagonals of the device matrix with at most missing one word
        input:
        ec_obj: EvenOdd_EC
        output:
        result_diagonal: (list(bool) or bitarray, int)
        '''
        diagonals = ec_utils.get_diagonal_lists(self.device_array)
        for diag in diagonals:
            down_count = 0
            for word in diag:
                if word is None:
                    down_count += 1
            if down_count == 1:
                return diag, diagonals.index(diag)
        return None

    def find_missing_single_word_horizontal(self):
        '''
        Will find a list of words that are the same index in each device that is
        only missing one value, i.e. only one value is None.
        input:
            self: EvenOdd_EC object
        output:
            temp_word_array: list(bool)
            word_index: int
            OR None
        '''
        num_devices = len(self.device_array)
        num_words = len(self.parity_array)
        for word_index in range(num_words):
            none_count = 0
            temp_word_array = []
            for device_index in range(num_devices):
                temp_word = self.device_array[device_index][word_index]
                temp_word_array.append(temp_word)
                if temp_word is None:
                    none_count += 1
            if none_count == 1:
                return temp_word_array, word_index
        return None

    def decode_missing_devices(self):
        '''
        Will find the diagonals with missing words and decode it from the diagonal
        missing only one word and to continue until totally finished.
        input:
        self: EvenOdd_EC object
        output:
        self: EvenOdd_EC object
        '''
        while self.any_words_missing():
            while self.find_missing_word_diagonal() is not None:
                diagonal, d_index = self.find_missing_word_diagonal()
                d_decoded_list = self.decode_missing_word(diagonal, self.syndrome_array[d_index])
                self = self.edit_diagonal_list(d_index, d_decoded_list)
            while self.find_missing_single_word_horizontal() is not None:
                horizontal, h_index = self.find_missing_single_word_horizontal()
                h_decoded_list = self.decode_missing_word(horizontal, self.parity_array[h_index])
                self = self.edit_horizontal_list(h_index, h_decoded_list)
        return self

    def decode_missing_word(self, data_list, parity):
        '''
        This function will xor the list and the parity bit to find the value where
        None is located. The data_list must only have one word being None to complete
        or else it will not be able to decode.
        input:
            data_list: list(bool)
            parity: bool
        output:
            decoded_list: list(bool)
        '''
        none_index = data_list.index(None)
        data_list[none_index] = parity
        missing_word = ec_utils.get_array_parity(data_list)
        data_list[none_index] = missing_word
        return data_list

    def edit_diagonal_list(self, diagonal_index, list_to_copy):
        '''
        This function will find the diagonal that needs to be edited in the object,
        and then copy the words in the given list to that object.
        inputs:
            diagonal_index: int
            list_to_copy: list(bool)
        output:
            self: EvenOdd_EC object
        '''
        num_words_in_device = len(self.device_array[diagonal_index])
        num_devices = len(self.device_array)
        device_index = diagonal_index
        for word_index in range(num_words_in_device):
            self.device_array[device_index][word_index] = list_to_copy[word_index]
            device_index = (device_index-1) % num_devices
        return self

    def edit_horizontal_list(self, word_index, list_to_copy):
        '''
        This function will replace the word at word_index on each device with the 
        corresponding value in list_to_copy.
        inputs:
            word_index: int
            list_to_copy: list(bool)
        outputs:
            self: EvenOdd_EC object
        '''
        num_devices = len(self.device_array)
        for device_index in range(num_devices):
            self.device_array[device_index][word_index] = list_to_copy[device_index]
        return self

    def any_words_missing(self):
        '''
        This function will determine if there are words still missing
        in the device array.
        input:
            self: EvenOdd_EC object
        output:
            return bool True if words missing, False if complete
        '''
        for device in self.device_array:
            for word in device:
                if word is None:
                    return True
        return False
