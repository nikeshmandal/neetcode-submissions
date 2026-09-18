class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr = head
        seen = set()

        while curr:

            if curr in seen:
                return True

            seen.add(curr)
            curr = curr.next

        return False