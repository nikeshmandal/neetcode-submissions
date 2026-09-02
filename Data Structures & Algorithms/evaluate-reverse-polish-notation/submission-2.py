from collections import defaultdict
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stacka=[]

        for c in range(len(tokens)):
            if (tokens[c] == '+'):
                b=stacka.pop()
                d=stacka.pop()
                stacka.append(d+b)
            elif (tokens[c] == '-'):
                b=stacka.pop()
                d=stacka.pop()
                stacka.append(d-b)
            elif (tokens[c] == '*'):
                b=stacka.pop()
                d=stacka.pop()
                stacka.append(d*b)
            elif (tokens[c] == '/'):
                b=stacka.pop()
                d=stacka.pop()
                stacka.append(d//b)
            
            else:
                stacka.append(int(tokens[c]))

        return int(stacka[0])


