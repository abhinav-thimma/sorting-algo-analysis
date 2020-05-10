from bubble_sort import Sort  as BubbleSort
from insertion_sort import Sort  as InsertionSort
from selection_sort import Sort  as SelectionSort
from radix_sort import Sort  as RadixSort
from merge_sort import Sort  as MergeSort
from quick_sort import Sort  as QuickSort
from cocktail_sort import Sort as CocktailSort
from gnome_sort import Sort as GnomeSort
from shell_sort import Sort as ShellSort

import numpy as np 
import time

def check_sorting(nums):
    for i in range(1, len(nums)):
        if(nums[i-1] > nums[i]):
            print('NOT_SORTED')
            return None
    return nums

class ArrayGenerator:
    def __init__(self, min = -10000, max = 10000):
        self.min = min
        self.max = max
        
    '''
    generates arrays with random unordered elements
    '''
    def get_random_arrays(self, no_of_arrays, size_of_array):
        arrays = []
        for i in range(no_of_arrays):
            nums = [np.random.randint(self.min, self.max) for i in range(size_of_array)]
            arrays.append(nums)
        return arrays

    '''
    generates arrays with sorted random elements
    '''
    def get_random_sorted_arrays(self, no_of_arrays, size_of_array):
        arrays = []
        for i in range(no_of_arrays):
            nums = [np.random.randint(self.min, self.min + np.random.randint(0, 50))]
            for pos in range(size_of_array - 1):
                nums.append(np.random.randint(nums[pos], nums[pos] + np.random.randint(0, 50) + 1))
            arrays.append(nums)
        return arrays

    def get_linear_arrays(self, no_of_arrays, size_of_arrays):
        arrays = []
        for i in range(no_of_arrays):
            nums = [num for num in range(0, size_of_arrays)]
            arrays.append(nums)
        return arrays

def compare_sorts(sort_function1, sort_function2):
    arrays = ArrayGenerator().get_random_arrays(1000, 1000)
    
    t = time.process_time()
    for arr in arrays:
        check_sorting(sort_function1(arr))
    t1 = time.process_time()
    for arr in arrays:
        check_sorting(sort_function2(arr))
    t2 = time.process_time()

    print('time for algorithm 1: ' + str(t1 - t))
    print('time for algorithm 2: ' + str(t2 - t1))


def time_sort_algorithms(sort_map):
    arrays = ArrayGenerator().get_random_arrays(100, 1000)
    for name,sort_function in sort_map.items():
        t = time.process_time()
        access_count = 0
        for arr in arrays:
            sorted_arr, count = sort_function(arr.copy())
            access_count += count
            check_sorting(sorted_arr)
        t1 = time.process_time()
        print(f'Time for {name}\t: {str(t1 - t)}\t  Array access count: {str(access_count)}')

def test_sort_algorithm(sort_function, steps):
    for i in range(steps):
        t = time.process_time()
        array = ArrayGenerator().get_random_arrays(1, 100*(10**i))[0]
        sorted_array, access_count = sort_function(array)
        check_sorting(sorted_array)
        t1 = time.process_time()
        print(f'Array size: {len(array)} Array access count: {str(access_count)}  time taken: {str(t1 - t)}')

sort_map = {}
sort_map['selection_sort'] = SelectionSort().selection_sort
sort_map['bubble_sort'] = BubbleSort().bubble_sort
sort_map['insertion_sort'] = InsertionSort().insertion_sort
sort_map['cocktail_sort'] = CocktailSort().cocktail_sort
sort_map['radix_sort'] = RadixSort().radix_sort
sort_map['merge_sort'] = MergeSort().merge_sort
# sort_map['quick_sort_recursive'] = QuickSort().quick_sort_recursive
sort_map['quick_sort_iterative'] = QuickSort().quick_sort_iterative
sort_map['gnome_sort'] = GnomeSort().gnome_sort
sort_map['shell_sort'] = ShellSort().shell_sort

time_sort_algorithms(sort_map)
# test_sort_algorithm(QuickSort().quick_sort, 5)