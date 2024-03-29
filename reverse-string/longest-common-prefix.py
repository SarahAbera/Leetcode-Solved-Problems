class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        length = []
        for string in strs:
            length.append(len(string))

        iterator = min(length)
        idx = 0

        flag = False
        ans = ""
        for idx in range(iterator):
            for i in range(len(strs) - 1):
                if i + 1 == len(strs) - 1 and strs[i][idx] == strs[i+1][idx]:
                    ans += (strs[i][idx])
                    continue

                if strs[i][idx] != strs[i+1][idx]:
                    flag = True
                    break

                elif strs[i][idx] == strs[i+1][idx]:
                    continue
            if flag:
                break
        
        return ans
