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
PF = ["PFALL", "PFALR", "PFALL2", "PFALR2", "PFALL3", "PFALR3", "PFALL4", "PFALR4"]
PH = ["Head1"]

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
class Player(pygame.sprite.Sprite):
    
    """
    This class represents the bar at the bottom that the player controls.
    """
    # -- Methods
    def __init__(self):
        self.secondtimer = 0#Counts up to 60 and adds a second
        self.time = []#Stores every second of time for non player objects
        self.ptime = []#Player version of previous
        self.timeseconds = []#Has each frame of a second and gets appended to self.time before being cleared
        self.ptimeseconds = []#Player version of previous
        self.rewind = "OFF"
        self.rewframe = 0
        self.rewtime = 0
        self.rewseconds = 0
        self.bounces = 0
        self.framepause = 0
        self.state = "Idle"
        self.fails = 0
        self.Direction = 1
        self.message = ""
        """ Constructor function """
        self.jumps = 0
        # Call the parent's constructor
        super().__init__()
        self.stage = 0
        self.stageM = 1
        self.timer = 0
        self.totalseconds = 0
        self.image = pygame.image.load(os.path.join('images', "PIR.gif")).convert()
        self.frame = 0
        self.rect = self.image.get_rect()

        #Visual triggers
        self.down = 0
        self.up = 0
        self.pull = 0
        
        self.change_x = 0
        self.change_y = 0
        self.anim = 0.0
        self.falltime = 0
        #All of the solid objects are here
        self.level = None
        self.text = "OFF"
    def update(self):
        
        """ Move the player. """
        # Gravity
        self.secondtimer += 1
        self.calc_grav()
##        if self.rewind == "OFF":
##            for block in self.level.platform_list:
##                if self.secondtimer < 60:
##                    Info = [block.rect.x, block.rect.y, block.moves]
##                    self.timeseconds.append(Info)
##                    Info.clear()
##                if self.secondtimer >= 60:
##                    self.secondtimer = 0
##                    self.time.append(self.timeseconds)
##            if self.secondtimer < 60:
##                Info = [
##                        self.rect.x,   #0
##                        self.rect.y,   #1
##                        self.jumps,    #2
##                        self.bounces,  #3
##                        self.Direction,#4
##                        self.image,    #5
##                        self.state,    #6
##                        ]
##                self.ptimeseconds.append(Info)
##                Info.clear()
##                if self.secondtimer >= 60:
##                    self.secondtimer = 0
##                    self.ptime.append(self.ptimeseconds)
        if self.rect.y >=480:
            for block in self.level.platform_list:
                if block.rect.x <= self.rect.x:
                    self.rect.y=block.rect.y-200
                    self.rect.x=block.rect.x
