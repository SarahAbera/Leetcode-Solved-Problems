class Solution:
    def findCircleNum(self, cnx: List[List[int]]) -> int:
        res=0
        n=len(cnx)
        def dfs(i):
            cnx[i][i]=2
            for j in range(0,n):
                if cnx[i][j]==1:
                    cnx[i][j]=2
                    dfs(j)
        for i in range(0,n):
            if cnx[i][i]==1:
                res+=1
                dfs(i)
        return res
