# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:56:20 2019

@author: almon
"""
import numpy as np


def monty_hall(choice, doors=[1, 2, 3], switch=True):
    # Choose the winning door
    money_door = np.random.choice(doors)

    # If you choose the winning door and you switched then you lose
    if choice == money_door:
        return not switch

    # If you did not chose the winning door and you switch then you win
    return switch


switch = True
n = 10000
i = 0
wins = 0
doors = [1, 2, 3]
while i < n:
    # Choose the door at random
    choice = np.random.choice(doors)
    wins += monty_hall(choice, doors, switch)
    i += 1

prob_win = wins/n
print(prob_win, 1 - prob_win)
