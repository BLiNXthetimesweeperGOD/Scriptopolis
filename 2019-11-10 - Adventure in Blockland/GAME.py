import random
import pygame
import os
Music = ["RT1.ogg", "RT2.ogg", "RT3.ogg", "RT4.ogg", "RT5.ogg"]
SoundFX = ["B_Dead", "B_Die", "B_EdgeStand", "B_GEEEEEE", "B_HeeYaBash", "B_Highfall", "B_IceSlip", "B_Laugh", "B_Mew", "B_NotHappyOooh", "B_OOOH", "B_SecretMedal", "B_Shoot", "B_StageClear", "B_Wah", "B_Woah", "B_Yes", "B_Unused1", "B_Unknown"]
print("Welcome!\nThis game is still very early in development, so bugs are everywhere.")
# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# Screen dimensions
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
 
 
from PlayerCharacter import Player
from Crnblb import Chronoblob
from PlatformOBJ import Platform
from FastOBJ import Fast

from LVLDAT import Level
from LVLDAT import Level_01
from LVLDAT import Level_02

def main():
    """ Main Program """
    pygame.init()
    
    
    

    
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)  
    pygame.display.set_caption("Blinx's adventure in blockland")
    cblob = Chronoblob()
    # Create the player
    player = Player()
    player1 = Player()
    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                    
                if event.key == pygame.K_RIGHT:
                    rightnoise = pygame.mixer.Sound(os.path.join("sounds", '%s.ogg' % (random.choice(SoundFX))))
                    rightnoise.play()
                    player.go_right()
                    cblob.go_left()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_SPACE:
                    player.moonjump()
                if event.key == pygame.K_DOWN:
                    currently_playing_song = pygame.mixer.music.load(os.path.join("music", random.choice(Music)))
                    pygame.mixer.music.play()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                text = font.render("This is Blinx's Adventure in Blockland.", True, WHITE)
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
        #If the player gets near the top of the screen, shift the world up (+y)
        if player.rect.top <= 50:
            diff = 50 - player.rect.top
            player.rect.top = 50
            current_level.height_world(diff)
        #If the player gets near the bottom of the screen, shift the world up (+y)
        if player.rect.bottom >= 500:
            diff = player.rect.bottom - 500
            player.rect.bottom = 500
            current_level.height_world(-diff)
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)
 
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            player1.rect.x = 150
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
                player1.level = current_level 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()
print("Thank you for playing Blinx's adventure in blockland!")
