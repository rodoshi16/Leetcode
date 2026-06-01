class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([(0, 0)])  # (current_amount, coins_used)
        visited = {0}

        while q:
            curr, steps = q.popleft()

            if curr == amount:
                return steps

            for coin in coins:
                nxt = curr + coin

                if nxt <= amount and nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps + 1))

        return -1

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




