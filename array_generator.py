import numpy as np

class ArrayGenerator:
    def __init__(self, min: int = -10000, max: int = 10000):
        self.min = min
        self.max = max
        
    '''
    generates arrays with random unordered elements
    '''
    def get_random_arrays(self, no_of_arrays: int, size_of_array: int):
        arrays = []
        for i in range(no_of_arrays):
            nums = [np.random.randint(self.min, self.max) for i in range(size_of_array)]
            arrays.append(nums)
        return arrays

    '''
    generates arrays with sorted random elements
    '''
    def get_random_sorted_arrays(self, no_of_arrays: int, size_of_array: int):
        arrays = []
        for i in range(no_of_arrays):
            nums = [np.random.randint(self.min, self.min + np.random.randint(0, 50))]
            for pos in range(size_of_array - 1):
                nums.append(np.random.randint(nums[pos], nums[pos] + np.random.randint(0, 50) + 1))
            arrays.append(nums)
        return arrays

    '''
    generates arrays with linear spacing
    '''
    def get_linear_arrays(self, no_of_arrays: int, size_of_arrays: int, order = 'ASC'):
        increment = 1 if order == 'ASC' else -1
        single_array = [num for num in range(0, increment * size_of_arrays, increment)]
        arrays= [single_array.copy() for i in range(0, no_of_arrays)]
        return arrays