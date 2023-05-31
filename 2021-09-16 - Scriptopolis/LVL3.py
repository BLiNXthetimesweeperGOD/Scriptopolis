import pygame
from LVLDAT import Level
from PlatformOBJ import Platform
#from backdrop import BGL
from PlatformImageOBJ import PlatformImage
from PlayerCharacter import Player
import random
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255,100,100)
PURPLE = (255,0,255)
GRAY = (100,100,100)
class Level_03(Level):
    """ Definition for level 1. """
    def __init__(self, player):
        """ Create level 1. """
        #Platform types are in this list for level creation purposes:
        types = ["spawn",#Where the player starts                                              (0)
                 "",#The main floor type                                                       (1)
                 "normal",#Same as ""                                                          (2)
                 "up",#Acts as an elevator going up                                            (3)
                 "down",#Acts as an elevator going down                                        (4)
                 "bouncy",#Trampoline-like, sends you higher with each bounce up to 10 bounces (5)
                 "fall",#Falls out of the world                                                (6)
                 "flyup",#Flies away                                                           (7)
                 "pullup",#Pulls the player to it                                              (8)
                 "pulldown",#Pulls the player to it                                            (9)
                 "pullleft",#Pulls the player to it                                           (10)
                 "pullright",#Pulls the player to it                                          (11)
                 "vanish",#Vanishes on contact                                                (12)
                 "hazard",#Dangerous to touch                                                 (13)
                 "fast",#Speeds the player up                                                 (14)
                 "slow",#Slows the player down                                                (15)
                 "reset",#Sends the player back to the start of the level                     (16)
                 "goal",#Completes the level if another level exists after the current one    (17)
                 "pushable",#You can push these                                               (18)
                 "timed",#Vanishes and reappears on a timer                                   (19)
                 "slideleft",#Moves the player to the left                                    (20)
                 "slideright",#Moves the player to the right                                  (21)
                 ]
        # Call the parent constructor
        Level.__init__(self, player)
        self.level_limit = -2500
        #Level platform list
        level = [
                 [1, 1, 0, 0, 0],
                 [8, 1, 1, 0, 1],
                 [1, 10, 9, 0, 1],
                 [25, 1, 5, 5, 1],
                 [25, 1, 30, 5, 5],
                 [4, 8, 55, 5, 4],
                 [11, 8, 59,3, 3],
                 #[1, 60, 1000, -2, 11],
                 ]
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0]*100, platform[1]*100)
            block.rect.x = platform[2]*100
            block.rect.y = platform[3]*100
            block.type = types[platform[4]]
            if block.type == "up":
                block.image.fill(GREEN)
            if block.type == "down":
                block.image.fill(RED)
            if block.type == "bouncy":
                block.image.fill(BLUE)
            if block.type == "" or block.type == "normal":
                block.image.fill(WHITE)
            if block.type.startswith("pull"):
                block.image.fill(GRAY)
            if block.type == "spawn":
                block.image.fill(PURPLE)
                player.rect.bottom = block.rect.top
            #block.player = self.player
            self.platform_list.add(block)
