import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # orders - list of orders
        # [price, amount, type]
        # 0 - buy, 1 - sell

        #buy - smallest sell order
        # trade - sell <= buy - trade
        # rest in the backlog

        # sell order - highest buy
        # buy >= sell - trade

        # return total amount of orders in the backlog


        # 5 + 1
        # buy {}, sell {}

        buy = []
        sell = []
        total = 0 
        MOD = (10 ** 9) + 7

        for price, amount, ordertype in orders:
            if ordertype == 0:
                # (5, 15), (2, 10)
                # keep matching trades if sell <= buy
                # if remaining - goes back to backlog 

                while amount > 0 and sell and sell[0][0] <= price:
                    sell_price, sell_amount = heapq.heappop(sell)

                    trade = min(sell_amount, amount)
                    amount -= trade
                    sell_amount -= trade 

                    if sell_amount > 0:
                        heapq.heappush(sell, (sell_price, sell_amount))
                
                if amount > 0:
                    heapq.heappush(buy, (-price, amount))
            
            else:


                while amount > 0 and buy and -buy[0][0] >= price:
                    buy_price, buy_amount = heapq.heappop(buy)

                    trade = min(buy_amount, amount)
                    buy_amount -= trade
                    amount -= trade 

                    if buy_amount > 0:
                        heapq.heappush(buy, (buy_price, buy_amount))
                
                if amount > 0:
                    heapq.heappush(sell, (price, amount))
        

        for price, amount in buy:
            total += amount
        
        for price, amount in sell:
            total += amount
        
        return total % MOD
        
        

        

        


                    


                    



            

             






        




        