class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Put second half into stack
        stack = []
        second = slow.next
        slow.next = None

        while second:
            stack.append(second)
            second = second.next

        # Insert nodes from stack
        curr = head

        while stack:
            temp = curr.next
            curr.next = stack.pop()
            curr.next.next = temp
            curr = temp