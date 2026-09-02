class Solution:
    def isValid(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while(l<r):
            if(l=="(" and r==")"):
                l+=1
                r-=1
            elif(l=="{" and r=="}"):
                l+=1
                r-=1
            elif(l=="[" and r=="]"):
                l+=1
                r-=1
            return True
        return False
        