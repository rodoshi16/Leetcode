# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        visited = set()

        while fast is not None:
            if fast not in visited:
                visited.add(fast)
                fast = fast.next
            else:
                return fast 
        
        return None
                
            
