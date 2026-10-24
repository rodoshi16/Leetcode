# cache: {key: Node}
#least to most recent
# [A-B-C]

# key is exists - update, remove from old pos, add to tail
# key doesn't exist - 1. if capa, add to end 2.if no, evict and then add 


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None 
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def remove(self, node: Node):
        # del head
        # del tail
        # one node

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        
        if node.prev is None and node.next is None:
            self.head = None
            self.tail = None

    
    def append(self, node: Node):
        #one node
        # prev exists

        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.tail.next, node.prev = node, self.tail
            self.tail = node
        
        node.next = None



class LRUCache:

    def __init__(self, capacity: int):
        if capacity > 0:
            self.capacity = capacity
        self.cache = {}
        self.lru = DoublyLinkedList()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        
        node = self.cache[key]
        self.lru.remove(node)
        self.lru.append(node)
        return node.value

        
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.lru.remove(node)
            self.lru.append(node)
        else:
            node = Node(key, value)
            if len(self.cache) < self.capacity:
                self.cache[key] = node
                self.lru.append(node)
            else:
                lru = self.lru.head
                del self.cache[lru.key]

                self.lru.remove(lru)

                self.cache[key] = node
                self.lru.append(node)

        
              
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)