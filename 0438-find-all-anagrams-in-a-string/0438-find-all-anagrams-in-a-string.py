class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m=len(p)
        p = sorted(p)
        a = []
        for i in range(n - m + 1):
            sub = sorted(s[i : i + m])
            if sub == p:
                a.append(i)
        return a