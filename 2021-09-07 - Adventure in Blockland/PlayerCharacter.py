import math
import os
import pygame
import random
from pygame.locals import *
import statistics as st
idleimage = ["PL1"]
PL = ["PL0", "PL1", "PL3", "PL4", "PL3", "PL1", "PL0"]
PR = ["PR0", "PR1", "PR3", "PR4", "PR3", "PR1", "PR0"]
PI = ["PIL", "PIR"]
PS = ["PLSL", "PLSR"]
PF = ["PFALL", "PFALR", "PFALL2", "PFALR2"]
PH = ["Head1"]

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
class Player(pygame.sprite.Sprite):
    
    """
    This class represents the bar at the bottom that the player controls.
    """
    # -- Methods
    def __init__(self):
        self.time = []
        self.fade = 255
        self.fade2 = 255
        self.fade3 = 255
        self.died = False
        self.framepause = 0
        self.state = "Idle"
        self.Direction = 1
        #store blocks for later use (not implemented yet!)
        self.inventory = []
        """ Constructor function """
        self.jumps = 0
        # Call the parent's constructor
        super().__init__()
        self.stage = 0
        self.stageM = 1
        self.timer = 0
        self.totalseconds = 0
        self.image = pygame.image.load(os.path.join('images', "PIR.gif")).convert()
        #self.head = pygame.image.load(os.path.join('images', "Head1.gif")).convert()
        #self.head.bottom = self.image.top
        self.frame = 0
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        #self.head = self.head.get_rect()
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
        self.anim = 0.0
        self.falltime = 0
        # List of sprites we can bump against
        self.level = None   
    def update(self):
        
        """ Move the player. """
        # Gravity
        self.calc_grav()
        if self.rect.y >=480:
            for block in self.level.platform_list:
                #print(self.level.platform_list)
                if block.rect.x <= self.rect.x:
                #    print(block.rect)
                    self.rect.y=block.rect.y-200
                    self.rect.x=block.rect.x
        pcH = [self.rect.top, self.rect.bottom]
        pcW = [self.rect.left, self.rect.right]
        midH = st.median(pcH)
        midW = st.median(pcW)
        pcH.clear()
        pcW.clear()
        if self.state == "WLeft":
            self.change_x -= 0.25
            if self.change_x <= -15:
                self.change_x = -15
            #if self.change_x <= -20:
            #    self.change_x = -20
            if self.change_y == 1:
                self.framepause += 1
                if self.framepause >= 2:
                    self.Direction = 0
                    self.frame+=1
                    if self.frame >= 4:
                        self.frame = 0
                    self.framepause = 0
                #self.head = pygame.image.load(os.path.join('images', "Head1.gif")).convert()
                self.image = pygame.image.load(os.path.join('images', PL[self.frame]+".gif")).convert()
            else:
                if self.frame == 4:
                    self.frame = 0
                if self.change_y <= 0:
                    #print(self.change_y)
                    #self.head = pygame.image.load(os.path.join('images', PH[0]+".gif")).convert()
                    self.image = pygame.image.load(os.path.join('images', PF[self.Direction]+".gif")).convert()
                elif self.change_y >= 2:
                    #print(self.change_y)
                    #self.head = pygame.image.load(os.path.join('images', "Head1.gif")).convert()
                    self.image = pygame.image.load(os.path.join('images', PF[self.Direction+2]+".gif")).convert()
            
        
        if self.state == "Idle":
            if self.frame >= 4:
                self.frame = 0
            if self.change_y == 1:
                #print(self.change_y)
                self.image = pygame.image.load(os.path.join('images', PI[self.Direction]+".gif")).convert()
            if self.change_y <= 0:
                #print(self.change_y)
                self.image = pygame.image.load(os.path.join('images', PF[self.Direction]+".gif")).convert()
            elif self.change_y >= 2:
                #print(self.change_y)
                self.image = pygame.image.load(os.path.join('images', PF[self.Direction+2]+".gif")).convert()
        if self.state == "WRight":
            self.change_x += 0.25
            if self.change_x >= 15:
                self.change_x = 15
            #if self.change_x >= 30:
            #    self.change_x = 30
            if self.change_y == 1:
                self.framepause += 1
                if self.framepause >= 2:
                    self.Direction = 1
                    self.frame+=1
                    if self.frame == 4:
                        self.frame = 0
                    self.framepause = 0
                self.image = pygame.image.load(os.path.join('images', PR[self.frame]+".gif")).convert()
            else:
                if self.frame == 4:
                    self.frame = 0
                if self.change_y <= 0:
                    self.image = pygame.image.load(os.path.join('images', PF[self.Direction]+".gif")).convert()
                elif self.change_y >= 2:
                    self.image = pygame.image.load(os.path.join('images', PF[self.Direction+2]+".gif")).convert()
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        #Moves specific blocks up on contact
        for block in self.level.platform_list:
            if midW in range(block.rect.left, block.rect.right):
                if block.type == "up" or "down":
                    if block.type == "up":
                        block.rect.y -= 0.01
                    if block.type == "down":
                        block.rect.y += 0.01
                if block.type == "left":
                    block.rect.x -= 0.01
                    self.rect.x -= 0.01
                if block.type == "right":
                    block.rect.x += 0.01
                    self.rect.x += 0.01
        #Use math to calculate which side we are on
        for block in self.level.platform_list:
            if self.rect.right >= block.rect.left and range(self.rect.top, self.rect.bottom) in range(block.rect.bottom, block.rect.top):
                self.rect.left = block.rect.right
                if jumps == 0:
                    self.rect.bottom = block.rect.bottom
            if self.rect.left <= block.rect.right and range(self.rect.top, self.rect.bottom) in range(block.rect.bottom, block.rect.top):
                self.rect.right = block.rect.left
                if jumps == 0:
                    self.rect.bottom = block.rect.bottom
        block_hit_list = pygame.sprite.spritecollide(self, self.level.imageplatform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                #block.rect.left-=5
                self.change_x = 0
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.change_x = 5
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                self.jumps = 0
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
 
            # Stop our vertical movement
            self.change_y = -50
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 1.1
        
        # See if we are on the ground.
        #if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
        #    self.change_y = 0
        #    self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        """ Called when user hits 'jump' button. """
        jumps = self.jumps
        if self.jumps != 2:
            
            platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            self.rect.y -= 10
        # If it is ok to jump, set our speed upwards and check if the player has jumped twice yet
            if self.jumps == 1:
                if len(platform_hit_list) > -20:
                    self.change_y = -20
                    self.jumps += 1
            if self.jumps == 0:
                if len(platform_hit_list) > -20:
                    self.change_y = -25
                    self.jumps += 1
                
            
            
    # Player-controlled movement:
    def go_left(self):
        self.state = "WLeft"
        """ Called when the user hits the left arrow. """
        
        if self.rect.x < -10:
            self.rect.x = -10
        self.Direction = 0
        
    def go_right(self):
        self.state = "WRight"
        """ Called when the user hits the right arrow. """
        
        
        self.Direction = 1
        
        
    def stop(self):
        self.state = "Idle"
        
        """ Called when the user lets off the keyboard. """
        
        self.change_x = 0

