class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.counter = 1

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def remove(self, node: Node):
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
        
        node.prev = None    
        node.next = None
    
    def append(self, node: Node):
        if self.tail is None:
            self.head, self.tail = node, node
        
        else:
            self.tail.next, node.prev = node, self.tail
            self.tail = node
        
        node.next = None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.cache = {}
        self.freq = {1: DoublyLinkedList()}
        self.lfu = 1 
     

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        
        node = self.cache[key]
        self.freq[node.counter].remove(node)
        
        if self.freq[node.counter].head is None:
            del self.freq[node.counter]

            if node.counter == self.lfu:
                self.lfu += 1
        
        node.counter += 1 
        if node.counter not in self.freq:
            self.freq[node.counter] = DoublyLinkedList()
        self.freq[node.counter].append(node)

        return node.value
       
    

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.freq[node.counter].remove(node)
        
            if self.freq[node.counter].head is None:
                del self.freq[node.counter]

                if node.counter == self.lfu:
                    self.lfu += 1
            
            node.counter += 1 
            if node.counter not in self.freq:
                self.freq[node.counter] = DoublyLinkedList()
            self.freq[node.counter].append(node)
        else:

            if len(self.cache) < self.capacity:
                node = Node(key, value)

                self.cache[key] = node
                
                if 1 in self.freq:
                    self.freq[1].append(node)
                else:
                    self.freq[1] = DoublyLinkedList()
                    self.freq[1].append(node)
                
                self.lfu = 1
            else:

                lru = self.freq[self.lfu].head
                self.freq[self.lfu].remove(lru)
                del self.cache[lru.key]

                if self.freq[self.lfu].head is None:
                    del self.freq[self.lfu]

                
                node = Node(key, value)

                self.cache[key] = node
                
                if 1 in self.freq:
                    self.freq[1].append(node)
                else:
                    self.freq[1] = DoublyLinkedList()
                    self.freq[1].append(node)
                
                self.lfu = 1
                






        



                














       
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)