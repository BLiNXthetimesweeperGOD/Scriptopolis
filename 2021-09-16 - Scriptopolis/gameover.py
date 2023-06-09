import pygame
from LVLDAT import Level
from PlatformOBJ import Platform
from PlatformImageOBJ import PlatformImage
from PlayerCharacter import Player
import random
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
class GMOVER(Level):
    """ Used as a way to prevent the player from dying too much """
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
         
        self.level_limit = -250000
        # Array with width, height, x, and y of platform
        types = [["left"]]
        level = [[10, 1000, 0, 1000, ""],
                 [100, 100, 0, 380, ""],
                 [100, 100, 100, 380, "up"],
                 [100, 100, 200, 380, "down"],
                 [100, 100, 300, 380, ""]]
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.type = platform[4]
            block.player = self.player
            self.platform_list.add(block)

##        # Go through the array above and add platforms
##        for platformimage in level:
##            block = PlatformImage(platformimage[0], platformimage[1])
##            block.rect.x = platformimage[2]
##            block.rect.y = platformimage[3]
##            block.player = self.player
##            self.imageplatform_list.add(block)
# Create platforms for the level
