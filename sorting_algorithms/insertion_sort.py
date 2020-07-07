class Sort:
    def insertion_sort(self, nums):
        array_access_count = 0
        for i in range(1, len(nums)):
            j, curr = i-1, nums[i]
            while j>=0 and nums[j] > curr:
                nums[j+1] = nums[j]
                j = j-1
                array_access_count += 3
            nums[j + 1] = curr
            array_access_count += 3
        return nums, array_access_count

    