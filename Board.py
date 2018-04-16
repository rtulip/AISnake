# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 17:47:55 2018

@author: Robbie Tulip
"""
import numpy as np
from Snake import snake
BOARD_SIZE = 6

class board:
    def __init__(self,snake1= None,snake2 = None,food = None):    
        self.__snake1 = snake1
        self.__snake2 = snake2
        self.__food = food
        
        self.__grid = np.zeros((BOARD_SIZE,BOARD_SIZE))
        if self.__snake1:
            for xy in self.__snake1.get_location():
                self.__grid[xy[1]][xy[0]] = 1
        if self.__snake2:
            for xy in self.__snake2.get_location():
                self.__grid[xy[0]][xy[1]] = 2
        if self.__food:
            self.__grid[self.__food[0]][self.__food[1]]
    
    def __str__(self):
        return str(self.__grid) + "\n"
    
s = snake()
b = board(snake1= s)
print(b)

s.move()
b = board(snake1 = s)
print(b)

s.set_direction(2)
s.move()
b = board(snake1 = s)
print(b)