# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #reorder pattern: 0, n, 1, n-1, 2, n-2
        #edge cases: empty, one ele, two ele -> return head 

        slow, fast = head, head

        while fast and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next 
        
        curr = slow.next
        slow.next = None
        prev = None
        
     
        while curr is not None:
            t = curr.next 
            curr.next = prev
            prev = curr
            curr = t 
        
        first = head
        second = prev 

        while second is not None:
            t1 = first.next 
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2 

 
        
        
        



       