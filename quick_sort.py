import sys

sys.setrecursionlimit(1500)

class Sort:
    array_access_count = 0
    def quick_sort(self, nums, start, end):
        if(len(nums) <= 1):
            return nums

        if(start < end):
            pivotPosition = self.partition(nums, start, end)
            self.quick_sort(nums, start, pivotPosition - 1)
            self.quick_sort(nums, pivotPosition +1, end)

        return nums, self.array_access_count

    '''
    modifies the array such that:
        elements to left of pivot are less than pivot
        elements to right of pivot are greater than pivot
    returns the pivot index
    '''
    def partition(self, nums, start, end):
        pivot = nums[start]
        startIdx, endIdx = start, end
        while(startIdx < endIdx):
            while(nums[startIdx] <= pivot and startIdx < end):
                startIdx+=1
                self.array_access_count += 1
            while(nums[endIdx] > pivot and endIdx > start):
                endIdx-=1
                self.array_access_count += 1
            if(startIdx < endIdx):
                nums[startIdx], nums[endIdx] = nums[endIdx], nums[startIdx]
                self.array_access_count += 2
        nums[endIdx], nums[start] = nums[start], nums[endIdx]
        self.array_access_count += 3
        return endIdx 