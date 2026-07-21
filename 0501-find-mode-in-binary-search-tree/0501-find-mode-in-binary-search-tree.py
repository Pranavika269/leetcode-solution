# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = Counter()

        def dfs(node):
            if not node:
                return

            count[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        max_freq = max(count.values())

        return [key for key, value in count.items() if value == max_freq]