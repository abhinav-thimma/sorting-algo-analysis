class Sort:
    def gnome_sort(self, nums, order = 'asc'):
        array_access_count, currIdx = 0, 1
        comparator = lambda x, y: (x < y)  if (order == 'asc') else (x > y)
        while currIdx < len(nums):
            if(comparator(nums[currIdx], nums[currIdx - 1])):
                nums[currIdx], nums[currIdx-1] = nums[currIdx-1], nums[currIdx]
                array_access_count += 2
                i = currIdx -1
                while(i > 0):
                    if(comparator(nums[i], nums[i-1])):
                        nums[i], nums[i-1] = nums[i-1], nums[i]
                        array_access_count+=2
                        i-=1
                    else:
                        break   
                    array_access_count+=2   
            currIdx += 1
        array_access_count += 2
        return nums, array_access_count