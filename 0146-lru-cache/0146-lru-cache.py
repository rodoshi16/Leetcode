class Node:

    def __init__(self, key, val: int):
        self.val = val
        self.prev = None
        self.next = None
        self.key = key
    

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

class LRUCache:

    def __init__(self, capacity: int):
        if capacity > 0:
            self.capacity = capacity
        
        self.cache = {}
        self.recent = {}
        self.linked = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        
        if node != self.linked.tail:

            if node == self.linked.head:
                self.linked.head = node.next
                self.linked.head.prev = None
            else:
                node.prev.next, node.next.prev = node.next, node.prev

            self.linked.tail.next, node.prev  = node, self.linked.tail
            self.linked.tail = node

        
        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            if node != self.linked.tail:

                if node == self.linked.head:
                    self.linked.head = node.next
                    self.linked.head.prev = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev

                node.prev = self.linked.tail
                node.next = None
                self.linked.tail.next = node
                self.linked.tail = node

            return

        node = Node(key, value)
        self.cache[key] = node

        if self.linked.head is None:
            self.linked.head = node
            self.linked.tail = node
        else:
            node.prev = self.linked.tail
            self.linked.tail.next = node
            self.linked.tail = node

        if len(self.cache) > self.capacity:
            old = self.linked.head

            if old.next is None:
                self.linked.head = None
                self.linked.tail = None
            else:
                self.linked.head = old.next
                self.linked.head.prev = None

            del self.cache[old.key]


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)