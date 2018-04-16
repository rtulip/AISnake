# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 19:39:23 2018

@author: Robbie Tulip
"""

class food:
    
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        
    def __str__(self):
        return str(self.get_location())
    
    def get_location(self):
        return [self.__x,self.__y]
    
    
    