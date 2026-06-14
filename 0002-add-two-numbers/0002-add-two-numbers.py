# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #input: linked lists 
        #empty, diff lengths, floats, int 

        #idea: traverse 
        # 52 % 10

        curr1 = l1
        curr2 = l2 
        dummy = ListNode(0)
        head1 = dummy
        c = 0 

        while curr1 or curr2:
            if curr1 is None:
                x = 0 
            else:
                x = curr1.val
            if  curr2 is None:
                y = 0
            else:
                y = curr2.val
            

            s = x + y + c
            if s >= 10:
                c = s // 10

            else:
                c = 0 
            n = s % 10 

            dummy.next = ListNode(n)
            if curr1 is not None: 
                curr1 = curr1.next
            if curr2 is not None:
                curr2 = curr2.next

            dummy = dummy.next
        
        if c > 0:
            dummy.next = ListNode(c)

        
        return head1.next
    