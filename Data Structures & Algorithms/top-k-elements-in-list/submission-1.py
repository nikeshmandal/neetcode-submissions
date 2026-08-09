from collections import Counter,defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        nums.sort()
        number_of_items={}
        for i in nums:
            number_of_items[i] = number_of_items.get(i, 0) + 1

        sorted_items = sorted(number_of_items.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]
        