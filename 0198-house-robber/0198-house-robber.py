class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        
        visted = {0: nums[0]}

        for i in range(1, n):
            if i-2 in visted and i-3 in visted:
                visted[i] = max(visted[i-2], visted[i-3]) + nums[i]
            elif i-2 in visted:
                visted[i] = visted[i-2] + nums[i]
            else:
                visted[i] = nums[i]
        
        return max(visted[n - 1], visted[n - 2])