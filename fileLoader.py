import json
import pygame
from hero import hero
from attack import attack
from area import area
from area import hitBox
from effect import effect
from gamedata import gameData
from animation import animation as anim

class fileLoader():
    def __init__(self, filesystem):
        self.file_system = filesystem

    def loadHeroes(self):
        file_data = open(self.file_system + "/Heroes.json")
        data = json.load(file_data)
        for a, HERO in enumerate(data.keys()):
            name = data[HERO]["name"]
            image = data[HERO]["image"]

            animations = []
            def_anim_num = data[HERO]["defaultAnimation"]["number"]
            def_anim_length = data[HERO]["defaultAnimation"]["length"]
            def_anim_frames = []
            for ab, frame in enumerate(data[HERO]["defaultAnimation"]["frames"]):
                def_anim_frames.append(pygame.image.load(data[HERO]["defaultAnimation"]["frames"][ab]))
            default_animation = anim(def_anim_num, def_anim_length, def_anim_frames)
            animations.append(default_animation)
            move_speed = data[HERO]["stats"]["moveSpeed"]
            rotation_speed = data[HERO]["stats"]["rotationSpeed"]
            attacks = []
            for b, Attack in enumerate(data[HERO]["Attacks"].keys()):
                attack_name = data[HERO]["Attacks"][Attack]["name"]
                attack_num = data[HERO]["Attacks"][Attack]["number"]
                attack_damage = data[HERO]["Attacks"][Attack]["damage"]
                attack_type = data[HERO]["Attacks"][Attack]["type"]
                attack_specs = []
                if attack_type == "projectile":
                    attack_specs.append(data[HERO]["Attacks"][Attack]["projectile"]["speed"])
                    attack_specs.append(pygame.image.load(data[HERO]["Attacks"][Attack]["projectile"]["image"]))
                    attack_specs.append(data[HERO]["Attacks"][Attack]["projectile"]["startRelX"])
                    attack_specs.append(data[HERO]["Attacks"][Attack]["projectile"]["startRelY"])
                    zones = []
                    for c, Zone in enumerate(data[HERO]["Attacks"][Attack]["projectile"]["hitBox"]):
                        zones.append(area(data[HERO]["Attacks"][Attack]["projectile"]["hitBox"][c]["startX"], data[HERO]["Attacks"][Attack]["projectile"]["hitBox"][c]["startY"], data[HERO]["Attacks"][Attack]["projectile"]["hitBox"][c]["width"], data[HERO]["Attacks"][Attack]["projectile"]["hitBox"][c]["height"]))

                    attack_specs.append(zones)
                effects = []
                for d, eff in enumerate(data[HERO]["Attacks"][Attack]["mods"].keys()):
                    health_mod = data[HERO]["Attacks"][Attack][eff]["healthMod"]
                    interval = data[HERO]["Attacks"][Attack][eff]["interval"]
                    repeat = data[HERO]["Attacks"][Attack][eff]["repeat"]
                    effects.append(effect(health_mod, interval, repeat))
                animation_num = data[HERO]["Attacks"][Attack]["animation"]["number"]
                animation_length = data[HERO]["Attacks"][Attack]["animation"]["length"]
                animation_frames = []
                for e, Frame in enumerate(data[HERO]["Attacks"][Attack]["animation"]["frames"]):
                    animation_frames.append(pygame.image.load(data[HERO]["Attacks"][Attack]["animation"]["frames"][e]))
                animation = anim(animation_num, animation_length, animation_frames)
                animations.append(animation)
                attacks.append(attack(attack_name, attack_num, attack_damage, attack_type, attack_specs, effects, animation))

            gameData.heroes.append(hero(name, image, animations, move_speed, rotation_speed, attacks))


