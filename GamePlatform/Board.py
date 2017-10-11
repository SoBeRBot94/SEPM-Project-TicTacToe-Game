from __future__ import print_function


class Board:

    def __init__(self):
        self.board = [0] * 9
        self.winningCombinations = (
            [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        )

    '''
    This function updates the board.
    Param: move (int) the move by the player or the AI
    Param: player (int) the current player
    '''
    def updateBoard(self, move, player):
        self.board[move-1] = player
        return self


    '''
    This function converts the board from list to a tuple. Replacing 0 with None, 1 with 'X' and 2 with 'O'
    '''

    def convertBoard(self):
        for index, item in enumerate(self.board):
            if item == 1:
                self.board[index] = 'X'
            elif item == 2:
                self.board[index] = 'O'
            else:
                self.board[index] = None
        i = 0
        convertedBoard = []
        while i < len(self.board):
            convertedBoard.append(self.board[i:i + 3])
            i += 3
        return convertedBoard

    '''
    This function reconverts from tuple to list. Replacing None with 0, 'X' with 1 and 'O' with 2
    Param: board (tuple) the board you are converting to a list
    '''

    def reConvertBoard(self, board):
        convertedBoard = [item for b in board for item in b]
        for index, item in enumerate(convertedBoard):
            if item == 'X':
                convertedBoard[index] = 1
            elif item == 'O':
                convertedBoard[index] = 2
            else:
                convertedBoard[index] = 0
        self.board = convertedBoard
        return self.board

    def convertMove(self, move):
        r, c = move
        return (r * 3) + (c + 1)

    '''
    This function returns the board updated with the new AI move. Depending on the difficulty chosen
    different AIs will be used.
    Param: AIlevel (int) the difficulty of the AI, can be a number between 1 and 3
    Param: player (int) who the current player is, should be either the number 1 or 2
    Return: board (list). If invalid player or AIlevel function returns 0
    '''

    '''
    TODO: here you call your AI, and change to the AIlevel corresponding to the level of difficulty.
    The idea is that we convert our list board to your tuple board, call your AI and then reconvert it 
    to a tuple. 
    '''

    def AImove(self, AIplayer, player):
        if player == 1 or player == 2:
            convertedBoard = self.convertBoard()
            turn = 'X' if (player == 1) else 'O'
            newMove = self.convertMove(AIplayer.nextMove(convertedBoard, turn))
            self.reConvertBoard(convertedBoard)
            self.playerMove(newMove, player)
            return newMove
        else:
            return 0


    '''
    This function returns the board updated with the new move. If the move or the player is invalid
    -1 will be returned.
    Param: move (int) the move the player choose to make, should be a number between 1 and 9
    Param: player (int) who the current player is, should be either the number 1 or 2
    Return: board (list)
    '''
    def playerMove(self, move, player):
        if player != 1 and player != 2:
            return -1

        if not self.checkValidMove(move):
            return -1
        else:
            self.updateBoard(move, player)
        return self.board


    '''
    This function initiates the board.
    Return: board (list)
    '''
    def initiateGameState(self):
        board = [0] * 9
        return board


    '''
    This function checks if any player has won
    Return: 0 if no winner, 1 or 2 if winner
    '''
    def checkWinner(self):
        for combination in self.winningCombinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == 1:
                return 1
            elif self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == 2:
                return 2
        return 0

    '''
    This function checks if the move is valid.
    Return: Bool
    '''
    def checkValidMove(self, move):
        if move not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
        elif self.board[move-1] != 0:
           return False
        return True



    def anySpaceLeft(self):
        """
        Checks if there is zeros in self.board
        :return: True if there is a zero in self.board otherwise False
        """
        for i in range(0, 9):
            if self.board[i] == 0:
                return True
        return False


    def printBoard(self):
      """
      Prints the board
      :return:
      """

      """for i in range(0,9):
          if (i%3) == 0:
              print("-------------")"""

      print("====== Game Platform ======")
      print("       -------------")
      print("       | " + str(self.board[0])+ " | " + str(self.board[1]) + " | " + str(self.board[2]) + " |")
      print("       -------------")
      print("       | " + str(self.board[3])+ " | " + str(self.board[4]) + " | " + str(self.board[5]) + " |")
      print("       -------------")
      print("       | " + str(self.board[6])+ " | " + str(self.board[7]) + " | " + str(self.board[8]) + " |")
      print("       -------------")
      print("===========================")

    def setBoard(self,newboard):
        """
        Changes the current board into a new board. Used in the testing only
        :param newboard: The board (int[9]) that will be changed into
        """
        self.board = newboard


    def print(self):
        print(self.board[0:3])
        print(self.board[3:6])
        print(self.board[6:9])
        return False
