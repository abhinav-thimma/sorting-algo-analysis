class Sort:
    def insertion_sort(self, nums, order = 'asc'):
        if(nums == None or len(nums) < 1):
            return nums, 0
        comparator = lambda x, y: (x < y)  if (order == 'asc') else (x > y)
        array_access_count = 0
        for i in range(1, len(nums)):
            j, curr = i-1, nums[i]
            while j>=0 and comparator(curr, nums[j]):
                nums[j+1] = nums[j]
                j = j-1
                array_access_count += 3
            nums[j + 1] = curr
            array_access_count += 3
        return nums, array_access_count

    