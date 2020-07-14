class Sort:
    def cocktail_sort(self, nums, order = 'asc'):
        if(nums == None):
            return None, 0
        array_access_count = 0
        comparator = lambda x, y: (x < y)  if (order == 'asc') else (x > y)
        for i in range(len(nums)):
            for j in range(i, len(nums) - i - 1):
                if(comparator(nums[j+1], nums[j])):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    array_access_count += 4
                else:
                    array_access_count +=2

            for j in range(len(nums) - i - 2, -1 + i, -1):
                if(comparator(nums[j+1], nums[j])):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    array_access_count += 4
                else:
                    array_access_count += 2
        return nums, array_access_count