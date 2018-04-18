# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 17:47:55 2018

@author: Robbie Tulip
"""
import numpy as np
from Snake import snake
from Food import food
BOARD_SIZE = 10

class board:
    def __init__(self,snake1= None,snake2 = None,food = None):    
        self.__snake1 = snake1
        self.__snake2 = snake2
        self.__food = food
        
        self.__grid = np.zeros((BOARD_SIZE,BOARD_SIZE))
        self.draw()
    
    def __str__(self):
        display = ""
        for line in self.__grid:
            display += str(line) 
            display += "\n"
         
        return display
    
    def draw(self):
        self.__grid = np.zeros((BOARD_SIZE,BOARD_SIZE))
        if self.__food:
            self.__grid[self.__food[1]][self.__food[0]] = 4
        if self.__snake1:
            for xy in self.__snake1.get_location():
                self.__grid[xy[1]][xy[0]] = 1
        if self.__snake2:
            for xy in self.__snake2.get_location():
                self.__grid[xy[1]][xy[0]] = 2
        
    
    def update(self, snake1_dir = None, snake2_dir = None, new_food = False):
        if snake1_dir:
            self.__snake1.set_direction(snake1_dir)
        if snake2_dir:
            self.__snake2.set_direction(snake2_dir)
        if new_food:
            self.__food = new_food
            
        if self.__snake1:
            self.__snake1.move()
        if self.__snake2:
            self.__snake2.move()
        
        self.draw()
        
    def grow_snake(self,snake_id):
        if snake_id == 1:
            self.__snake1.grow()
        elif snake_id == 2:
            self.__snake2.grow()
        else:
            print("invalid Snake_id")
         
        
s = snake()
f = food(4,2)
b = board(s,food = f)

print(b)
b.update()
print(b)
b.update(snake1_dir=2)
print(b)
b.grow_snake(1)
b.update(new_food = food(7,7))
print(b)
