import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 600
class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ You can do stuff on it.
            """
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.type = "blank"
        self.moves = 0
        self.rect = self.image.get_rect()
        
