from animation import animation
import math
from gameobject import gameObject
from globals import globals

class attack():

    def __init__(self, name, attackNum, damage, type, attackSpecs, effects, animation, ):
        self.name = name
        self.damage = damage
        self.type = type
        self.attack_specs = attackSpecs
        self.effects = effects
        self.animation = animation
        self.attack_num = attackNum

    def update(self, target):
            if(self.type == "projectile"):
                if(self.animation.iteration < 1):
                    if(target.animation.currentFrame < self.animation.length-1):
                        if (target.animation == target.hero.default_animation):
                            target.animation = self.animation
                    else:
                        globals.gameObjects.append(gameObject(self.attack_specs[1], target.x + math.cos(math.radians(target.angle)) * self.attack_specs[2], target.y + math.sin(math.radians(target.angle)) * self.attack_specs[3], target.sprite.angle, self.attack_specs[0], 1))
                        target.animation = target.hero.default_animation
                        self.animation.iteration = 0
                        self.animation.currentFrame = 0
                        target.currentAttack = None