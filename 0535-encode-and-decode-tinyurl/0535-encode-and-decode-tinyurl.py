import random
class Codec:
    d = {}
    counter = 1 

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.counter += 1 
        new_s = f"http://tinyurl.com/{self.counter}"
        self.d[new_s] = longUrl 
        return new_s

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl in self.d:
            return self.d[shortUrl]
        else:
            return ""
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))