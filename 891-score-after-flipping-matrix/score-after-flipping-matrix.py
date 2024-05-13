class Solution:
    def invertRow(self, row):
        for i in range(len(row)):
            row[i] = int((not row[i]))

    def invertCol(self, col, grid):
        Rows = len(grid)
        for i in range(Rows):
            grid[i][col] = int((not grid[i][col]))
    
    def calcSum(self, grid):
        SUM = 0
        for row in grid:
            strRow = [str(n) for n in row]
            SUM+=int(''.join(strRow), 2)
        
        return SUM

    def matrixScore(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])

        for row in grid:
            if not row[0]:  self.invertRow(row)
        
        for j in range(Cols):
            if sum([grid[i][j] for i in range(Rows)]) < Rows/2:
                self.invertCol(j, grid)

        return self.calcSum(grid)