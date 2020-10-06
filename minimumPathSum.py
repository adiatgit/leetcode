def minPathSum(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j > 0:
                grid[i][j] = grid[i][j] + grid[i][j - 1]
            if j == 0 and i > 0:
                grid[i][j] = grid[i][j] + grid[i - 1][j]
            if i > 0 and j > 0:
                grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])
    print(grid)
    return grid[-1][-1]
print(minPathSum([
  [1,3,1]]))