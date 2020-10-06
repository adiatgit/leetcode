def gol(board):
    count = [[0 for j in range(len(board[0]))] for i in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            for k in (-1, 0, 1):
                for m in (-1, 0, 1):
                    n, o= i+k, j+m
                    if i + k < len(board) and i + k >= 0 and j + m < len(board[0]) and j + m >= 0:
                        if not(i + k == i and j + m == j):
                            if board[i + k][j + m] == 1:
                                count[i][j] += 1

    for i in range(len(board)):
        for j in range(len(board[0])):
            if count[i][j] < 2 and board[i][j] == 1:
                board[i][j] = 0
            elif count[i][j] <= 3 and board[i][j] == 1:
                board[i][j] = 1
            elif count[i][j] > 3 and board[i][j] == 1:
                board[i][j] = 0
            elif count[i][j] == 3 and board[i][j] == 0:
                board[i][j] = 1
    return board
print(gol([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]))
