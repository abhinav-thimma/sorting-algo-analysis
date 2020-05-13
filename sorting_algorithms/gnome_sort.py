class Sort:
    def gnome_sort(self, nums):
        array_access_count = 0
        currIdx = 1
        while currIdx < len(nums):
            if(nums[currIdx] < nums[currIdx - 1]):
                nums[currIdx], nums[currIdx-1] = nums[currIdx-1], nums[currIdx]
                array_access_count += 2
                i = currIdx -1
                while(i > 0):
                    if(nums[i] < nums[i-1]):
                        nums[i], nums[i-1] = nums[i-1], nums[i]
                        array_access_count+=2
                        i-=1
                    else:
                        break   
                    array_access_count+=2   
            currIdx += 1
        array_access_count += 2
        return nums, array_access_count