# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 17:47:55 2018

@author: Robbie Tulip
"""
import numpy as np
from Snake import snake
from Food import food
from json import loads
SETTINGS  = loads(open("gameSettings.json").read())

class board:
    def __init__(self,snake1= None,snake2 = None,food = None):    
        self.__snake1 = snake1
        self.__snake2 = snake2
        self.__food = food
        self.__grid = np.zeros((SETTINGS["BOARD"]["BOARD_SIZE"],SETTINGS["BOARD"]["BOARD_SIZE"]))
        self.draw()
    
    def __str__(self):
        display = ""
        for line in self.__grid:
            display += str(line) 
            display += "\n"
         
        return display

    def __len__(self):
        return SETTINGS["BOARD"]["BOARD_SIZE"]
    
    def draw(self):
        self.__grid = np.zeros((SETTINGS["BOARD"]["BOARD_SIZE"],SETTINGS["BOARD"]["BOARD_SIZE"]))
        if self.__food:
            self.__grid[self.__food[1]][self.__food[0]] = 4
        if self.__snake1:
            for pos in self.__snake1:
                self.__grid[pos[1]][pos[0]] = 1
                if pos == self.__snake1[0]:
                    self.__grid[pos[1]][pos[0]] = 2
        if self.__snake2:
            for pos in self.__snake2:
                self.__grid[pos[1]][pos[0]] = 2
        
    
    def update(self, snake1_dir = None, snake2_dir = None, new_food = False):
        if snake1_dir is not None:
            self.__snake1.set_direction(snake1_dir)
        if snake2_dir is not None:
            self.__snake2.set_direction(snake2_dir)
        if new_food:
            self.__food = new_food
            
        if self.__snake1:
            self.__snake1.move()
        if self.__snake2:
            self.__snake2.move()
        
        self.draw()
    
    def get_snake(self,snake_id):
        if snake_id == 1:
            return self.__snake1
        elif snake_id == 2:
            return self.__snake2
        else:
            print("Invalid Snake id")
    def grow_snake(self,snake_id):
        if snake_id == 1:
            self.__snake1.grow()
        elif snake_id == 2:
            self.__snake2.grow()
        else:
            print("invalid Snake_id")

    def get_entities(self):
        return self.__snake1, self.__snake2, self.__food

    def generate_dnn_data(self):
        data = []
        for i in range(self.__len__()):
            for j in range(self.__len__()):
                data.append(self.__grid[j][i])
        return data
    