from GameEngine.Player import Player
from GamePlatform.Platform import Platform
from random import shuffle

class Tournament: 

    def __init__(self):
        self.quarterFinals = []
        self.semiFinals = []
        self.final = [] 
        self.difficulties = ['easy', 'medium', 'hard']     

    def startTournament(self):
        # Entering players 
        players = self.enterPlayers()
        ais = self.enterAIs(8 - len(players))
        # fill quarterFinals array with players and randomize the order
        for player in players:
            self.quarterFinals.append(Player(player, "user"))
        for ai in ais: 
            self.quarterFinals.append(Player(ai[0], "ai", ai[1]))
        shuffle(self.quarterFinals)
        print(self.quarterFinals)
        # matches are querterFinals[0] against quarterFinals[1], que
        # rterFinals[2] agains quarterFinals[3] and so on.
        for x in [0,2,4,6]:
            p = Platform(self.quarterFinals[x], self.quarterFinals[x + 1])
            # collect the winner of each quarter final and semiFinals.append(winner)
            winner = p.startGame()
            if (winner == 'tie'):
                # very unfair
                self.semiFinals.append[self.quarterFinals[x]]
            self.semiFinals.append(winner)

        print(self.semiFinals)

        # start matches semiFinals [0] against semiFinals[1] ...
        for x in [0,2]:
            p = Platform(self.semiFinals[x], self.semiFinals[x + 1])
            winner = p.startGame()
            if (winner == 'tie'):
                # still very unfair
                self.final.append[self.semiFinals[x]]
            self.final.append(winner)
    
        print(self.final)
        winner = 'tie'
        while (winner == 'tie'):
            p = Platform(self.final[0], self.final[1])
            winner = p.startGame()
        print("The winner is..." + winner.name + "!")
        # ... 
        # at last we have a winner!!!!!!! :)

    def enterPlayers(self):
        entersPlayers = True 
        players = []
        while (entersPlayers and (len(players) < 8)):
            inp = input("Enter the name of a player or 'ai' to start entering ais: ")
            if not (inp.lower() == "ai"):
                players.append(inp)
            else: 
                entersPlayers = False
        return players

    def enterAIs(self, amount):
        ais = []
        for x in range(0, amount):
            name = input("Enter AI name: ")
            difficulty = input("Enter AI difficulty ('easy', 'medium', 'hard'): ")
            while (difficulty.lower() not in self.difficulties): 
                difficulty = input("Enter AI difficulty ('easy', 'medium', 'hard'): ")

            ais.append((name, difficulty))
        return ais



#if __name__ == '__main__': 
#    t = Tournament()
#    t.startTournament()