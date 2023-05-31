import random
import pygame
import os
Music = ["RT1.ogg", "RT2.ogg", "RT3.ogg", "RT4.ogg", "RT5.ogg"]
SoundFX = ["B_Dead", "B_Die", "B_EdgeStand", "B_GEEEEEE", "B_HeeYaBash", "B_Highfall", "B_IceSlip", "B_Laugh", "B_Mew", "B_NotHappyOooh", "B_OOOH", "B_SecretMedal", "B_Shoot", "B_StageClear", "B_Wah", "B_Woah", "B_Yes", "B_Unused1", "B_Unknown"]

# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 600
 
 
from PlayerCharacter import Player

from PlatformOBJ import Platform

from LVLDAT import Level
from LVLDAT import Level_01
from LVLDAT import Level_02
from LVLDAT import GMOVER
#from LVLDAT import Level_03
#from LVLDAT import Level_04

def main():
    """ Main Program """
    pygame.init()
    font = pygame.font.SysFont("arial", 15)
    
    

    
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    
    
    pygame.display.set_caption("Blinx's adventure in blockland")
 
    # Create the player
    player = Player()
    # Create all the levels
    level_list = []
    level_list.append(Level_01(player)) 
    level_list.append(Level_02(player))
    level_list.append(GMOVER(player))
    
    #level_list.append(Level_03(player))
    #level_list.append(Level_04(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    deathmessage = ["It looks like you fell down a bit too far...",
                    "I guess your training with Jimmy wasn't enough...",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    ""]
    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
    drawgmovertxt = False
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                    #leftnoise = pygame.mixer.Sound(os.path.join("sounds", '%s.ogg' % (random.choice(SoundFX))))
                    #leftnoise.play()
                if event.key == pygame.K_RIGHT:
                    #rightnoise = pygame.mixer.Sound(os.path.join("sounds", '%s.ogg' % (random.choice(SoundFX))))
                    #rightnoise.play()
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                #if event.key == pygame.K_DOWN:
                    #currently_playing_song = pygame.mixer.music.load(os.path.join("music", random.choice(Music)))
                    #pygame.mixer.music.play()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
 
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world_x(-diff)
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world_x(diff)

        # If the player gets near the top of the screen, shift the world down (-y)
        if player.rect.top <= 20:
            diff = player.rect.top - 20
            player.rect.top = 20
            current_level.shift_world_y(-diff)
 
        # If the player gets near the bottom of the screen, shift the world up (+y)
        if player.rect.bottom >= 400:
            diff = 400 - player.rect.bottom
            player.rect.bottom = 400
            current_level.shift_world_y(diff)
        timesv = font.render("saving time...", 1, (255,255,0))
        
        gotxt = font.render("""%s""" % (deathmessage[player.totalseconds]), 1, (player.fade2,player.fade3,player.fade))
        seconds = font.render(str(player.totalseconds), 1, (255,255,0))
        Xspd = font.render("X %d" % (player.change_x), 1, (255,255,0))
        Yspd = font.render("Y %d" % (player.change_y), 1, (100,255,0))
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
        current_height = player.rect.y + current_level.world_height
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
        screen.blit(seconds, (100, 100))
        player.timer+=1
        timedata = [player.rect.x, player.rect.y]
        if player.timer == 60:
            player.time.append(timedata)
            #screen.blit(timesv, (100, 150))
            player.timer = 0
            player.totalseconds += 1
        if player.change_y > 100:
            player.jumps = 0
            player.totalseconds = 0
            player.timer = 0
            player.time.clear()
            current_level = GMOVER(player)
            drawgmovertxt = True
            player.died = True
            player.rect.x = 120
            player.rect.y = 120
            
            active_sprite_list.draw(screen)
            current_level_no == 2
            current_level = level_list[current_level_no]
            player.level = current_level
            current_level.update()
            current_level.draw(screen)
        if drawgmovertxt == True:
            screen.blit(gotxt, (320, 150))
            
            if player.fade > 0:
                player.fade-=1
            if player.fade < 100:
                if player.fade3 > 4:
                    player.fade3-=2
            if player.fade3 <= 10:
                if player.fade2 > 100:
                    player.fade2 -= 3
            for block in player.level.imageplatform_list:
                player.rect.bottom = block.rect.top
            for i in range(2500):
                A = screen.get_at((random.randint(1, 600), random.randint(1, 480)))
                screen.set_at((random.randint(1, 600), random.randint(1, 480)), A)
            #if player.rect.y >= 100:
                #player.rect.y = 900
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()
print("Thank you for playing Blinx's adventure in blockland!")
