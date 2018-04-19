# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 19:13:00 2018

@author: Robbie Tulip
"""
from json import loads
from random import sample
from threading import Thread

from Snake import snake
from Food import food
from Board import board


SETTINGS  = loads(open("gameSettings.json").read())

class game:
    
    def __init__(self,num_players):
        
        if num_players == 1:
            s1 = snake(player = 0)
        elif num_players == 2:
            s1 = snake(player = 0)
            s2 = snake(player = 1)
        else:
            return ("Invalid Number of Players")
        
        self.__locs = list(range(SETTINGS["BOARD"]["BOARD_SIZE"]))
        if num_players == 1:
            f = self.generate_food(snake1 = s1)
        elif num_players == 2:
            f = self.generate_food(snake1 = s1,snake2 = s2)

        if num_players == 1:
            print (s1)
            self.__board = board(snake1 = s1,food = food(6,1))
        elif num_players == 2:
            print (s1, s2)
            self.__board = board(snake1 = s1, snake2 = s2, food = f)
        
        print(self.__board)
        self.__food_flag = False
        self.__loop = Thread(target = self.game_loop)
        self.__loop.start()
                
    def generate_food(self, snake1 = None, snake2 = None):  
        f = sample(self.__locs,2)
        if snake1 and snake2:
            while f in snake1 or f in snake2:
                f = sample(self.__locs,2)
        elif snake1:
            while f in snake1:
                f = sample(self.__locs,2)
        elif snake2:
            while f in snake2:
                f = sample(self.__locs,2)
        return food(f[0],f[1])
        
    def analyze_board(self):
        s1, s2, f = self.__board.get_entities()
        if s1 and s2:
            for loc in s1:
                if loc in s2:
                    print("COLLISION")
                    return False
        if s1:
            dir = s1.direction()
            if dir == SETTINGS["SNAKE"]["NORTH"]:
                if s1[0][1] == 0:
                    return False
                    
                if [s1[0][0],s1[0][1]-1] in s1:
                    return False
            elif dir == SETTINGS["SNAKE"]["EAST"]:
                if s1[0][0] == SETTINGS["BOARD"]["BOARD_SIZE"]-1:
                    return False
                
                if [s1[0][0]+1,s1[0][1]] in s1:
                    return False
            elif dir == SETTINGS["SNAKE"]["SOUTH"]:
                if s1[0][1] == SETTINGS["BOARD"]["BOARD_SIZE"]-1:
                    return False
                
                if [s1[0][0],s1[0][1]+1] in s1:
                    return False
            elif dir == SETTINGS["SNAKE"]["WEST"]:
                if s1[0][0] == 0:
                    return False
                
                if [s1[0][0]-1,s1[0][1]] in s1:
                    return False
            
        if s2:
            dir = s2.direction()
            if dir == SETTINGS["SNAKE"]["NORTH"]:
                if s2[0][1] == 0:
                    return False
                    
                if [s2[0][0],s2[0][1]-1] in s2:
                    return False
            elif dir == SETTINGS["SNAKE"]["EAST"]:
                if s2[0][0] == SETTINGS["BOARD"]["BOARD_SIZE"]-1:
                    return False
                
                if [s2[0][0]+1,s2[0][1]] in s2:
                    return False
            elif dir == SETTINGS["SNAKE"]["SOUTH"]:
                if s2[0][1] == SETTINGS["BOARD"]["BOARD_SIZE"]-1:
                    return False
                
                if [s2[0][0],s2[0][1]+1] in s2:
                    return False
            elif dir == SETTINGS["SNAKE"]["WEST"]:
                if s2[0][0] == 0:
                    return False
                
                if [s2[0][0]-1,s2[0][1]] in s2:
                    return False
        
        if s1 and f.get_location() in s1:
            print("Grow S1")
            self.__board.grow_snake(1)
            self.__food_flag = True
        elif s2 and f.get_location() in s2:
            self.__board.grow_snake(2)
            self.__food_flag = True

        print("ALL GOOD")
        return True       

    def game_loop(self):
        print(self.__board)
        while self.analyze_board():
            s1, s2, f = self.__board.get_entities()
            dir1 = None
            dir2 = None
            if s1:
                dir1 = s1.direction()
            if s2:
                dir2 = s1.direction()
            if self.__food_flag:
                self.__board.update(dir1,dir2,self.generate_food())
                self.__food_flag = False
            else:
                self.__board.update(dir1,dir2)
            print(self.__board)
        
g = game(1)