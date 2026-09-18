class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2

        dummy = ListNode()
        prev = dummy

        while curr1 and curr2:

            if curr1.val <= curr2.val:
                new = ListNode(curr1.val)
                prev.next = new
                prev = new
                curr1 = curr1.next

            else:
                new = ListNode(curr2.val)
                prev.next = new
                prev = new
                curr2 = curr2.next

        if curr1:
            prev.next = curr1

        if curr2:
            prev.next = curr2

        return dummy.next