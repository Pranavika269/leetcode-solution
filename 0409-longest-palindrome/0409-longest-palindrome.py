class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        odd = False

        for freq in count.values():
            length += (freq // 2) * 2
            if freq % 2 == 1:
                odd = True

        if odd:
            length += 1

        return length