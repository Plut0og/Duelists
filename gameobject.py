from sprite import sprite
import math
import pygame

class gameObject():
    def __init__(self, image, x, y, angle, move_speed, rotation_speed):
        self.orig_image = image
        self.image = image
        self.x = x
        self.y = y
        self.angle = angle
        self.move_speed = move_speed
        self.rotation_speed = rotation_speed
        self.sprite = sprite(self)

    def moveForwards(self):
        angle = math.radians(self.angle)
        self.x += math.cos(angle + math.pi / 2) * self.move_speed
        self.y -= math.sin(angle + math.pi / 2) * self.move_speed

    def rotate(self, rotation):
        orig_rect = self.orig_image.get_rect()
        rot_image = pygame.transform.rotate(self.orig_image, self.angle + rotation)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        self.image = rot_image

    def update(self):
        self.rotate(0)
        self.moveForwards()
        self.sprite.update()

    def draw(self):
        self.sprite.draw()