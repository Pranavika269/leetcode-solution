class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                # Case 1: '*' matches zero occurrences of the preceding element.
                # We skip the 'char*' part of the pattern.
                # Case 2: '*' matches one or more occurrences.
                # This requires a match at the current position, then we advance
                # in the string but stay at the same pattern position.
                res = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # No '*' follows, so it's a standard one-to-one character match.
                res = first_match and dp(i + 1, j + 1)
            
            memo[(i, j)] = res
            return res

        return dp(0, 0)