import pygame
import os
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 600
Blocktypes = ["SpeedBlock"]
class PlatformImage(pygame.sprite.Sprite):
    """ Area that speeds up the player """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.image.load(os.path.join('blockimages', "%s.gif" % (random.choice(Blocktypes)))).convert()
 
        self.rect = self.image.get_rect()
    
