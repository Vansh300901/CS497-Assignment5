class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """

        n = len(graph)
        all_visited = (1 << n) - 1

        inf = 10**9
        dp = [[inf] * n for _ in range(1 << n)]

        for i in range(n):
            dp[1 << i][i] = 0

        for mask in range(1 << n):
            for u in range(n):
                if mask & (1 << u):
                    for v in graph[u]:
                        next_mask = mask | (1 << v)
                        dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + 1)

        result = min(dp[all_visited][i] for i in range(n))

        if result != inf:
            return result
        
        return -1