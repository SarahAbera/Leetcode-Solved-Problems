class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # isvalid function for checking ip number is valid or not
        def isvalid(str):
            if (str[0]=="0" and len(str)>1) or int(str)>255:
                return False
            return True

        res=[]
        def back(i,ip,r):
            if i==len(s) and r==0:
                res.append(ip[:-1])
                return
            if i+1<=len(s) and isvalid(s[i:i+1]):
                back(i+1,ip+s[i:i+1]+".",r-1)
            if i+2<=len(s) and isvalid(s[i:i+2]):
                back(i+2,ip+s[i:i+2]+".",r-1)
            if i+3<=len(s) and isvalid(s[i:i+3]):
                back(i+3,ip+s[i:i+3]+".",r-1)
            return res
        return back(0,"",4)
