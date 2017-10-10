from GameEngine.Player import Player
from GamePlatform.Platform import Platform
from os import system

class UI:
    def __init__(self):
        pass

    def initPlayer(self, n):
        p_name = input("Player {}: ".format(n))
        while True:
            answer = input("AI? (Y/N): ")
            print(answer)
            if answer.lower() == "y":
                while True:
                    difficulty = input("Difficulty: (hard/medium/easy): ")
                    if difficulty.lower() in ["hard", "medium", "easy"]:
                        return Player(p_name, "ai", difficulty)
            elif answer.lower() == "n":
                return Player(p_name, "user")

    def initGame(self):
        p1 = self.initPlayer(1)
        p2 = self.initPlayer(2)
        p = Platform(p1, p2)
        system("clear")
        p.startGame()

    def initMenu(self):
        while True:
            print("Tic-Tac-Toe")
            print("1. Play a game")
            print("2. Create a tournament")
            print("3. Quit")

            choice = input("What do you want to do? ")
            if choice == "1":
                self.initGame()
            elif choice == "2":
                pass
            elif choice.lower() == "q" or choice == "3":
                self.exitGame()
            else:
                print("Wrong input")

    def startGame(self):
        while True:
            system("clear")
            self.initMenu()

    def exitGame(self):
        print("Thank you for playing!")
        exit()

