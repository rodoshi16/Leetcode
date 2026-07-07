class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if graph == []:
            return True 
        
        d = {}

        for i in range(len(graph)):
            if i not in d:
                s = [i]
                d[i] = "red"

            while s:
                t = s.pop()
                if t not in d:
                    d[t] = "red"

                for n in graph[t]:
                    if n in d and d[t] == d[n]:
                        return False
                    
                    elif n not in d and d[t] == "red":
                        d[n] = "blue"
                        s.append(n)
                    
                    elif n not in d and d[t] == "blue":
                        d[n] = "red"
                        s.append(n)
        
        return True
                


        










        

        