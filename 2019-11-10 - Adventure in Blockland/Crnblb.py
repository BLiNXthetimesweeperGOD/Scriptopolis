import random
import pygame
import os
class Chronoblob(pygame.sprite.Sprite):
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
        self.image = pygame.image.load(os.path.join('images', "FinalChronoblob.gif")).convert()

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
        #Fall speed cap
        if self.change_y > 20:
                self.change_y = 20
        # Move left/right
        self.rect.x += self.change_x
            
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.rect < block.rect:    
                self.rect.right = block.rect.left
            #Do the opposite if moving left
            if block.rect.right < self.rect.top:    
                self.rect.left = block.rect.right
        # See if we hit anything
        #"Fast" physics data
        block_hit_list = pygame.sprite.spritecollide(self, self.level.fast_list, False)
        for block in block_hit_list:
            # If we are inside the block, set our speed to 50.
            self.image = pygame.image.load(os.path.join('images',"FinalChronoblob.gif")).convert()
            if self.rect.right > block.rect.left:    
                self.change_x=50
        block_hit_list = pygame.sprite.spritecollide(self, self.level.bfast_list, False)
        for block in block_hit_list:
            # If we are inside the block, set our speed to -50.
            self.image = pygame.image.load(os.path.join('images', "FinalChronoblob.gif")).convert()
            if self.rect.right > block.rect.left:    
                self.change_x = -50
        block_hit_list = pygame.sprite.spritecollide(self, self.level.imageplatform_list, False)
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            
            # Stop our vertical movement
            self.change_y = 0
        block_hit_list = pygame.sprite.spritecollide(self, self.level.imageplatform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.change_y = -6
            elif self.change_y < 0:
                self.change_y = -6
            # Add "Boing" sound here
            self.change_y = -50
        block_hit_list = pygame.sprite.spritecollide(self, self.level.wimageplatform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.change_y = -6
            elif self.change_y < 0:
                self.change_y = -6
            # Add "Boing" sound here
            self.change_y = -20
 

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
                # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
    def jump(self):
        """ Called when chronoblob hits ground. """
 
        # move down a bit and see if there is a platform below.
        # Move down 2 pixels because it doesn't work well if it only moves down 1
        # when working with a platform moving down.
        self.rect.y += 5
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        # If it is ok to jump, set speed upwards
        
        if len(platform_hit_list) > 0:
            self.change_y = -10
    def go_left(self):
        """ Called when the chronoblob hits a wall. """
        self.change_x = -6
    def go_right(self):
        """ Called when the chronoblob hits a wall. """
        self.change_x = 6
