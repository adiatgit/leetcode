def MaxDistance(grid):
    # 0 for water, 1 for land
    grid_length = len(grid)
    zerosPos = []
    onesPos =[]
    for i in range(0, grid_length):
        for j in range(0, grid_length):
            if(grid[i][j] == 0):
                zerosPos.append([i,j])
            else:
                onesPos.append([i,j])
    maxAll =[]
    if(len(onesPos)==0 or len(zerosPos)==0):
        return -1
    for i in zerosPos:
        maxDist=grid_length+1
        for j in onesPos:
            currentDist = abs(i[0] - j[0]) + abs(i[1]- j[1])
            if(currentDist <= maxDist):
                maxDist =currentDist
        maxAll.append(maxDist)
    return max(maxAll)

# grid = [[1,0,1],[0,0,0],[1,0,1]]
grid = [[1,0,0],[0,0,0],[0,0,0]]
print MaxDistance(grid)
