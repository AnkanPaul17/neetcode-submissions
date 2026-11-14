# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0
        curr=head
        while curr is not None:
            c+=1
            curr=curr.next
        new_n=c-n+1
        if new_n==1:
            head=head.next
            return head
        new_c=0
        final=head
        while final is not None:
            new_c+=1
            if new_c==new_n-1:
                final.next=final.next.next
            final=final.next
        return head
