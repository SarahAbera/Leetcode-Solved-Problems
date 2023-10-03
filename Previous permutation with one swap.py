class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 2, -1, -1):
            max_index = i + 1
            for j in range(i+1, len(arr)):
                if arr[max_index] < arr[j] < arr[i]:
                    max_index = j

            if arr[max_index] < arr[i]:
                arr[max_index], arr[i] = arr[i], arr[max_index]
                break

        return arr
        
