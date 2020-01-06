class Solution {
    int currArea = 0;
    int[][] ourGrid;

    public int maxAreaOfIsland(int[][] grid) {
        ourGrid = grid;
        int currMax = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (ourGrid[i][j] == 1) {
                    currArea = 0;
                    exploreIsland(i, j);
                    if (currArea > currMax) {
                        currMax = currArea;
                    }
                }
            }
        }
        return currMax;
    }

    public void exploreIsland(int row, int col) {
        if (row >= ourGrid.length || row < 0) {
            return;
        }
        if (col >= ourGrid[0].length || col < 0) {
            return;
        }
        if (ourGrid[row][col] == 'X' || ourGrid[row][col] == 0) {
            return;
        } else if (ourGrid[row][col] == 1) {
            ourGrid[row][col] = 'X';
            currArea += 1;
            System.out.println(currArea);
            exploreIsland(row - 1, col);
            exploreIsland(row + 1, col);
            exploreIsland(row, col + 1);
            exploreIsland(row, col - 1);
        }
    }
}
