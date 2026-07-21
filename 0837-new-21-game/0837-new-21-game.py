class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        cache = {}

        def dfs(score):
            if score == k - 1:
                return min(n - k + 1, maxPts) / maxPts
            if score > n:
                return 0
            if score >= k:
                return 1.0

            if score in cache:
                return cache[score]

            cache[score] = dfs(score + 1)
            cache[score] -= (dfs(score + 1 + maxPts) - dfs(score + 1)) / maxPts
            return cache[score]

        return dfs(0)