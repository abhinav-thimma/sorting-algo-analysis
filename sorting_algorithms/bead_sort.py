class Sort:
    def bead_sort(self, nums):
        array_access_count = 0
        while(not self.is_sorted(nums)):
            i = 0
            while(i < len(nums) - 1):
                if(nums[i] > nums[i+1]):
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    i+=1
                    array_access_count+=2
                array_access_count+=2
                i+=1
        return nums, array_access_count

    def is_sorted(self, nums):
        for i in range(len(nums) - 1):
            if(nums[i] > nums[i+1]):
                return False
        return True

print(Sort().bead_sort([5,2,1,3,1]))