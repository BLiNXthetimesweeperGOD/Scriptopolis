import random
import pygame
import os
import statistics as st
Music = ["loop0", "loop1", "loop2", "Testmap"]

# Global constants
level_count = 3
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
from LVLDAT import Level_03
from LVLDAT import Level_04


def main():
    """ Main Program """
    pygame.init()
    font = pygame.font.SysFont("arial", 15)
    
    

    
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    
    
    pygame.display.set_caption("Scriptopolis Game")
 
    # Create the player
    player = Player()
    # Create all the levels
    level_list = []
    level_list.append(Level_04(player))
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    level_list.append(Level_03(player))
    current_level_no = 0
    current_level = level_list[current_level_no]
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    
    Dialog = [        
                    "Welcome to Scriptopolis, nameless hero!...",
                    "I brought you here, as you are this world's last hope!",
                    "I know you don't want to help, but... well...",
                    """It appears that reality isn't working as it should.
I don't know what else I can do...
My boss and all of his friends stopped responding.
The only way for you to get out of here is to help me
get them to respond again and fix reality.
I'm sorry!""",
                    """If you do help, power will be restored to the
machine I used to bring you here.
It, along with the rest of scriptopolis ran out of power when
I teleported you.""",
                    "How am I still talking?",
                    "I came from your universe. That machine was made by me.",
                    "",
                    "",
                    "",
                    "",
                    ""]
    playrect = 0
    playrect2 = 0
    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
    drawgmovertxt = False
    # Loop until the user clicks the close button.
    done = False
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    for block in player.level.platform_list:
        if block.type == "spawn":
            blocksides = [block.rect.left, block.rect.right]
            startpos = st.median(blocksides)
            player.rect.bottom = block.rect.top
            player.rect.x = startpos
    pygame.mixer_music.load("music\\%s.wav" % (Music[current_level_no]))
    pygame.mixer_music.play(loops=0, start=0.0, fade_ms=1999)
    size = []
    # -------- Main Program Loop -----------
    while not done:
        #Player inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == 32:
                    player.text = "ON"
##                if event.key == 32:
##                    player.rewind = "ON"
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
            if event.type == pygame.KEYUP:
                #if event.key == 32:
                #    player.text = "OFF"
                if event.key == 32:
                    player.rewind = "OFF"
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                    
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
        if pygame.mixer_music.get_pos() == -1:
            pygame.mixer_music.fadeout(3000)
            pygame.mixer_music.load("music\\%s.wav" % (Music[current_level_no]))
            pygame.mixer_music.play(loops=0, start=0.0, fade_ms=0)
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
        MOVE = font.render("Move to the right, please!", 2, (250,0,0))
        if player.text == "ON":
            #All of the debug text rendered during the game
            PMES = font.render("%s" % (player.message), 1, (100,255,0))
            JUMP = font.render("JUMPS   %d" % (player.jumps), 1, (100,255,0))
            DIRT = font.render("FACING  %d" % (player.Direction), 1, (100,100,255))
            Xspd = font.render("X SPEED %d" % (player.change_x), 1, (255,255,255))
            Yspd = font.render("Y SPEED %d" % (player.change_y), 1, (100,255,0))
            LEVL = font.render("STAGE   %d" % (current_level_no), 1, (0 ,255,100))

        
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit and current_level_no != level_count:
            player.rect.x = 120
            pygame.mixer_music.fadeout(300)
            print(current_level_no)
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
        POSX = font.render("POS_X %d" % (current_position), 1, (255,255,100))
        POSY = font.render("POS_Y %d" % (current_height), 1, (255,255,100))
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        draws = 0
        draws = player.rect.top
        if player.bounces != 0:
            
            for A in range(100):
                draws+=1
                if random.randint(0, 2) == 2:
                    for i in range(player.rect.left, player.rect.right):
                        A = screen.get_at((i, draws))
                        A[0] = random.randint(1, 100)
                        A[1] = random.randint(1, 200)
                        A[3] = random.randint(1, 255)
                        #print(A)
                    
                        if A[0] != 0 and A[1] != 0 and A[2] != 0 and random.randint(0, 1) == 1:
                            screen.set_at((i-int(player.change_x), int(draws+player.change_y/3*-1)), A)#random.randint(-25, 0)), A)
                            screen.set_at((i-int(player.change_x/1.5), int(draws+player.change_y/2*-1)), A)#random.randint(-25, 0)), A)
                            screen.set_at((i-int(player.change_x/2), int(draws+player.change_y/1*-1)), A)#random.randint(-25, 0)), A)
                            screen.set_at((i-int(player.change_x*1.5), int(draws+player.change_y*-2)), A)#random.randint(-25, 0)), A)
                            screen.set_at((i-int(player.change_x/1.5), int(draws+player.change_y/2*-1)), A)#random.randint(-25, 0)), A)
                            screen.set_at((i-int(player.change_x/2), int(draws+player.change_y/1*-1)), A)#random.randint(-25, 0)), A)
        if player.pull != 0:
            
            for A in range(100):
                draws+=1
                if random.randint(0, 2) == 2:
                    for i in range(player.rect.left, player.rect.right):
                        A = screen.get_at((i, draws))
                        A[0] = 255
                        A[1] = 255
                        A[3] = 255
                        #print(A)
                    
                        if A[0] != 0 and A[1] != 0 and A[2] != 0 and random.randint(0, 1) == 1:
                            screen.set_at((i-int(player.change_x*-1), int(draws+player.change_y/3*-1)), A)#random.randint(-25, 0)), A)
                            screen.set_at((i-int(player.change_x/1.5*-1), int(draws+player.change_y/2*-1)), A)#random.randint(-25, 0)), A)
                            screen.set_at((i-int(player.change_x/2*-1), int(draws+player.change_y/1*-1)), A)#random.randint(-25, 0)), A)
                            screen.set_at((i-int(-player.change_x*1.5), int(draws+player.change_y*-2)), A)#random.randint(-25, 0)), A)
                            screen.set_at((i-int(-player.change_x/1.5), int(draws+player.change_y/2*-1)), A)#random.randint(-25, 0)), A)
                            screen.set_at((i-int(-player.change_x/2), int(draws+player.change_y/1*-1)), A)#random.randint(-25, 0)), A)
        if player.change_y >= 100:
            player.timer+=1
        if player.timer >= 30:
            # Teleport the player to the spawn block so they don't fall forever
            for block in player.level.platform_list:
                if block.type == "spawn":
                    player.change_x = 0
                    player.change_y = 0
                    player.rect.x = block.rect.x
                    player.rect.bottom = block.rect.top
                    player.timer = 0
                    player.fails = 0
                if player.timer > 30:
                    player.fails = 1

            
        # Limit to 60 frames per second
        clock.tick(60)
        #screen.blit(seconds, (100, 100))
        #player.timer+=1
        #timedata = [player.rect.x, player.rect.y]
        #if player.timer == 60:
        #    player.time.append(timedata)
        if player.text == "ON":
            screen.blit(PMES, (100, 50))
##            screen.blit(LEVL, (100, 50))
##            screen.blit(JUMP, (100, 75))
##            screen.blit(DIRT, (100, 100))
##            screen.blit(Xspd, (100, 125))
##            screen.blit(Yspd, (100, 150))
##            screen.blit(POSX, (100, 175))
##            screen.blit(POSY, (100, 200))
        #    player.timer = 0
        #    player.totalseconds += 1
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()

