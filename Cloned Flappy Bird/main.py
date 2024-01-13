import pygame
import sys
from menu import menu
from run import run
from game_over import game_over

pygame.init()

mode = 0
score = 0
highest_score = 0

#mode = 0 is menu page
#mode = 1 is running the game
#mode = 2 is the game over page
#mode = -1 is exiting the game
while mode != -1:
    if mode == 0:
        mode = menu()
    elif mode == 1:
        mode, score = run()
        if highest_score < score:
            highest_score = score
    elif mode == 2:
        mode = game_over(score, highest_score)

pygame.quit()
sys.exit()