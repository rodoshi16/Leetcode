class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        groups = {}
        for i in range(n):
            if group[i] not in groups:
                groups[group[i]] = []
            groups[group[i]].append(i)

        group_graph = {g: set() for g in groups}
        group_indegree = {g: 0 for g in groups}

        item_graph = {i: [] for i in range(n)}
        item_indegree = [0] * n

        for i in range(n):
            for prev in beforeItems[i]:
                item_graph[prev].append(i)
                item_indegree[i] += 1

                if group[prev] != group[i]:
                    if group[i] not in group_graph[group[prev]]:
                        group_graph[group[prev]].add(group[i])
                        group_indegree[group[i]] += 1


        def topo_groups():
            queue = deque()

            for g in group_indegree:
                if group_indegree[g] == 0:
                    queue.append(g)

            result = []

            while queue:
                g = queue.popleft()
                result.append(g)

                for nxt in group_graph[g]:
                    group_indegree[nxt] -= 1

                    if group_indegree[nxt] == 0:
                        queue.append(nxt)

            return result if len(result) == len(groups) else []


        def topo_items(items):
            indegree = {i: 0 for i in items}

            for i in items:
                for nxt in item_graph[i]:
                    if nxt in indegree:
                        indegree[nxt] += 1

            queue = deque()

            for i in items:
                if indegree[i] == 0:
                    queue.append(i)

            result = []

            while queue:
                i = queue.popleft()
                result.append(i)

                for nxt in item_graph[i]:
                    if nxt in indegree:
                        indegree[nxt] -= 1

                        if indegree[nxt] == 0:
                            queue.append(nxt)

            return result if len(result) == len(items) else []


        group_order = topo_groups()

        if not group_order:
            return []

        answer = []

        for g in group_order:
            sorted_items = topo_items(groups[g])

            if not sorted_items:
                return []

            answer.extend(sorted_items)

        return answer