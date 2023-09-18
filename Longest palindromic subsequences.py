class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        def palindrome(l , r):
            if (l,r) in dp:
                return dp[(l,r)]

            if l > r:
                return 0
            if l == r:
                return 1

            if s[l] == s[r]:
                dp[(l,r)] = 2 + palindrome(l+1, r-1)
                return dp[(l,r)]
                
            dp[(l,r)] =  max(palindrome(l+1,r), palindrome(l,r-1))
            return dp[(l,r)]

        return palindrome(0,len(s) - 1)
