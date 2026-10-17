class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        #input: list of stock prices, fee
        # output: max profit to achieve

        # every trans has a fee
        # [1,3,2,8,4,9]

        # just buy on the lowest price at the beginning and sell on the max - fee

        # 7-2 = 5, 9-4= 5-2 = 3
        # [1,3,7,5,10,3]

        # not holding -> buy, not buy
        # holding -> sell, not sell
        # (state, prices[i])
        
        d = {}

        def dp(state, i):
            #max profit
            if i == len(prices):
                if state == 0:
                    return 0 
                else:
                    return float('-inf')

            if (state, i) in d:
                return d[(state, i)]

            if state == 0:
                d[(state, i)] = max(dp(0, i+1), dp(1, i+1) - prices[i])
            
            if state == 1:
                d[(state, i)] = max(dp(1, i+1), dp(0, i+1) + prices[i] - fee)
            
            return d[(state, i)]

        
        return dp(0, 0)