# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 17:53:22 2018

@author: Robbie Tulip
"""
from copy import deepcopy
from json import loads
SETTINGS  = loads(open("gameSettings.json").read())

class snake:
    
    def __init__(self,player = 0):
        self.__x_locs = []
        self.__y_locs = []
        self.__score = 0
        self.__direction = SETTINGS["SNAKE"]["EAST"]
        if player == 0:
            self.__x_locs = [i for i in range(SETTINGS["SNAKE"]["START_X"]+SETTINGS["SNAKE"]["START_SIZE"]-1,SETTINGS["SNAKE"]["START_X"]-1,-1)]
            self.__y_locs = [SETTINGS["SNAKE"]["START_Y"] for i in range(SETTINGS["SNAKE"]["START_SIZE"])]
            
    def __str__(self):
        return str([[self.__x_locs[i],self.__y_locs[i]] for i in range(len(self.__x_locs))])
    
    def __getitem__(self,idx):
        if 0 <= idx < len(self.__x_locs):
            return [self.__x_locs[idx],self.__y_locs[idx]]
        elif -len(self.__x_locs) <= idx < 0:
            return [self.__x_locs[idx],self.__y_locs[idx]]
        else:
            raise IndexError
        
    def __len__(self):
        return len(self.__x_locs)
    def get_location(self):
        return [[self.__x_locs[i],self.__y_locs[i]] for i in range(len(self.__x_locs))]
    
    def set_location(self,new_location):
        self.__x_locs = [new_location[i][0] for i in range(len(new_location))]
        self.__y_locs = [new_location[i][1] for i in range(len(new_location))]
        self.__score = len(new_location) - SETTINGS["SNAKE"]["START_SIZE"]
    
    def direction(self):
        return self.__direction
    
    def set_direction(self,new_direction):
        if new_direction in [SETTINGS["SNAKE"]["NORTH"],SETTINGS["SNAKE"]["EAST"],SETTINGS["SNAKE"]["SOUTH"],SETTINGS["SNAKE"]["WEST"]]:
            self.__direction = new_direction
    
    def score(self):
        return self.__score
    
    def move(self):
        new_location = self.get_location()
        for i in range(len(new_location)-1,0,-1):
            new_location[i] = deepcopy(new_location[i-1])
        if self.__direction == SETTINGS["SNAKE"]["NORTH"]:
            new_location[0][1] -= 1
        elif self.__direction == SETTINGS["SNAKE"]["EAST"]:
            new_location[0][0] += 1
        elif self.__direction == SETTINGS["SNAKE"]["SOUTH"]:
            new_location[0][1] += 1
        elif self.__direction == SETTINGS["SNAKE"]["WEST"]:
            new_location[0][0] -= 1
        self.set_location(new_location)
        
    def grow(self):
        new_location = self.get_location()
        new_location.append(deepcopy(new_location[-1]))
        self.set_location(new_location)    