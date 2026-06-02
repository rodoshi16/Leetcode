# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head


        slow = None
        fast = head 

        while fast and fast.next is not None:
            if slow is None:
                slow = head
            else:
                slow = slow.next 
            fast = fast.next.next
        
        return slow.next
        