##        if self.rewind == "ON" and self.rewseconds != len(self.ptime)-1:
##            Seconds = len(self.ptime)-1-self.rewseconds
##            Frame = len(self.ptime[Seconds])-1-self.rewframe
##            self.rect.x = self.ptime[Seconds][Frame][0]
##            if self.rewframe >= 60:
##                self.rewframe = 0
##                self.rewseconds += 1
##        
        pcH = [self.rect.top, self.rect.bottom]
        pcW = [self.rect.left, self.rect.right]
        midH = st.median(pcH)
        midW = st.median(pcW)
        pcH.clear()
        pcW.clear()
        #Movement states start here
        if self.state == "WLeft":
            self.change_x -= 0.25
            if self.change_x <= -15:
                self.change_x = -15
            if self.change_y == 1:
                self.framepause += 1
                if self.framepause >= 2:
                    self.Direction = 0
                    self.frame+=1
                    if self.frame >= 4:
                        self.frame = 0
                    self.framepause = 0
                self.image = pygame.image.load(os.path.join('images', PL[self.frame]+".gif")).convert()
            else:
                if self.frame == 4:
                    self.frame = 0
                if self.change_y <= 0:
                    self.image = pygame.image.load(os.path.join('images', PF[self.Direction]+".gif")).convert()
                if self.change_y >= 1 and self.change_y <= 10:
                    self.image = pygame.image.load(os.path.join('images', PF[self.Direction+4]+".gif")).convert()
                elif self.change_y >= 11:
                    self.image = pygame.image.load(os.path.join('images', PF[self.Direction+2]+".gif")).convert()
        
        if self.state == "Idle":
            if self.frame >= 4:
                self.frame = 0
            if self.change_y <= -1:
                self.image = pygame.image.load(os.path.join('images', PF[self.Direction]+".gif")).convert()
            if self.change_y >= 1 and self.change_y <= 5:
                self.image = pygame.image.load(os.path.join('images', PF[self.Direction+4]+".gif")).convert()
            if self.change_y >= 6 and self.change_y <= 11:
                self.image = pygame.image.load(os.path.join('images', PF[self.Direction+6]+".gif")).convert()
            elif self.change_y >= 11:
                self.image = pygame.image.load(os.path.join('images', PF[self.Direction+2]+".gif")).convert()
            if self.change_y == 1:
                self.image = pygame.image.load(os.path.join('images', PI[self.Direction]+".gif")).convert()
            
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
                if self.change_y >= 1 and self.change_y <= 10:
                    self.image = pygame.image.load(os.path.join('images', PF[self.Direction+4]+".gif")).convert()
                elif self.change_y >= 11:
                    self.image = pygame.image.load(os.path.join('images', PF[self.Direction+2]+".gif")).convert()

            #Movement states end here




                    
        # Move left/right
        self.rect.x += self.change_x
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        #Block type info
        for block in self.level.platform_list:
            if midW in range(block.rect.left, block.rect.right):
                if block.type == "down" and block.moves < 100:
                    if self.rect.bottom == block.rect.top and block.type == "down":
                        self.rect.y += 2
                    if block.rect.bottom <= self.rect.top:
                        block.rect.y-=2
                        block.moves-=1
                    block.rect.y += 2
                    block.moves += 1
                if block.type == "up" and block.moves < 100:
                    if self.rect.bottom == block.rect.top and block.type == "up":
                        self.rect.y -= 2
                    if self.rect.top <= block.rect.bottom and self.rect.top > block.rect.top:
                        self.rect.y += 2
                    block.rect.y -= 2
                    block.moves += 1
                if block.type == "bouncy" and self.rect.bottom == block.rect.top:
                    self.rect.y -= 10
                    self.jumps = 1
                    self.bounces += 1
                    if self.bounces == 10:
                        self.bounces -= 1
                    self.change_y -= 5*self.bounces
                
                if block.type != "bouncy" and self.rect.bottom == block.rect.top:
                    self.bounces = 0
            if block.type.startswith("pull"):
                direct = block.type[4:]
                if self.rect.x in range(block.rect.left, block.rect.right):
                    if direct == "up":
                        if self.rect.y > block.rect.y:
                            self.change_y=-10
                            self.pull = 1
                    if direct == "down":
                        if self.rect.y < block.rect.y:
                            self.change_y=10
                            self.pull = 1
                
                if self.rect.y in range(block.rect.top, block.rect.bottom):
                    if direct == "left":
                        self.change_x=-10
                        self.pull = 1
                    if direct == "right":
                        self.change_x=10
                        self.pull = 1
                elif self.rect not in block.rect:
                    self.pull = 0
                    
            if block.type.startswith("mess"):
                if midW in range(block.rect.left, block.rect.right):
                    self.message = block.message
            #Move blocks back to their original positions when the player is away.
            if midW not in range(block.rect.left, block.rect.right):
                if block.type == "down" and block.moves > 0:
                    block.rect.y -= 2
                    block.moves -= 1
                if block.type == "up" and block.moves > 0:
                    block.rect.y += 2
                    block.moves -= 1
        playersize = self.rect.bottom-self.rect.top
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        
        #Use math to calculate which side we are on and stop the player from wall clipping
        for block in block_hit_list:
            self.colliding = False
            MIDPOINT_X = [block.rect.left, midW, block.rect.right]
            MIDPOINT_Y = [block.rect.top, self.rect.bottom, block.rect.bottom]
            CENTERPOINT_X = st.median(MIDPOINT_X)
            CENTERPOINT_Y = st.median(MIDPOINT_Y)
            blockSides = [block.rect.left, block.rect.right]
            blockSides2 = [block.rect.top, block.rect.bottom]
            Side = min(blockSides, key=lambda x:abs(x-CENTERPOINT_X))
            Height = min(blockSides2, key=lambda x:abs(x-CENTERPOINT_Y))
            
            

            if Side == block.rect.left:
                self.rect.right = block.rect.left
            if Side == block.rect.right:
                self.rect.left = block.rect.right
            if Side != block.rect.left and Side != block.rect.right:
                self.colliding = False
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        floor = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in floor:
            
            MIDPOINT_X = [block.rect.left, midW, block.rect.right]
            MIDPOINT_Y = [block.rect.top, self.rect.bottom, block.rect.bottom]
            CENTERPOINT_X = st.median(MIDPOINT_X)
            CENTERPOINT_Y = st.median(MIDPOINT_Y)
            blockSides = [block.rect.left, block.rect.right]
            blockSides2 = [block.rect.top, block.rect.bottom]
            Side = min(blockSides, key=lambda x:abs(x-CENTERPOINT_X))
            Height = min(blockSides2, key=lambda x:abs(x-CENTERPOINT_Y))
            
            # Reset our position based on the top/bottom of the object.
            if Height == block.rect.top and self.change_y > 0:
                self.rect.bottom = block.rect.top
                self.jumps = 0
                
            if Height == block.rect.bottom and self.change_y <= 0 and self.rect.top <= block.rect.bottom:
                self.rect.top = block.rect.bottom
                
            if block.type == "pullup":
                self.rect.bottom = block.rect.top
            # Stop our vertical movement
            self.change_y = 0
        
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 1.1
 
    def jump(self):
        """ Called when user hits 'jump' button. """
        jumps = self.jumps
        self.last_x = self.rect.x
        self.last_y = self.rect.y
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        
        
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
        for block in platform_hit_list:
            if self.rect.top <= block.rect.bottom and block.rect.top < self.rect.top:
                self.change_y *= -1
                self.jumps = 0
            
    # Player-controlled movement:
    def go_left(self):
        self.state = "WLeft"
        """ Called when the user hits the left arrow. """
        
        #if self.rect.x < -10:
        #    self.rect.x = -10
        self.Direction = 0
        
    def go_right(self):
        self.state = "WRight"
        """ Called when the user hits the right arrow. """
        
        
        self.Direction = 1
        
        
    def stop(self):
        self.state = "Idle"
        
        """ Called when the user lets off the keyboard. """
        
        self.change_x = 0

