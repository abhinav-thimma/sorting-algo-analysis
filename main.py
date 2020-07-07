from array_generator import ArrayGenerator

from sorting_algorithms.bubble_sort import Sort  as BubbleSort
from sorting_algorithms.insertion_sort import Sort  as InsertionSort
from sorting_algorithms.selection_sort import Sort  as SelectionSort
from sorting_algorithms.radix_sort import Sort  as RadixSort
from sorting_algorithms.merge_sort import Sort  as MergeSort
from sorting_algorithms.quick_sort import Sort  as QuickSort
from sorting_algorithms.cocktail_sort import Sort as CocktailSort
from sorting_algorithms.gnome_sort import Sort as GnomeSort
from sorting_algorithms.shell_sort import Sort as ShellSort
from sorting_algorithms.tree_sort import Sort as TreeSort
from sorting_algorithms.tim_sort import Sort as TimSort

from data import mongo_setup
import services.data_service as svc

import time

'''
This method checks if an array is sorted correctly (ascending order)
Inputs:     nums: array to check sorting on
'''
def check_sorting(nums):
    for i in range(1, len(nums)):
        if(nums[i-1] > nums[i]):
            print('NOT_SORTED')
            return None
    return nums

'''
This function is used to compare two sorting algorithms
Inputs:     sort_function_1: first sort_function reference
            sort_function_2: second sort_function reference
'''
def compare_sorts(sort_function1, sort_function2):
    arrays = ArrayGenerator().get_random_arrays(1000, 1000)
    
    t = time.process_time()
    for arr in arrays:
        check_sorting(sort_function1(arr.copy())[0])
    t1 = time.process_time()
    print('time for algorithm 1: ' + str(t1 - t))

    for arr in arrays:
        check_sorting(sort_function2(arr.copy())[0])
    t2 = time.process_time()
    print('time for algorithm 2: ' + str(t2 - t1))

'''
This function is an extrapolation of compare_sorts and allows to runs different sorting algorithms at once
Inputs:     sort_map:  {'sorting_algorithm_name' : sort_function, ..}
'''
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

'''
This function is used to test a single sorting algorithm for several steps
Inputs:     sort_function:  sort_function reference
            steps:  number of times the sorting process must be repeated
'''
def test_sort_algorithm_raw(sort_function, steps):
    for i in range(steps):
        t = time.process_time()
        array = ArrayGenerator().get_random_arrays(1, 100*(10**i))[0]
        sorted_array, access_count = sort_function(array)
        check_sorting(sorted_array)
        t1 = time.process_time()
        print(f'Array size: {len(array)} Array access count: {str(access_count)}  time taken: {str(t1 - t)}')

'''
This function tests a sort function with different kinds of random arrays
Inputs:     sort_function: sort_function reference
            array_gen_map: {'array_type': array_generator_function}
'''
def test_sort_algorithm_with_generated_arrays(sort_function, array_gen_map):
    for name, array_generator in array_gen_map.items():
        arrays = array_generator(10, 1000)
        t = time.process_time()
        access_count = 0
        for arr in arrays:
            sorted_arr, count = sort_function(arr.copy())
            access_count += count
            check_sorting(sorted_arr)
        t1 = time.process_time()
        print(f'Time for {name}\t: {str(t1 - t)}\t  Array access count: {str(access_count)}')

'''
This function stores the results of combination of sort_function and array_generator in DB
Inputs:     sort_map: {'sorting_algorithm_name' : sort_function, ..}
            array_gen_map: {'array_type': array_generator_function}
'''       
def store_results(sort_map, array_gen_map):
    # setting the mongo db connection
    mongo_setup.global_init()
    # iterating over each sort and array generator 
    for sort_name, sort_function in sort_map.items():
        sort_list = []
        for array_type, array_generator in array_gen_map.items():
            arrays = array_generator(1000, 1000)
            # time difference in nano seconds
            t = time.process_time() * (10**9)
            access_count = 0
            for arr in arrays:
                sorted_arr, count = sort_function(arr.copy())
                access_count += count
                check_sorting(sorted_arr)
            t1 = time.process_time() * (10**9)

            array = svc.create_array(arrays, array_type)
            sort = svc.create_sort(array, float(t1 - t), access_count)
            sort_list.append(sort)
            print(f'the time taken for {sort_name} using {array_type} arrays = {float(t1-t)}')
        # storing the results in db
        sorttime = svc.create_sort_time(sort_name, sort_list)

def driver():
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
    sort_map['tree_sort'] = TreeSort().tree_sort
    sort_map['tim_sort'] = TimSort().tim_sort

    array_gen_map = {}
    array_gen_map['random'] = ArrayGenerator().get_random_arrays
    # array_gen_map['random_sorted'] = ArrayGenerator().get_random_sorted_arrays
    array_gen_map['linear'] = ArrayGenerator().get_linear_arrays

    # time_sort_algorithms(sort_map)
    # test_sort_algorithm_raw(TimSort().tim_sort, 5)
    # test_sort_algorithm_with_generated_arrays(TimSort().tim_sort, array_gen_map)
    # compare_sorts(QuickSort().quick_sort_iterative, TimSort().tim_sort)
    store_results(sort_map, array_gen_map)

# driver()
# mongo_setup.global_init()
# print(svc.get_data_for_algo('selection_sort'))