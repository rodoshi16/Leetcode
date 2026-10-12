class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True 

        for i in range(n):
            if not dp[i]:
                continue

            for j in range(i+1, n+1):
                if s[i: j] in words:
                    dp[j] = True
        
        return dp[n]



        

                





        


        




