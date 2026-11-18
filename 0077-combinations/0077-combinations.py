class Solution:    
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        def backtrack(pos, res, curr=[]):
            if len(curr) > k:
                return
            if pos == n:
                if len(curr) == k:
                    res.append(curr.copy())
                return
            curr.append(pos + 1)
            backtrack(pos + 1, res, curr)
            curr.pop()
            backtrack(pos + 1, res, curr)
        backtrack(0, res)
        return res