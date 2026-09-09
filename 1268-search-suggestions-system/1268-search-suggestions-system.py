class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        lst = []

        for i in range(len(searchWord)):
            prefix = searchWord[:i+1]

            l = 0
            r = len(products) - 1

            while l <= r:
                mid = (l + r) // 2

                if products[mid][:i+1] < prefix:
                    l = mid + 1
                else:
                    r = mid - 1

            t = []

            for j in range(l, min(l + 3, len(products))):
                if products[j][:i+1] == prefix:
                    t.append(products[j])

            lst.append(t)

        return lst
