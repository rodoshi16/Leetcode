import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = ListNode(0)
        dummy = head
        count = 0 
        
        heap = []
        for linked in lists:
            if linked is not None: 
                heapq.heappush(heap, (linked.val, count, linked))
                count += 1
        

        while len(heap) > 0:
            node = heapq.heappop(heap)
            dummy.next = node[2]
            dummy = dummy.next 
            if node[2].next is not None:
                heapq.heappush(heap, (node[2].next.val, count, node[2].next))
                count += 1
        
        return head.next
        
        








        