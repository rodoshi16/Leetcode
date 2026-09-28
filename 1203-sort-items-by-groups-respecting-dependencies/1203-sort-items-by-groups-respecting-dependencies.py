class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        # group -> its items (same as yours)
        groups = {}
        for i in range(n):
            if group[i] not in groups:
                groups[group[i]] = [i]
            else:
                groups[group[i]].append(i)

        # two "before" maps, built from the same beforeItems
        item_before = {i: [] for i in range(n)}    # same-group prerequisites
        group_before = {g: [] for g in range(m)}   # prerequisite groups

        for i in range(n):
            for p in beforeItems[i]:
                if group[p] == group[i]:
                    item_before[i].append(p)
                else:
                    group_before[group[i]].append(group[p])

        # your top() idea, made generic: order `nodes` using `before`
        def top_sort(nodes, before):
            res = []
            visited = set()
            path = set()   # nodes on the current recursion path, to catch cycles

            def top(ele):
                if ele in path:
                    return False        # cycle
                if ele in visited:
                    return True
                path.add(ele)
                for p in before[ele]:
                    if not top(p):      # handle prerequisites first
                        return False
                path.remove(ele)
                visited.add(ele)
                res.append(ele)
                return True

            for ele in nodes:
                if not top(ele):
                    return None
            return res

        # 1) order the groups
        group_order = top_sort(range(m), group_before)
        if group_order is None:
            return []

        # 2) for each group, in that order, order just its items
        res = []
        for g in group_order:
            items = top_sort(groups.get(g, []), item_before)
            if items is None:
                return []
            res.extend(items)

        return res
        
        


