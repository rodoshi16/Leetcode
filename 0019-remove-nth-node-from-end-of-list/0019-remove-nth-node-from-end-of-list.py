# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0
        i = 0 
        while curr is not None:
            l += 1 
            curr = curr.next 
        if l == 1 and n == 1:
            return None
        
        curr = head
        while curr.next is not None:
            if i == l-n:
                head = curr.next
            elif  i+1 == l-n:
                curr.next = curr.next.next 
                return head
            else:
                curr = curr.next
            i += 1
        
        return head
        
    
        
