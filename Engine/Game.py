#!/usr/bin/env python3
from GameEngine.Player import Player
from GamePlatform.Platform import Platform

if __name__ == '__main__':
    p1 = Player("Anton", "ai", "hard")
    p2 = Player("Tor", "user")

    p = Platform(p1, p2)
    p.startGame()