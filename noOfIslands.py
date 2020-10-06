def numIslands(grid):
    def traverse(root, i, j, visited):
        if i < 0 or j < 0 or i >= len(root) or j >= len(root[0]) or root[i][j] != '1':
            return
        root[i][j] = '-1'
        traverse(root, i + 1, j, visited)
        traverse(root, i - 1, j, visited)
        traverse(root, i, j + 1, visited)
        traverse(root, i, j - 1, visited)
    count = 0
    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] =='1':
                traverse(grid, i, j, visited)
                count += 1
    return count
print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))