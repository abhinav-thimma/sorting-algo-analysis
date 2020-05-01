class Sort:
    def pad(self, num, maxDigits):
        strNum = str(num)
        if(len(strNum) < maxDigits):
            return '0'*(maxDigits - len(strNum)) + strNum
        return strNum

    def radix_sort(self, nums):
        array_access_count = 0
        # step 1: find the max num
        max = nums[0]
        for j in range(0, len(nums)):
            max = nums[j] if nums[j] > max else max
        array_access_count += (len(nums) + 1)

        # step 2: pad all numbers to contain same no. of digits
        maxDigits = len(str(max))
        nums = [self.pad(num, maxDigits) for num in nums]
        array_access_count += len(nums)
        buckets = [[] for i in range(10)]

        # step 3: sort by bucket
        for passNum in range(1, maxDigits+1):
            for i in range(len(nums)):
                buckets[int(nums[i][-passNum])].append(nums[i])
                array_access_count += 2
            nums = [num for bucket in buckets for num in bucket]
            buckets = [[] for i in range(10)]
        return [int(num) for num in nums], array_access_count