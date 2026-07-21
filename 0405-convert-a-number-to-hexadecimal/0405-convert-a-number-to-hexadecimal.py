class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        ans = ""

        # Handle negative numbers using 32-bit two's complement
        if num < 0:
            num += 2**32

        while num:
            ans = hex_chars[num & 15] + ans
            num >>= 4
        return ans