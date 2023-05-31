import pygame
from LVLDAT import Level
from PlatformOBJ import Platform
from PlatformImageOBJ import PlatformImage
from PlayerCharacter import Player
import random
from ED import EndIMG
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
class Level_04(Level):
    """ Definition for level 3. """
 
    def __init__(self, player):
 
        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -3000
 
        # Array with type of platform, and x, y location of the platform.
        level = [
                 [random.randint(1,101), random.randint(1,101), random.randint(1,500)*5, random.randint(300,500)],
                 [random.randint(1,101), random.randint(1,101), random.randint(1,250)*5, random.randint(300,500)],
                 [random.randint(1,101), random.randint(1,101), random.randint(1,300)*5, random.randint(300,500)],
                 [random.randint(1,101), random.randint(1,101), random.randint(1,400)*5, random.randint(300,500)],
                 [random.randint(1,101), random.randint(1,101), random.randint(1,200)*5, random.randint(300,500)],
                 [random.randint(1,101), random.randint(1,101), random.randint(1,50)*5, random.randint(300,500)],
                 [random.randint(1,101), random.randint(1,101), random.randint(1,600)*5, random.randint(300,500)],
                 [random.randint(1,101), random.randint(1,101), random.randint(1,800)*5, random.randint(300,500)],
                 [random.randint(1,101), random.randint(1,101), random.randint(1,200)*5, random.randint(300,500)],
                 [random.randint(1,101), random.randint(1,101), random.randint(1,200)*5, random.randint(300,500)],
                 [random.randint(1,101), random.randint(1,101), random.randint(1,500)*5, random.randint(300,500)],
                 [random.randint(1,101), random.randint(1,101), random.randint(1,250)*5, random.randint(300,500)],
                 [random.randint(1,101), random.randint(1,101), random.randint(1,150)*5, random.randint(300,500)],
                 [random.randint(1,101), random.randint(1,101), random.randint(1,180)*5, random.randint(300,500)],


                 ]
 
        # Go through the array above and add platforms
        for platformimage in level:
            block = PlatformImage(platformimage[0], platformimage[1])
            block.rect.x = platformimage[2]
            block.rect.y = platformimage[3]
            block.player = self.player
            self.imageplatform_list.add(block)
        level = [
                 [0, 0, 3500, 500],
                 ]
        for endimg in level:
            block = EndIMG(endimg[0], endimg[1])
            block.rect.x = endimg[2]
            block.rect.y = endimg[3]
            block.player = self.player
            self.end_list.add(block)
