class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while (nums[l]<nums[r]):
            if(target>nums[l] and target<nums[r]):
                mid=(l+r)//2

                if(target==nums[mid]):
                    return mid

                mid=(l+r)//2

            elif(nums[mid]<target):
                l=mid+1

            elif(nums[mid]>target):
                r=mid-1

        return -1



        