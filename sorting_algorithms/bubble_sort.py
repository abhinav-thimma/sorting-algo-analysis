class Sort:
    def bubble_sort(self, nums, order = 'asc'):
        comparator = lambda x, y: (x < y)  if (order == 'asc') else (x > y)
        array_access_count = 0
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if(comparator(nums[j+1], nums[j])):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    array_access_count+=2
                array_access_count+=2
        return nums, array_access_count
