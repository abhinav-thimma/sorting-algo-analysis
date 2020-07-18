class Sort:
    def shell_sort(self, nums, order = 'asc'):
        if(nums == None or len(nums) < 1):
            return nums, 0
        array_access_count = 0
        comparator = lambda x, y: (x < y)  if (order == 'asc') else (x > y)
        gap = int(len(nums)/2)
        while(gap >= 1):
            for j in range(gap, len(nums)):
                for i in range(j - gap, -1, -gap):
                    if(comparator(nums[i], nums[i+gap])):
                        break
                    else:
                        nums[i], nums[i+gap] = nums[i+gap], nums[i]
                        array_access_count += 2
                    array_access_count+=2
            gap = int(gap/2)
        return nums, array_access_count