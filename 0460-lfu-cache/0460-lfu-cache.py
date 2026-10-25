#lru
# A-B-C
# 3 2 7
# {A: 3, B: 3, C: 3}
# {2: [D], 3: [B, C, A]}

#Doubly ll
# Node

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
        #head
        # tail
        # middle

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
        #tail
        # no tail

        if self.tail is None:
            self.tail = node
            self.head = node
        
        else:

            self.tail.next, node.prev = node, self.tail
            self.tail = node
            node.next = None

class LFUCache:
    def __init__(self, capacity: int):
        #cache, freq hashmap
        #self.lfu var

        self.capacity = capacity
        self.cache = {}
        self.lfu = 1 
        self.freq = {1: DoublyLinkedList()}



    def get(self, key: int) -> int:
        #key exists - remove from last freq, add to new freq
        # key doesnt - return -1
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
        # exists - update val, update freq
        # not exist - 1.if have capacity: create and add to freq 1
        # no cap - evict lfu, del if needed

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

            node = Node(key, value)
            if len(self.cache) < self.capacity:
                self.cache[key] = node
                
                if 1 not in self.freq:
                    self.freq[1] = DoublyLinkedList()
                self.freq[1].append(node)
                self.lfu = 1 
            
            else:

                #evict lfu
                lru = self.freq[self.lfu]
                del self.cache[lru.head.key]
                lru.remove(lru.head)


                self.cache[key] = node
                if 1 not in self.freq:
                    self.freq[1] = DoublyLinkedList()
                self.freq[1].append(node)
                self.lfu = 1 





        
                














       
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)