class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        while l <= r:

            mid = (l + r) // 2

            total_hours = 0

            for pile in piles:
                total_hours += (pile + mid - 1) // mid

            if total_hours > h:
                # Speed is too slow
                l = mid + 1

            else:
                # Speed works, but maybe we can go slower
                r = mid - 1

        return l