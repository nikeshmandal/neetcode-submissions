# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        first=head
        second=head
        x=0
        nn=1

        while (second and second.next):
            first=first.next
            second=second.next.next
            x+=1

        x=x*2
        x=x-n


        
        
        while nn<x:
            curr=curr.next
            nn+=1
        
        if(curr is not None):
            curr.next=curr.next.next

        return head

