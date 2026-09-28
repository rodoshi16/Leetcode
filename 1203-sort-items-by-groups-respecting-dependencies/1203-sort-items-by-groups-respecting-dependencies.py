class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        groups = {}
        for i in range(n):
            if group[i] not in groups:
                groups[group[i]] = [i]
            else:
                groups[group[i]].append(i)

       
        item_before = {i: [] for i in range(n)}    
        group_before = {g: [] for g in range(m)}  

        for i in range(n):
            for p in beforeItems[i]:
                if group[p] == group[i]:
                    item_before[i].append(p)
                else:
                    group_before[group[i]].append(group[p])


        def top_sort(nodes, before):
            res = []
            visited = set()
            path = set()   

            def top(ele):
                if ele in path:
                    return False      
                if ele in visited:
                    return True
                path.add(ele)
                for p in before[ele]:
                    if not top(p):    
                        return False
                path.remove(ele)
                visited.add(ele)
                res.append(ele)
                return True

            for ele in nodes:
                if not top(ele):
                    return None
            return res

        group_order = top_sort(range(m), group_before)
        if group_order is None:
            return []

      
        res = []
        for g in group_order:
            items = top_sort(groups.get(g, []), item_before)
            if items is None:
                return []
            res.extend(items)

        return res
        
        


