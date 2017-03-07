import math
import pygame
from globals import globals

class sprite():
    def __init__(self, target):
        self.target = target
        self.image = target.image
        self.x = target.x
        self.y = target.y
        self.angle = target.angle


    def update(self):
        self.image = self.target.image
        self.x = self.target.x
        self.y = self.target.y
        self.angle = self.target.angle


    def draw(self):
        globals.gameDisplay.blit(self.image, (self.x, self.y))