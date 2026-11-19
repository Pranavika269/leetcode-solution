class Solution:
    def __init__(self):
        self.cache = None


    def generateTrees(self, n: int) -> list[TreeNode | None]:
        self.cache = [[None for _ in range (n + 1)] for _ in range (n + 1)]
        return self.get_unique_trees(1, n)


    def get_unique_trees(self, l, r):
        node = []


        if l > r:
            node.append(None)
            return node


        if self.cache[l][r]:
            return self.cache[l][r]


        for i in range(l, r + 1):
            left_subtrees = self.get_unique_trees(l, i - 1)
            right_subtrees = self.get_unique_trees(i + 1, r)


            for left_subtree in left_subtrees:
                for right_subtree in right_subtrees:
                    n = TreeNode(i)


                    n.left = left_subtree
                    n.right = right_subtree
                    node.append(n)


        self.cache[l][r] = node
        return node