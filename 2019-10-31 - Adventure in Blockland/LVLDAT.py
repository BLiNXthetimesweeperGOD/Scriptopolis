import pygame
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

from PlatformOBJ import Platform
from PlatformImageOBJ import PlatformImage
from PlayerCharacter import Player
from ED import EndIMG

class Level():
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.imageplatform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.end_list = pygame.sprite.Group()
        self.player = player

 
        # How far this world has been scrolled left/right
        self.world_shift = 0
 
    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.imageplatform_list.update()
        self.end_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        screen.fill(BLACK)
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.imageplatform_list.draw(screen)
        self.end_list.draw(screen)
        self.enemy_list.draw(screen)
 
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
        for platformimage in self.imageplatform_list:
            platformimage.rect.x += shift_x
        for endimg in self.end_list:
            endimg.rect.x += shift_x
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
 
 
# Create platforms for the level
from LVL1 import Level_01
from LVL2 import Level_02
from LVL3 import Level_03
from LVL4 import Level_04
