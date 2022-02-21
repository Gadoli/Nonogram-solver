# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 19:22:47 2022

@author: david


CSP Projet - Nonogram
black and white
"""

import Nonogram


""" easy one """
print("\nEasy Nonogram")
C_indications = [[2], [1], [4], [1]]
R_indications = [[1], [2], [3], [1 ,1]]
I = [C_indications,R_indications]

game = Nonogram.Nonogram(4,4,I)

print(game)

print("\ntest naive solver")
game.naiveSolver(-1, game.getEmptyGrid())

print(game)
print()


""" medium one """
print("\nMedium Nonogram")
C = [[1], [1], [1], [2,1], [2], [3], [1], [1,1], [1,3], [3]]
R = [[2], [2, 1], [7], [1,1], [4,1,2]]
M = [C,R]

game2 = Nonogram.Nonogram(10,5,M)

print(game2)
# game2.naiveSolver(-1, game2.getEmptyGrid())

print("\nSolving this one with the naive solver would take a lot of time...")
print("2**50 node to check !!!")
print("Another solver must be used - work in progress")