import pygame
from LVLDAT import Level
from PlatformOBJ import Platform
from PlayerCharacter import Player
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
class Level_01(Level):
    """ Definition for level 1. """
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.level_limit = -100
 
        # Array with width, height, x, and y of platform
        level = [[20, 20, 210, 500],
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player

            self.platform_list.add(block)

        level = [[20, 70, 210, 400],
                 ]
 
# Create platforms for the level
