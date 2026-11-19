class Solution:
    def simplifyPath(self, path: str) -> str:
        dir = path.split("/")

        stack = []

        for i in dir:
            if i == ".." and stack:
                stack.pop()

            elif i == "." or i == "" or i == "..":
                continue

            else:
                stack.append(i)

        res = ""

        for i in stack:
            res += "/" + i

        return "/" if res == "" else res