class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #can hold at most one share of stock at any one time
        # u can sell/buy stock multiple times on same day (never more than one share of stock)

        #[7,1,5,3,6,4]
        # buy: when price is less
        # sell: when price is high

        # if prices[i] < buy 
        # buy =  math.inf
        # sell = 0 
        # profit = 0 
        # for i in range(len(prices)):
        #     if prices[i] < buy:
        #         buy = prices[i]
        #     elif prices[i] > buy:
        #         sell = prices[i]
        #         profit += (sell - buy)
        #         buy = math.inf
        #         sell = 0
        # return profit 


        profit = 0 
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit 

        