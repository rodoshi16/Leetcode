class Node:

    def __init__(self):
        self.children = {}
        self.end = False

class Trie(object):

    def __init__(self):
        self.root = Node()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        #go through all children and check if word[0]
        #cur
        #continue 

        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]] = Node()
            cur = cur.children[word[i]]
        cur.end = True
            

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        #the very last word need to be an end word

        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.children:
                return False
            cur = cur.children[word[i]]

        return cur.end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """

        cur = self.root
        for i in range(len(prefix)):
            if prefix[i] not in cur.children:
                return False
            cur = cur.children[prefix[i]]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)