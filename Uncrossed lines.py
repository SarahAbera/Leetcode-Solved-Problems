class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(idx1,idx2):
            if idx1 >= len(nums1) or idx2 >= len(nums2):
                return 0

            if nums1[idx1] == nums2[idx2]:
                return 1 + dp(idx1 + 1, idx2 + 1)
            else:
                return max(dp(idx1 + 1, idx2), dp(idx1, idx2 + 1))
                
        return dp(0,0)
