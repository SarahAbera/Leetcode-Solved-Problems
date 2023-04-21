class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.count = 0

        difference = []
        for i in range(len(nums1)):
            difference.append(nums1[i] - nums2[i])

        def merge(left_arr, right_arr):
            ptr = 0
            for index in range(len(left_arr)):
                while ptr < len(right_arr) and left_arr[index]-right_arr[ptr] > diff:
                    ptr +=1
                self.count += len(right_arr) - ptr

            i = 0
            j = 0
            merged = []
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    merged.append(left_arr[i])
                    i += 1
                else:
                    merged.append(right_arr[j])
                    j += 1
            merged.extend(left_arr[i:])
            merged.extend(right_arr[j:])
            return merged

        def divide(difference):
            if len(difference) == 1:
                return difference
            
            l = 0
            r = len(difference) - 1
            mid = (l + r)//2
            left = divide(difference[:mid+1])
            right = divide(difference[mid+1:])

            return merge(left,right)
        divide(difference)
        return self.count
