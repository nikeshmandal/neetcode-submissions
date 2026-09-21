# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        prev=None
        n=n-1
        
        for i in range(n):
            curr=curr.next

        curr.next=curr.next.next

        return head

