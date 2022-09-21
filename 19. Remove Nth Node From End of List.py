# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res=head
        if res.next==None and n==1:
            res=None
            return head
        if(res.next):
            for i in range(0,n):
                res=res.next  
            if(res.next.next):
                temp=res.next.next
                res.next=temp
            else:
                res.next=None
        return head
