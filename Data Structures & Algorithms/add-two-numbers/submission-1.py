# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        num1=0
        i=0
        while curr1 is not None:
            num1+=curr1.val*(10**i)
            i+=1
            curr1=curr1.next
        curr2=l2
        num2=0
        j=0
        while curr2 is not None:
            num2+=curr2.val*(10**j)
            j+=1
            curr2=curr2.next
        num=num1+num2
        head=ListNode()
        curr=head
        if num==0:
            return ListNode(0)
        while num>0:
            curr.next=ListNode(num%10)
            num=num//10
            curr=curr.next
        return head.next
