class Sort:
    def selection_sort(self, nums, order = 'asc'):
        if(nums == None or len(nums) < 1):
            return nums, 0
        comparator = lambda x, y: (x < y)  if (order == 'asc') else (x > y)
        array_access_count = 0
        for i in range(0, len(nums) - 1):
            min, pos = nums[i], i
            # step: find min in the remaining array and replace with the current element
            for j in range(i + 1, len(nums)):
                if(comparator(nums[j], min)):
                    min, pos = nums[j], j
                    array_access_count += 1
                array_access_count += 1
            nums[i], nums[pos] = nums[pos], nums[i]
            array_access_count += 5
        return nums, array_access_count