class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        memo = defaultdict(int)
        def backtrack(arr, operation):
            if (arr,operation) in memo:
                return memo[(arr,operation)]

            if len(arr) == 2:
                return operation * math.gcd(arr[0], arr[1])

            ans = 1
            for i in range(len(arr)):   
                for j in range(i+1, len(arr)):
                    new_gcd = operation * gcd(arr[i], arr[j])
                    temp = list(arr)
                    temp.pop(j)
                    temp.pop(i)

                    ans = max(ans, new_gcd + backtrack(tuple(temp),operation + 1))
            memo[(arr,operation)] = ans
            return memo[(arr,operation)]

        return backtrack(tuple(nums), 1)
                    
