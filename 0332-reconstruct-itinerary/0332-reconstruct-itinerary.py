from typing import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #iterating through the nested list and constructing a graph 
        # think of each element to be a node 
        # set the neighbours to be next 
        # construct adj from tickets 
        # perform dfs 
        
        d = defaultdict(list)
        for lst in tickets:
            d[lst[0]].append(lst[1])
            
        for src in d:
            d[src].sort(reverse=True)
        
        if "JFK" not in d:
            return []
    
        final = []
        
        
        def dfs(source):
            while d[source]: 
                nei = d[source].pop()
                dfs(nei)
            final.append(source)
        
        dfs("JFK")
        return final[::-1]
        
        