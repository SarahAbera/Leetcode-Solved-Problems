class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        self.count = 0
        def merge(left_arr, right_arr):
            l = 0
            r = 0
            
            while l < len(left_arr):
                
                while r < len(right_arr) and left_arr[l] > (2 * right_arr[r]):
                    r += 1
                
                self.count += r
                l += 1

            k = 0
            l = 0
            mergedArray = []
            while k < len(left_arr) and l < len(right_arr):
                if left_arr[k] > right_arr[l]:
                    mergedArray.append(right_arr[l])
                    l += 1
                    
                else:
                    mergedArray.append(left_arr[k])
                    k += 1
                    
            mergedArray.extend(right_arr[l:])
            mergedArray.extend(left_arr[k:])

            return mergedArray

        def divide(arr):
            if len(arr) == 1:
                return arr

            left = 0
            right = len(arr) - 1
            mid = (left + right) // 2

            arr_left = divide(arr[:mid+1])
            arr_right = divide(arr[mid+1:])

            return merge(arr_left,arr_right)

        divide(nums)
        return self.count
