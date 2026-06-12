"""
# Definition for a Node.

"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #construct deep copy of list, points to brand new nodes
        #mapping of old to new 

        d = {None: None}
        curr = head
        while curr is not None:
            d[curr] = Node(curr.val)
            curr = curr.next 
        
        curr = head
        while curr is not None:
            d[curr].next = d[curr.next]
            d[curr].random = d[curr.random]
            curr = curr.next
        
        curr = head
        
        return d[curr]

        # d = {None: None}

        # curr = head
        # dummy = Node(0)
        # head1 = dummy
        # while curr is not None:
        #     if curr not in d:
        #         n1 = Node(curr.val)
        #         d[curr] = n1
        #         dummy.next = n1
            
        #     else:
        #         dummy.next = d[curr]
            
        #     dummy = dummy.next
            
        #     if curr.next in d:
        #         d[curr].next = d[curr.next]
            
        #     if curr.random in d:
        #         d[curr].random = d[curr.random]
            
        #     curr = curr.next
        
        # return head1.next
        

\