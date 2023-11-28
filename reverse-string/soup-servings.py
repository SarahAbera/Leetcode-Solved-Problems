class Solution:
    def soupServings(self, n: int) -> float:
        if(n>4800):
            return 1
        def A_empty(A,B,i,d):
            if (A,B) in d:
                return d[(A,B)]
            if A<=0 and B<=0:
                return i/2
            elif A<=0:
                return i
            elif B<=0:
                return 0
            else:
                total=0
                i*=1/4
                total+=A_empty(A-100,B,i,d)
                total+=A_empty(A-75,B-25,i,d)
                total+=A_empty(A-50,B-50,i,d)
                total+=A_empty(A-25,B-75,i,d)
                # i/=1/4
                d[(A,B)]=total
                return total
        return A_empty(n,n,1,dict())

                