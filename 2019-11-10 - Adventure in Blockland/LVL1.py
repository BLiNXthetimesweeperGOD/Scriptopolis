print("Platform_Test")
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

class Level_01(Level):
    """ Definition for the test level. """
    
    def __init__(self, player):
        cblob = Chronoblob()
        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -3000
        #Normal Platforms
        # Array with width, height, x, and y of platform
        level = [[5000, 9900, 210, 600],
                 [5000, 9900, -4790, 300],
                 [340, 125, 210, 400],
                 [100, 305, 700, 400],
                 [100, 150, 800, 500],
                 [500, 305, 700, -2800],
                 [500, 305, 1200, -2900],
                 
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
                 [150, 125, 550, 400],


                 ]
 
        # Go through the array above and add platforms
        for platformimage in level:
            block = PlatformImage(platformimage[0], platformimage[1])
            block.rect.x = platformimage[2]
            block.rect.y = platformimage[3]
            block.player = self.player
            block.cblob = self.cblob
            
            self.imageplatform_list.add(block)
        
        level = [
                 [150, 125, 2400, 599],
                 ]
        for wplatformimage in level:
            block = PlatformImage(wplatformimage[0], wplatformimage[1])
            block.rect.x = wplatformimage[2]
            block.rect.y = wplatformimage[3]
            block.player = self.player
            block.cblob = self.cblob
            
            self.wimageplatform_list.add(block)
        #Speed Block
        level = [[100, 100, 1000, 400],
                 [100, 100, -3000, 100],
                 ]
        for fast in level:
            block = Fast(fast[0], fast[1])
            block.rect.x = fast[2]
            block.rect.y = fast[3]
            block.player = self.player
            block.cblob = self.cblob
            
            self.fast_list.add(block)
        #Left Speed Block
        level = [[100, 100, 3000, 200],
                 ]
        for bfast in level:
            block = LFast(bfast[0], bfast[1])
            block.rect.x = bfast[2]
            block.rect.y = bfast[3]
            block.player = self.player
            block.cblob = self.cblob
            
            self.bfast_list.add(block)
        #Ending image
        level = [
                 [0, 0, 3500, 480],
                 ]
        for endimg in level:
            block = EndIMG(endimg[0], endimg[1])
            block.rect.x = endimg[2]
            block.rect.y = endimg[3]
            block.player = self.player
            block.cblob = self.cblob
            self.end_list.add(block)
