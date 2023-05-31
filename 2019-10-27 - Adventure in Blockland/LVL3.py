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
class Level_03(Level):
    """ Definition for level 3. """
 
    def __init__(self, player):
 
        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000
        
        # Array with type of platform, and x, y location of the platform.
        level = [
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
