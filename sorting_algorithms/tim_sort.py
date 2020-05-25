import numpy as np

class Sort:
    SPLIT_SIZE = 32
    array_access_count = 0

    def insertion_sort(self, nums, left, right):
        if(left < right):
            for i in range(left + 1, right + 1):
                j, curr = i-1, nums[i]
                self.array_access_count+=1
                while j>=left and nums[j] > curr:
                    nums[j+1] = nums[j]
                    self.array_access_count+=2
                    j = j-1
                nums[j + 1] = curr
                self.array_access_count+=1
    
    def merge(self, nums, left, mid, right):
        left_arr = nums[left:mid]
        right_arr = nums[mid:right+1]
        self.array_access_count+=(right - left + 1)
        merged_arr = []
        l_idx, r_idx, m_idx = 0, 0, 0

        while((l_idx < len(left_arr)) and (r_idx < len(right_arr))):
            if(left_arr[l_idx] <= right_arr[r_idx]):
                merged_arr.append(left_arr[l_idx])
                l_idx+=1
            else:
                merged_arr.append(right_arr[r_idx])
                r_idx+=1
        while(l_idx < len(left_arr)):
            merged_arr.append(left_arr[l_idx])
            l_idx+=1
        
        while(r_idx < len(right_arr)):
            merged_arr.append(right_arr[r_idx])
            r_idx+=1
        self.array_access_count+=2*(right - left + 1)

        nums[left:right+1] = merged_arr

    '''
    memory efficient merge of sorted arrays
    '''
    def merge_in_place(self, nums, left, mid, right):
        left_size = mid - left
        right_size = right - mid

        left_arr = nums[left:mid].copy()
        l_idx, m_idx, r_idx = 0, left, mid

        while((l_idx < len(left_arr)) and (mid <= r_idx <= right)):
            if(left_arr[l_idx] <= nums[r_idx]):
                nums[m_idx] = left_arr[l_idx]
                m_idx+=1
                l_idx+=1
            else:
                nums[m_idx] = nums[r_idx]
                m_idx+=1
                r_idx+=1
        
        while(l_idx < len(left_arr)):
            nums[m_idx] = left_arr[l_idx]
            m_idx+=1
            l_idx+=1
        while(r_idx <= right):
            nums[m_idx] = nums[r_idx]
            r_idx+=1
            m_idx+=1

    def tim_sort(self, nums):
        self.array_access_count = 0
        # sorting sub arrays of SPLIT_SIZE length
        for i in range(0, len(nums), self.SPLIT_SIZE):
            self.insertion_sort(nums, i, min(len(nums)-1, i+self.SPLIT_SIZE-1))

        # merging adjacent subdivided arrays with increasing range
        batch_range = self.SPLIT_SIZE
        while(batch_range < len(nums)):
            for i in range(0, len(nums), 2*batch_range):
                left, right = i, min(i+2*batch_range -1, len(nums)-1)
                mid = left + batch_range
                self.merge_in_place(nums, left, mid, right)
            batch_range*=2
        return nums, self.array_access_count
