def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # checking rows
    def checkValid(theList):
        x = [i for i in theList if i!='.']
        return len(x) == len(set(x))
    for i in board:
        if(not checkValid(i)):
            return False
    for i in range(len(board[0])):
        x = [row[i] for row in board]
        if(not checkValid(x)):
            return False
    for i in range(0, 9,3):
        for j in range(0,9,3):
            matrix = [board[x][y] for x in range(i, i+3) for y in range(j,j+3)]
            if(not checkValid(matrix)):
                return False
    return True
isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])