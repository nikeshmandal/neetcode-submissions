class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        second = head
        length = 0

        while second:
            length += 1
            second = second.next

        position = length - n

        if position == 0:
            return head.next

        for _ in range(position - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head