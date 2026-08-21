class Solution:
    def trap(self, height: List[int]) -> int:
        s=len(height)
        left=[0]*s
        right=[0]*s
        result=0
        left[0]=height[0]
        for i in range(1,s):
            left[i]=max(left[i-1],height[i])

        right[s-1]=height[s-1]
        for j in range(s-2,-1,-1):
            right[j]=max(right[j+1],height[j])

        for x in range(1,s-1):
            result+=(min(left[x],right[x])- height[x])

        return result

"""        result=0
        for i in range(1,len(height)):
            left=height[i]
            for j in range(i):
                left=max(left,height[j])
            right=height[i]
            for j in range(i+1,len(height)):
                right=max(right,height[j])

            result+=(min(left,right)-height[i])
        return result """
        # by 0(n^2) iterating throught the list and finding the left and right max of each index and finding the area to store by subtracting right- left for each i it works but get this error so not for exams --Time Limit Exceeded. You may have an infinite loop or your code is too inefficient.

        