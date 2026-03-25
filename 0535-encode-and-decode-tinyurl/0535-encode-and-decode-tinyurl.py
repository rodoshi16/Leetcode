import random
class Codec:
    d = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        new_s = f"{longUrl[::8]}tinyurl.com/{random.randint(0, 19029)}"
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