class GameEngine:
    def __init__(self):
        self.board = [[None for i in range(3)] for i in range(3)]
        self.player = 'X'
        self.nextMove = None
        #print("Game Engine init")

    def getPlayer(self):
        return self.player
        #if self.player == 'X':
        #    self.player = 'O'
        #else:
        #    self.player = 'X' 

    def changePlayer(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'
    # If the move is valid the function retruns the updated board.
    # If the move is invalid the function returns None. 
    def makeMove(self, row, col, player):
        if (self.board[row][col] == None):
            self.board[row][col] = player
            #self.changePlayer()
            return self.board
        return None

    def getBoard(self):
        #print(self.board)
        return self.board

    def updateBoard(self, player, move):
        self.board[move[0]][move[1]] = player

    def isFinished(self, board):
        for i in range(0,3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] !=            None:
                return True

            if board[i][0] == board[i][1] == board[i][2] and board[i][0] !=            None:
                return True

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != None:
            return True
        if board[2][0] == board[1][1] == board[0][2] and board[2][0] != None:
            return True

        return not any(None in row for row in board)

