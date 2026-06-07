class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a >= c:
                    dp[a] = min(dp[a], dp[a - c] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
















        # if amount == 0:
        #     return 0

        # if len(coins) == 1:
        #     if amount == coins[0]:
        #         return 1
        #     elif amount != coins[0] and amount == 0:
        #         return 0
        #     elif amount % coins[0] == 0:
        #         return amount // coins[0]
        #     else:
        #         return -1

        # i = 1 
        # dp = [0]
        # while i < 90: 
        #     s = set()
        #     for ele in dp:
        #         for c in coins:
        #             a = ele + c
        #             s.add(a)
        #             if a == amount:
        #                 return i
        #     i += 1
        #     dp = s
        # return -1




