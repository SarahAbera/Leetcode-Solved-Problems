class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)
        i,j = 0,1
        while j < len(needle):
            if needle[i] == needle[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            elif i == 0:
                j += 1
            else:
                i = lps[i-1]

        needle_i, str_i = 0, 0
        while str_i < len(haystack):
            if needle[needle_i] == haystack[str_i]:
                needle_i += 1
                str_i += 1 
            elif needle_i == 0:
                str_i += 1 
            else:
                needle_i = lps[needle_i - 1]
            if needle_i == len(needle):
                return str_i - needle_i
            
        return -1
            
        


        
