class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #after each char is typed, suggest at most three product names from products 
        #m - mobile, mouse, moneypot, monitor, mousepad
        #m - mobile, moneypot, monitor
        #mo - moneypot, monitorm, mouse
        #mou - mouse, mousepad


        products.sort()
        lst = []

        for i in range(len(searchWord)):
            t = []
            for ele in products:
                if searchWord[0:i+1] == ele[0:i+1] and len(t) < 3:
                    t.append(ele)
            
            lst.append(t)
        
        return lst
                
        

            

            









        