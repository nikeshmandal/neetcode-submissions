class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print (nums)
        longest=defaultdict(set)

        for i in range(len(nums)):
            if((nums[i]-nums[i-1])==1):
                longest[1].add(nums[i])
        return (len(longest[1])+1)