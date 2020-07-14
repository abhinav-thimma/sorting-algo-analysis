'''
to run tests use `python -m unittest tests.test_sorts` from root folder
'''

import unittest

import numpy as np

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

class TestSorts(unittest.TestCase):
    def is_sorted(self, nums, order = 'asc'):
        comparator = lambda x, y: (x > y)  if (order == 'asc') else (x < y)
        for i in range(1, len(nums)):
            if(comparator(nums[i-1], nums[i])):
                print('NOT_SORTED')
                return None
        return nums
    
    def get_sort_map(self):
        sort_map = {}
        sort_map['selection_sort'] = SelectionSort().selection_sort
        sort_map['bubble_sort'] = BubbleSort().bubble_sort
        sort_map['insertion_sort'] = InsertionSort().insertion_sort
        sort_map['cocktail_sort'] = CocktailSort().cocktail_sort
        # sort_map['radix_sort'] = RadixSort().radix_sort
        sort_map['merge_sort'] = MergeSort().merge_sort
        sort_map['quick_sort_recursive'] = QuickSort().quick_sort_recursive
        sort_map['quick_sort_iterative'] = QuickSort().quick_sort_iterative
        sort_map['gnome_sort'] = GnomeSort().gnome_sort
        sort_map['shell_sort'] = ShellSort().shell_sort
        sort_map['tree_sort'] = TreeSort().tree_sort
        sort_map['tim_sort'] = TimSort().tim_sort
    
        return sort_map

    def test_sort_null(self):
        sort_map = self.get_sort_map() 

        for key, sort_function in sort_map.items():
            print(f'testing null array for {key}')
            for i in range(1000):
                arr = None
                self.assertEqual(sort_function(arr), (None, 0))
                self.assertEqual(sort_function(arr, order = 'asc'), (None, 0))
                self.assertEqual(sort_function(arr, order = 'desc'), (None, 0))
    
    def test_sort_empty(self):
        sort_map = self.get_sort_map() 

        for key, sort_function in sort_map.items():
            print(f'testing empty array for {key}')
            for i in range(1000):
                arr = []
                self.assertEqual(sort_function(arr), ([], 0))
                self.assertEqual(sort_function(arr, order = 'asc'), ([], 0))
                self.assertEqual(sort_function(arr, order = 'desc'), ([], 0))

    def test_sort(self):
        sort_map = self.get_sort_map()

        for key, sort_function in sort_map.items():
            print(f'testing random array for {key}')
            for i in range(1000):
                arr = np.random.randint(-1000, 1000, size = 100).tolist()
                self.assertEqual(sort_function(arr.copy())[0], sorted(arr))
                self.assertEqual(sort_function(arr.copy(), order = 'asc')[0], sorted(arr))
                self.assertEqual(sort_function(arr.copy(), order = 'desc')[0], sorted(arr)[::-1])

if __name__ == '__main__':
    unittest.main()