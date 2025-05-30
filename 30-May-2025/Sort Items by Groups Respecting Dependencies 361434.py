# Problem: Sort Items by Groups Respecting Dependencies - https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        
        item_graph = defaultdict(list)
        item_indegree = [0] * n

        group_graph = defaultdict(list)
        group_indegree = [0] * m

        group_to_items = defaultdict(list)

        for i in range(n):
            group_to_items[group[i]].append(i)

            for prev in beforeItems[i]:
                if group[prev] == group[i]:
                    item_graph[prev].append(i)
                    item_indegree[i] += 1
                else:
                    group_graph[group[prev]].append(group[i])
                    group_indegree[group[i]] += 1
        
        def topological_sort(nodes, graph, indegree):
            queue = deque([node for node in nodes if indegree[node] == 0])
            res = []
            while queue:
                node = queue.popleft()
                res.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
            return res if len(res) == len(nodes) else []

        sorted_items_in_group = {}

        for g in group_to_items:
            items = group_to_items[g]
            sorted_items = topological_sort(items, item_graph, item_indegree[:])
            if not sorted_items:
                return []
            sorted_items_in_group[g] = sorted_items
        
        groups = list(group_to_items.keys())
        sorted_groups = topological_sort(groups, group_graph, group_indegree[:])

        if not sorted_groups:
            return []
        
        result = []
        for g in sorted_groups:
            result.extend(sorted_items_in_group[g])
        return result