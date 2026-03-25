class Codec:
    d = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        new_s = f"http://tinyurl.com/{len(self.d)+1}"
        self.d[new_s] = longUrl 
        return new_s

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
 
        return self.d[shortUrl]
    
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))