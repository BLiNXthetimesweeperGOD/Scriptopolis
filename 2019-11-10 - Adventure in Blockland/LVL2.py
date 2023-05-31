print("Speed_Test")
import pygame
from LVLDAT import Level
from PlatformOBJ import Platform
from PlatformImageOBJ import PlatformImage
from PlayerCharacter import Player
from FastOBJ import Fast
import random
from ED import EndIMG
from BKFastObj import LFast
from Crnblb import Chronoblob
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (100, 100, 255)

class Level_02(Level):
    """ Definition for the test level. """
    
    def __init__(self, player):
        cblob = Chronoblob()
        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -9000
        #Normal Platforms
        # Array with width, height, x, and y of platform
        level = [[9900, 9900, 210, 600],
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            block.cblob = self.cblob
            
            self.platform_list.add(block)
        # Array with type of platform, and x, y location of the platform.
        #Water Platforms
        level = [
                 [150, 125, 2000, 599],


                 ]
 
        # Go through the array above and add platforms
        for platformimage in level:
            block = PlatformImage(platformimage[0], platformimage[1])
            block.rect.x = platformimage[2]
            block.rect.y = platformimage[3]
            block.player = self.player
            block.cblob = self.cblob
            
            self.imageplatform_list.add(block)
        #Speed Block
        level = [[100, 100, 1000, 450],
                 [100, 100, 1500, 450],
                 ]
        for fast in level:
            block = Fast(fast[0], fast[1])
            block.rect.x = fast[2]
            block.rect.y = fast[3]
            block.player = self.player
            block.cblob = self.cblob
            
            self.fast_list.add(block)
