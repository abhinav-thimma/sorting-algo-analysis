class Sort:
    def bubble_sort(self, nums):
        array_access_count = 0
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if(nums[j] > nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    array_access_count+=4
                else:
                    array_access_count+=2
        return nums, array_access_count
