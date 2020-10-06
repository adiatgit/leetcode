def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    used = [[0 for i in range(len(board[0]))] for j in range((len(board)))]
    print(used)
    def get_index(letter):
        for i, sublist in enumerate(board):
            if letter in sublist:
                return [i,board.index(sublist)]
        return -1
    print get_index('D')
    for each_letter in word:
        get_index(each_letter)
exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], 'ABCCED')
