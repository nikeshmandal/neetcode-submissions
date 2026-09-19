class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # =========================================================
        # APPROACH 1: O(1) EXTRA SPACE
        # Find middle → Reverse second half → Merge
        # =========================================================

        # 1. Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # prev = head of reversed second half
        first = head
        second = prev

        # 3. Merge the two halves
        while second.next:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


        # =========================================================
        # APPROACH 2: STACK
        # Find middle → Store second half in stack → Merge
        #
        # Time:  O(n)
        # Space: O(n)
        # =========================================================

        '''
        # Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Store second half in stack
        stack = []

        second = slow.next

        # Break the list into two halves
        slow.next = None

        # Put second half nodes into stack
        while second:
            stack.append(second)
            second = second.next

        # Merge first half with reversed second half
        curr = head

        while stack:

            # Save the original next node
            temp = curr.next

            # Take the last node from second half
            curr.next = stack.pop()

            # Connect it back to the first half
            curr.next.next = temp

            # Move to the next node in first half
            curr = temp
        '''