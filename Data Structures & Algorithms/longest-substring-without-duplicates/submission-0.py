class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        j = 0
        maximum = 0

        while j < len(s):

            if s[j] not in s[i:j]:
                j += 1
                maximum = max(maximum, j - i)

            else:
                i += 1

        return maximum