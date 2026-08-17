"""class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print (nums)
        longest=defaultdict(set)

        for i in range(len(nums)):
            if((nums[i]-nums[i-1])==1):
                longest[1].add(nums[i])
        return (len(longest[1])+1)
        """
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()

        longest = 1
        current = 1

        for i in range(1, len(nums)):

            if nums[i] == nums[i-1]:
                continue

            if nums[i] == nums[i-1] + 1:
                current += 1
            else:
                current = 1

            longest = max(longest, current)

        return longest"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:

            # Only start counting if num is the beginning
            # of a consecutive sequence
            if num - 1 not in num_set:

                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest