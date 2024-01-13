import sys
import random
import time
import pygame 
from pygame.locals import *
from bird import Bird
from wall import Wall

def run():
    #Initial setting
    pygame.display.set_caption("Flappy Bird by Sunny")

    #Setting - Game Constant
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 500
    GRAVITY = 0.25 #Simulate the gravity 
    JUMP_VELOCITY = -8 #Change the bird's velocity to simluate a jump by the bird
    JUMP_KEY = pygame.K_SPACE
    BIRD2_POSITION = -1000
    SCORE_TEXT_COLOR = (92, 50, 168)
    GAMEOVER_TEXT_COLOR = (51, 51, 51)

    #Setting - Game Environment
    FPS = pygame.time.Clock()
    score = 0

    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    bird = Bird(SCREEN_HEIGHT)
    bird2 = Bird(BIRD2_POSITION) #bird2 is for transformation of 'bird' from "top to bottom" or "bottom to top"

    WALL_GENERATION = pygame.USEREVENT + 0
    pygame.time.set_timer(WALL_GENERATION, 1500)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(bird, bird2)
    walls = pygame.sprite.Group()
    top_walls = pygame.sprite.Group() # Create for sound effect score_increment_sound

        #Font
    score_currentValue_font = pygame.font.SysFont('impact', 20)

        #Image
    bg_image = pygame.image.load('./image/bg_image2.jpg')
    bg_image1 = pygame.transform.scale(bg_image, (bg_image.get_width(), SCREEN_HEIGHT)) #let image fit the height of the screen
    bg_image_rect1 = bg_image1.get_rect()
    bg_image_rect1.topleft = (0, 0)
    bg_image2 = pygame.transform.scale(bg_image, (bg_image.get_width(), SCREEN_HEIGHT)) #let image fit the height of the screen
    bg_image_rect2 = bg_image2.get_rect()
    bg_image_rect2.topleft = (bg_image_rect1.right, 0)

        #Sound/Music
    pygame.mixer.music.load('./music/bg_music.wav') #load background music
    pygame.mixer.music.play(-1) #play background music indefinitely 
    pygame.mixer.music.set_volume(0.3) #set volume of the background music
    jump_sound = pygame.mixer.Sound('./sound/jump_sound.flac')
    game_over_sound = pygame.mixer.Sound('./sound/game_over_sound.wav')
    score_increment_sound = pygame.mixer.Sound('./sound/score_increment_sound.wav')

    #Main program 

    running = True
    while running:

        #Handle event
        for event in pygame.event.get():
            if event.type == QUIT: #EXIT APP
                for sprite in all_sprites.sprites():
                    sprite.kill()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == JUMP_KEY: #JUMP EVENT
                jump_sound.play()
                bird.vertical_velocity = JUMP_VELOCITY
                if not bird2.outside:
                    bird2.vertical_velocity = JUMP_VELOCITY
            if event.type == WALL_GENERATION: #GENERATE WALLS
                height_between_walls = random.randint(120, 200) #size of the hole between top and bottom walls
                wall_height = random.randint(0, SCREEN_HEIGHT - height_between_walls) #for determine height of two walls in below
                wall_bottom = Wall(False, wall_height, SCREEN_WIDTH, SCREEN_HEIGHT)
                wall_top = Wall(True, SCREEN_HEIGHT - (wall_height + height_between_walls), SCREEN_WIDTH, SCREEN_HEIGHT)
                all_sprites.add(wall_bottom, wall_top)
                walls.add(wall_bottom, wall_top)
                top_walls.add(wall_top)
        
        #GAME END if bird collide with a wall
        for sprite in walls.sprites():
            collision_with_bird = pygame.sprite.collide_mask(bird, sprite)
            collision_with_bird2 = pygame.sprite.collide_mask(bird2, sprite)
            if collision_with_bird or collision_with_bird2:
                running = False

        #Increase score if the bird passes between two walls
        for sprite in top_walls.sprites():
            if not sprite.pass_bird and (sprite.rect.centerx < bird.rect.centerx or sprite.rect.centerx < bird2.rect.centerx):
                score_increment_sound.play()
                sprite.pass_bird = True
                score += 1

        bird.vertical_velocity += GRAVITY #velocity changes due to gravity
        bird.rect.y += bird.vertical_velocity #bird fell down due to gravity 
        if not bird2.outside:
            bird2.vertical_velocity += GRAVITY
            bird2.rect.y += bird2.vertical_velocity


        #Make sure to have fluent transformation of the bird from "top to bottom" or "bottom to top" of the screen using bird2
        if bird.rect.top < 0: #Go top
            bird2.rect.top = bird.rect.top + SCREEN_HEIGHT
            bird2.vertical_velocity = bird.vertical_velocity
            bird2.outside = False
            if bird.rect.bottom < 0 or bird.rect.top >= 0:
                bird.rect.bottom = SCREEN_HEIGHT
                bird2.rect.top = int(BIRD2_POSITION / 2)
                bird2.outside = True
        if bird.rect.bottom > SCREEN_HEIGHT: # Go bottom
            bird2.rect.bottom = bird.rect.bottom - SCREEN_HEIGHT
            bird2.vertical_velocity = bird.vertical_velocity
            bird2.outside = False
            if bird.rect.top >= SCREEN_HEIGHT or bird.rect.bottom < SCREEN_HEIGHT:
                bird.rect.top = 0
                bird2.rect.top = int(BIRD2_POSITION / 2)
                bird2.outside = True

        #Update display 
        walls.update() #update all walls which are existing  

        #Make sure to remove the previous position of the bird
        #At the same time, we have dynamic background image 
        bg_image_rect1.x -= 1
        bg_image_rect2.x -= 1
        if bg_image_rect1.x == -1 * bg_image1.get_width():
            bg_image_rect1.x = bg_image_rect2.right #set image1 adjacent to the left side of image2
        if bg_image_rect2.x == -1 * bg_image2.get_width():
            bg_image_rect2.x = bg_image_rect1.right #set image2 adjacent to the left side of image1

        DISPLAYSURF.blit(bg_image1, bg_image_rect1)
        DISPLAYSURF.blit(bg_image2, bg_image_rect2)

        bird.draw(DISPLAYSURF) #draw/relocate position of the bird
        bird2.draw(DISPLAYSURF) #draw/relocate position of the bird2
        walls.draw(DISPLAYSURF) #draw/relocate position of wall(s)

        #Update Score
        DISPLAYSURF.blit(score_currentValue_font.render(f'{score}', True, (SCORE_TEXT_COLOR)), (SCREEN_WIDTH // 2,20))

        pygame.display.update() #update display

        FPS.tick(60) #make sure the game is 60 frames

    pygame.mixer.music.pause() 
    game_over_sound.play()
    
    for sprite in all_sprites.sprites():
        sprite.kill()

    return (2, score) #go to game over page

    
