class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if (char=='('):
                stack.append(")")
            elif (char=='{'):
                stack.append("}")
            elif (char=='['):
                stack.append("]")
            elif not stack or char!=stack.pop():
                return False
        return not stack


"""
  l=0
        r=len(s)-1
        while(l<r):
            if(s[l]=="(" and s[r]==")"):
                l+=1
                r-=1
            elif(s[l]=="{" and s[r]=="}"):
                l+=1
                r-=1
            elif(s[l]=="[" and s[r]=="]"):
                l+=1
                r-=1            return True
return False """
        # This solution isnt optimal it is a stack implementation problem also it doesnt pass the test cases only 2/42 passed
        