from GamePlatform.Board import Board
import time

class Platform:
    def __init__(self, player1, player2):

        self.players = [player1, player2]
        self.playerTurn = 1
        self.gameState = Board()

    '''
    Main loop
    returns winner name or 0 if tie
    '''
    def startGame(self):
        winner = 0
        self.printBoardHelp()
        print("To place a move, enter the number corresponding to the position on the board")
        print("Press q to quit the game\n")

        while True:
            self.gameState.printBoard()
            if self.players[self.playerTurn-1].typePlayer == "user":
                inputMove = self.askForMove(self.players[self.playerTurn-1].name, "Choose your move: ")
                if inputMove in ('q', 'Q', 'quit', 'Quit'):
                    print(self.players[self.playerTurn-1].name, "has quit the game")
                    # What should be returned? should other player win?
                    break
                while True:
                    moveIsValid = self.gameState.checkValidMove(inputMove)
                    if moveIsValid:  # or inputMove == 0:
                        break
                    else:
                        inputMove = self.askForMove(self.players[self.playerTurn-1].name, "Invalid move, input a new move: ")
                # if inputMove==0:
                #    winner = self.gameState.checkWinner()
                #    break
                self.gameState.playerMove(inputMove, self.playerTurn)
            else:
                time.sleep(1)
                self.gameState.AImove(self.players[self.playerTurn-1], self.playerTurn)

            winner = self.gameState.checkWinner()
            if winner != 0:
                self.gameState.printBoard()
                print("The Winner is " + self.players[winner-1].name + "!")
                print("Congratulations!")
                winner = self.players[winner-1].name
                break

            if not self.gameState.anySpaceLeft():
                print("The Game Ended in a Tie!")
                break

            if self.playerTurn == 1:
                self.playerTurn = 2
            elif self.playerTurn == 2:
                self.playerTurn = 1
            else:
                print("Something has gone wrong while switching players")

        return winner

    def askForMove(self, player, string):
        while True:
            inputString = input(str(player)+", "+string)
            if len(inputString) > 0 and inputString in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return int(inputString)
            elif len(inputString) > 0 and inputString in ['q', 'Q', 'quit', 'Quit']:
                return inputString
            else:
                print("Invalid input, should be 1-9")

    def printBoardHelp(self):
        print("===== Board Positions ====")
        print("       -------------     ")
        print("       | 1 | 2 | 3 |     ")
        print("       -------------     ")
        print("       | 4 | 5 | 6 |     ")
        print("       -------------     ")
        print("       | 7 | 8 | 9 |     ")
        print("       -------------     ")
        print("========================== \n")
