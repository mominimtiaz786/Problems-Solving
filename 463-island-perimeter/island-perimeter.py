class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c]:
                    sides_connected = [
                        r and grid[r-1][c],
                        c and grid[r][c-1],
                        r < rows -1 and grid[r+1][c],
                        c < cols -1 and grid[r][c+1],
                    ]
                    perimeter+=(4-sum([bool(side) for side in sides_connected]))


        return perimeter