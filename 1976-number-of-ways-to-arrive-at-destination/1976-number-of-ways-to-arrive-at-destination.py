import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        # Build adjacency list
        graph = [[] for _ in range(n)]

        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        dist = [float('inf')] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1

        min_heap = [(0, 0)]  # (time, node)

        while min_heap:
            curr_time, node = heapq.heappop(min_heap)
            
            # Ignore outdated entries
            if curr_time > dist[node]:
                continue

            for nbr, edge_time in graph[node]:
                new_time = curr_time + edge_time

                # Found a shorter path
                if new_time < dist[nbr]:
                    dist[nbr] = new_time
                    ways[nbr] = ways[node]
                    heapq.heappush(min_heap, (new_time, nbr))

                # Found another shortest path
                elif new_time == dist[nbr]:
                    ways[nbr] = (ways[nbr] + ways[node]) % MOD

        return ways[n - 1]