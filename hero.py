import pygame


class hero():

    def __init__(self, name, img, animations, move_speed, rotation_speed, attacks):
        self.name = name
        self.animations = animations
        self.image = pygame.image.load(img)
        self.default_animation = self.animations[0]
        self.move_speed = move_speed
        self.rotation_speed = rotation_speed

        self.attacks = attacks