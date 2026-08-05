class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.x,self.y=0,0
        if len(s)!=len(t):
            return False
        for i in (range(len(s))):
            self.x+=ord(s[i])**2
            self.y+=ord(t[i])**2
        if(self.x==self.y):
            return True

        else:
            return False 
