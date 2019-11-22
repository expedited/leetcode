class Solution:
    grid = []
    # mark a spot with X if we've seen it, then update our real grid in numIslands

    def exploreIsland(self, curr, grid):
        if curr[0] < 0 or curr[0] >= len(grid):
            return
        if curr[1] < 0 or curr[1] >= len(grid[0]):
            return
        currval = self.grid[curr[0]][curr[1]]
        if currval == "0" or currval == "X":
            return
        else:
            self.grid[curr[0]][curr[1]] = "X"
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for x, y in directions:
            self.exploreIsland((curr[0] + x, curr[1] + y), self.grid)
        return

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                curr = self.grid[row][col]
                if curr == "1":
                    self.exploreIsland((row, col), self.grid)
                    count += 1
        return count
