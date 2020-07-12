import sys
import numpy as np

sys.setrecursionlimit(1500)

class Sort:
    array_access_count = 0
    '''
    recursive version of quick sort algorithm
    '''
    def quick_sort_recursive(self, nums, order = 'asc'):
        comparator = lambda x, y: (x <= y)  if (order == 'asc') else (x >= y)
        self.array_access_count = 0
        return self.sort(nums, 0, len(nums) - 1, comparator)

    def sort(self, nums, start, end, comparator):
        if(len(nums) <= 1):
            return nums

        if(start < end):
            pivotPosition = self.partition(nums, start, end, comparator)
            self.sort(nums, start, pivotPosition - 1, comparator)
            self.sort(nums, pivotPosition +1, end, comparator)

        return nums, self.array_access_count

    '''
    iterative version of quick-sort which solves recursion depth issues
    '''
    def quick_sort_iterative(self, nums, order = 'asc'):
        comparator = lambda x, y: (x <= y)  if (order == 'asc') else (x >= y)
        self.array_access_count = 0
        stack = [] 
        stack.append(0)
        stack.append(len(nums) - 1)
        top = 1

        while(len(stack) > 1):
            end = stack.pop()
            start = stack.pop()

            # partition the array based on these values
            pivotPosition = self.partition(nums, start, end, comparator)

            if(pivotPosition - 1 > start):
                stack.append(start)
                stack.append(pivotPosition - 1)
            
            if(pivotPosition + 1 < end):
                stack.append(pivotPosition + 1)
                stack.append(end)
        return nums, self.array_access_count

    '''
    modifies the array such that:
        elements to left of pivot are less than pivot
        elements to right of pivot are greater than pivot
    returns the pivot index
    '''
    def partition(self, nums, start, end, comparator):
        pivot = nums[start]
        startIdx, endIdx = start, end
        while(startIdx < endIdx):
            while(comparator(nums[startIdx], pivot) and startIdx < end):
                startIdx+=1
                self.array_access_count += 1
            while(not comparator(nums[endIdx], pivot) and endIdx > start):
                endIdx-=1
                self.array_access_count += 1
            if(startIdx < endIdx):
                nums[startIdx], nums[endIdx] = nums[endIdx], nums[startIdx]
                self.array_access_count += 2
        nums[endIdx], nums[start] = nums[start], nums[endIdx]
        self.array_access_count += 3
        return endIdx 