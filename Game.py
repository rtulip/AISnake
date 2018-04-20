# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 19:13:00 2018

@author: Robbie Tulip
"""
from json import loads
from random import sample
from threading import Thread
from time import sleep
import sys

from Snake import snake
from Food import food
from Board import board

sys.path.append('D:\Py Workspace\AIFramework')
from Network import network
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
            self.__board = board(snake1 = s1,food = f)
        elif num_players == 2:
            print (s1, s2)
            self.__board = board(snake1 = s1, snake2 = s2, food = f)
        
        print(self.__board)
        self.__food_flag = False
        self.EXIT = False
        
        self.n = network(SETTINGS["BOARD"]["BOARD_SIZE"]**2+3,2,32,3)
        
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
        print(s1.direction())
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
        return True       

    def game_loop(self):
        print("START")
        print(self.__board)
        s1, s2, f = self.__board.get_entities()
        dir1 = s1.direction()
        dir2 = None
        while self.analyze_board() and not self.EXIT:
            
            if self.__food_flag:
                self.__board.update(dir1,dir2,self.generate_food())
                self.__food_flag = False
            else:
                
                self.__board.update(dir1,dir2)
            print(self.__board)
            if s1:
                instructions = [-1,0,1]
                
                input = self.__board.generate_dnn_data()
                input.append(self.__board.get_snake(1).direction())
                input.append(len(self.__board.get_snake(1)))
                input.append(1)
                output = self.n.iterate(input)
                print(output)
                #test = sample(instructions,1)
                dir1 += (output.index(max(output))-1)
                
                if dir1 < 0:
                    dir1 = 3
                if dir1 >3:
                    dir1 = 0
            if s2:
                dir2 = s1.direction()
            self.__board.get_snake(1).set_direction(dir1)
            
            sleep(0.5)
            
        
g = game(1)
input("Press A button to end")
g.EXIT = True