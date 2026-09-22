class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        if target not in nums:
            return -1

        while(l<r):
            mid=(l+r)//2
            if(target==nums[mid]):
                return (nums.index(mid))

            elif(nums[mid]<target):
                l=mid+1

            elif(nums[mid]>target):
                r=mid-1

            return (nums.index(mid))



        