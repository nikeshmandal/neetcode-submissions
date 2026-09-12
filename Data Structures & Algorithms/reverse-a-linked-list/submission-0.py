class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        liste = []

        first = head

        while first is not None:
            liste.append(first.val)
            first = first.next

        liste.reverse()

        dummy = ListNode()
        current = dummy

        for i in liste:
            current.next = ListNode(i)
            current = current.next

        return dummy.next