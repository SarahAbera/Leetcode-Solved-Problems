class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for i, p in enumerate(parent):
            graph[p].append(i)

        
        ans = 1
        def dfs(node):
            nonlocal ans

            longest, long2 = 0, 0

            for child in graph[node]:
                path_length = dfs(child)

                if s[child] != s[node]:
                    if path_length > longest:
                        long2 = longest
                        longest = path_length
                    elif path_length > long2:
                        long2 = path_length

            ans = max(ans , longest + long2 + 1)
            return longest + 1

        dfs(0)
        return ans
