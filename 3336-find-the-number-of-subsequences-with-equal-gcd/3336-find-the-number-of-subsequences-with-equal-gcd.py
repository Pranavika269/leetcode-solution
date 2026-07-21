from functools import cache
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        @cache
        def dfs(i, g1, g2):
            if i == len(nums):
                return int(g1 == g2 and g1 > 0)

            x = nums[i]
            return (
                dfs(i + 1, g1, g2) +
                dfs(i + 1, x if g1 == 0 else gcd(g1, x), g2) +
                dfs(i + 1, g1, x if g2 == 0 else gcd(g2, x))
            ) % MOD

        return dfs(0, 0, 0)