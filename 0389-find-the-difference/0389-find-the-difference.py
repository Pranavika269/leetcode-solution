class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(t)
        
        for ch in s:
            count[ch] -= 1
        
        for ch in count:
            if count[ch] > 0:
                return ch