class Sort:
    def bead_sort(self, nums, order = 'asc'):
        array_access_count = 0
        comparator = lambda x, y: (x < y)  if (order == 'asc') else (x > y)
        while(not self.is_sorted(nums, comparator)):
            i = 0
            while(i < len(nums) - 1):
                if(comparator(nums[i+1], nums[i])):
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    i+=1
                    array_access_count+=2
                array_access_count+=2
                i+=1
        return nums, array_access_count

    def is_sorted(self, nums, comparator):
        for i in range(len(nums) - 1):
            if(comparator(nums[i+1], nums[i])):
                return False
        return True