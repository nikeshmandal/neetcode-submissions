class Solution:

    def area(self, heights, l, r):
        height = min(heights[l], heights[r])
        width = r - l
        return height * width

    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        maximum_area = 0

        while l < r:

            current_area = self.area(heights, l, r)

            maximum_area = max(maximum_area, current_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maximum_area