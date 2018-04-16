# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 17:47:55 2018

@author: Robbie Tulip
"""
import np

BOARD_SIZE = 15

class board(snake1= None,snake2 = None,food = None):
    self.__snake1 = snake1
    self.__snake2 = snake2
    self.__food = food
    
    self.__grid = np.zeros(BOARD_SIZE,BOARD_SIZE)
    