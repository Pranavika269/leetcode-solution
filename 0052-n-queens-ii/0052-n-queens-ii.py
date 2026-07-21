class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row):
            if row == n:
                return 1
            else:
                count = 0

                for col in range(n):
                    if col in cols:
                        continue
                    elif row - col in diag1:
                        continue
                    elif row + col in diag2:
                        continue
                    else:
                        cols.add(col)
                        diag1.add(row - col)
                        diag2.add(row + col)

                        count += backtrack(row + 1)

                        cols.remove(col)
                        diag1.remove(row - col)
                        diag2.remove(row + col)

                return count

        return backtrack(0)