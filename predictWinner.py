def PredictTheWinner(nums):
    player1, player2 = 0,0
    def predictWinner(list1, i, j):
        player1 += predictWinner(list1, i+1, j)
        player2 += predictWinner(list1, i+2,j)