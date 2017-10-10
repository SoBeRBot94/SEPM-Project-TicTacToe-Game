from GameEngine.Player import Player
from GamePlatform.Platform import Platform
import random 

class Tournament: 

    def __init__(self):
        self.quarterfinals = []
        self.semifinals = []
        self.final = [] 
        self.difficulties = ['easy', 'medium', 'hard']     

    """
        Runs the quarterfinals and adds the winner to the semifinals.
        If a game ends in a tie the winner is choosen at random with equal probability. 
    """
    def runQuarterfinals(self):
        # matches are querterFinals[0] against quarterFinals[1]
        # qurterFinals[2] agains quarterFinals[3] and so on.
        for x in [0,2,4,6]:
            p = Platform(self.quarterfinals[x], self.quarterfinals[x + 1])
            # collect the winner of each quarter final and semiFinals.append(winner)
            winner = p.startGame()
            if (winner == 'tie'):
                self.semifinals.append(self.quarterfinals[x + random.randint(0,1)])
            else: 
                self.semifinals.append(winner)
    
    """
        Runs the semifinals and adds the winner to the final.
        If a game ends in a tie the winner is choosen at random with equal probability. 
    """
    def runSemifinals(self):
        # start matches semiFinals[0] against semiFinals[1] ...
        for x in [0,2]:
            p = Platform(self.semifinals[x], self.semifinals[x + 1])
            winner = p.startGame()
            if (winner == 'tie'):
                self.final.append(self.semifinals[x + random.randint(0,1)])
            else: 
                self.final.append(winner)
    
    """
        Runs the final.
        If a game ends in a tie the winner is choosen at random with equal probability. 
    """
    def runFinal(self):
        p = Platform(self.final[0], self.final[1])
        winner = p.startGame()
        if (winner == 'tie'):
            winner = self.final[random.randint(0, 1)]

        print("The winner of the tournament is " + winner.name + "!")

    """
        Creates Player objects given the name and difficulties entered by the user.
    """
    def fillTournament(self): 
        players = self.enterPlayers()
        ais = self.enterAIs(self.numberOfPlayers - len(players))

        if (self.numberOfPlayers == 8):
            self.fillQuarterfinals(players, ais)
        if (self.numberOfPlayers == 4):
            self.fillSemifinals(players, ais)

    def fillQuarterfinals(self, players, ais):
        for player in players:
            self.quarterfinals.append(Player(player, "user"))
        for ai in ais: 
            self.quarterfinals.append(Player(ai[0], "ai", ai[1]))
        random.shuffle(self.quarterfinals)
        
    def fillSemifinals(self, players, ais):
        for player in players:
            self.semifinals.append(Player(player, "user"))
        for ai in ais: 
            self.semifinals.append(Player(ai[0], "ai", ai[1]))
        random.shuffle(self.semifinals)

    """
        Prompts the user for the tournament size. Saves it to self.numberOfPlayers.
    """
    def getTournamentSize(self):
        inp = input("Enter the number of players in the tournament ('4' or '8'): ")
        while (inp not in ['4', '8']):
            inp = input("Invalid input. Enter the number of players in the tournament ('4' or '8'): ")
        self.numberOfPlayers = int(inp)

    def startTournament(self):
        self.getTournamentSize()
        self.fillTournament()
        if (self.numberOfPlayers == 8):
            self.runQuarterfinals()
        self.runSemifinals()
        self.runFinal()

    """
        :returns: The name of the players entered by the user.
        :rtype: [String]
    """
    def enterPlayers(self):
        entersPlayers = True 
        players = []
        while (entersPlayers and (len(players) < self.numberOfPlayers)):
            inp = input("Enter the name of a player or 'ai' to start entering ais: ")
            if not (inp.lower() == "ai"):
                players.append(inp)
            else: 
                entersPlayers = False
        return players

    """
        :returns: The name of the ai and the difficulty entered by the user (name, difficulty).
        :rtype: [(String, String)]
    """
    def enterAIs(self, amount):
        ais = []
        for x in range(0, amount):
            name = input("Enter AI name: ")
            difficulty = input("Enter AI difficulty ('easy', 'medium', 'hard'): ")
            while (difficulty.lower() not in self.difficulties): 
                difficulty = input("Enter AI difficulty ('easy', 'medium', 'hard'): ")

            ais.append((name, difficulty))
        return ais

