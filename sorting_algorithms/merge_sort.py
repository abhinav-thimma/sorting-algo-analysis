class Sort:
    array_access_count = 0
    comparator = lambda x, y: (x < y)
    def merge_sort(self, nums, order = 'asc'):
        if(nums == None):
            return None, 0
        self.array_access_count = 0
        self.comparator = lambda x, y: (x < y)  if (order == 'asc') else (x > y)
        return self.sort(nums)

    def sort(self, nums):
        if(len(nums) <= 1):
            return nums
        
        self.array_access_count += len(nums)
        leftArr = self.sort(nums[:int(len(nums)/2)])
        leftArr = leftArr if isinstance(leftArr, list) else leftArr[0]
        rightArr = self.sort(nums[int(len(nums)/2):])
        rightArr = rightArr if isinstance(rightArr, list) else rightArr[0]
        return self.merge_arrs(leftArr, rightArr), self.array_access_count
    
    '''
    merges two sorted arrays into a single sorted array
    '''
    def merge_arrs(self, leftArr, rightArr):
        l, r = 0, 0
        sorted_arr = []
        while(l < len(leftArr) and r < len(rightArr)):
            if(self.comparator(leftArr[l], rightArr[r])):
                sorted_arr.append(leftArr[l])
                l+=1
            else:
                sorted_arr.append(rightArr[r])
                r+=1
            self.array_access_count += 3
        while(l < len(leftArr)):
            sorted_arr.append(leftArr[l])
            l+=1
            self.array_access_count += 1
        while(r < len(rightArr)):
            sorted_arr.append(rightArr[r])
            r+=1
            self.array_access_count += 1
        return sorted_arr