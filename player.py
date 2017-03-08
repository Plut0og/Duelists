from sprite import sprite
import math
import pygame
from area import hitBox
from globals import globals
from gamedata import gameData

class player():

    def __init__(self, name, initX, initY, hero):
        self.name = name
        self.hero_path = hero
        self.hero = gameData.heroes[self.hero_path]
        self.orig_image = self.hero.image
        self.image = self.hero.image

        self.x = initX
        self.y = initY
        self.angle = 0

        self.sprite = sprite(self)

        self.animation = self.hero.default_animation
        self.currentAttack = None
        self.data = [self.hero_path, self.x, self.y, self.angle, self.currentAttack, self.animation]

        self.rotate(self.angle)

    def moveTo(self, x, y):
        self.x = x
        self.y = y

    def moveForwards(self):
        angle = math.radians(self.angle)
        self.x += math.cos(angle + math.pi / 2) * self.hero.move_speed
        self.y -= math.sin(angle + math.pi / 2) * self.hero.move_speed

    def moveBackwards(self):
        angle = math.radians(self.angle)
        self.x += math.cos(angle - math.pi / 2) * self.hero.move_speed
        self.y -= math.sin(angle - math.pi / 2) * self.hero.move_speed

    def rotate(self, rotation):
        orig_rect = self.orig_image.get_rect()
        rot_image = pygame.transform.rotate(self.orig_image, rotation)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        self.image = rot_image

        self.angle = rotation

    def rotateLeft(self):
        orig_rect = self.orig_image.get_rect()
        rot_image = pygame.transform.rotate(self.orig_image, self.angle + self.hero.rotation_speed)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        self.image = rot_image

        self.angle += self.hero.rotation_speed

    def rotateRight(self):
        orig_rect = self.orig_image.get_rect()
        rot_image = pygame.transform.rotate(self.orig_image, self.angle - self.hero.rotation_speed)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        self.image = rot_image

        self.angle -= self.hero.rotation_speed

    def fight(self, attack):
        self.currentAttack = self.hero.attacks[attack]

    def update(self):
        self.orig_image = self.animation.run()

        if(self.currentAttack != None):
            self.currentAttack.update(self)
        else:
            self.orig_image = self.hero.image
        self.rotate(self.angle)
        self.sprite.update()

        self.data = [self.hero_path, self.x, self.y, self.angle, self.currentAttack, self.animation]

    def draw(self):
        self.sprite.draw()

