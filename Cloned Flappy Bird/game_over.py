import pygame 
import sys
import pygame_gui

def game_over(score, highest_score):

    pygame.display.set_caption("Flappy Bird by Sunny - Game Over")

    #Constant
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 500
    BUTTON_WIDTH = 110
    BUTTON_HEIGHT = 50

    RUN_BUTTON_POSITION_X = SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2
    RUN_BUTTON_POSITION_Y = SCREEN_HEIGHT / 5 * 2.5
    EXIT_BUTTON_POSITION_X = SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2
    EXIT_BUTTON_POSITION_Y = SCREEN_HEIGHT / 5 * 3.3
    MENU_BUTTON_POSITION_X = SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2
    MENU_BUTTON_POSITION_Y = SCREEN_HEIGHT / 5 * 4.1
    GAMEOVER_POSITION_X = SCREEN_WIDTH / 2 
    GAMEOVER_POSITION_Y = SCREEN_HEIGHT / 5 * 1.3
    SCORE_TEXT_POSITION_X = SCREEN_WIDTH / 2 
    SCORE_TEXT_POSITION_Y = SCREEN_HEIGHT / 5 * 2.2
    HIGH_SCORE_TEXT_POSITION_X = SCREEN_WIDTH / 2 
    HIGH_SCORE_TEXT_POSITION_Y = SCREEN_HEIGHT / 5 * 1.8

    TRY_AGAIN_TEXT = 'TRY AGAIN'
    APP_EXIT_TEXT = 'EXIT'
    TO_MENU_TEXT = 'GO TO MENU'

    GAMEOVER_COLOR = (166, 0, 255)
    TEXT_COLOR = (5, 248, 252)

    #Background 
    bg_image = pygame.image.load('./image/bg_image2.jpg')
    bg_image1 = pygame.transform.scale(bg_image, (bg_image.get_width(), SCREEN_HEIGHT)) #let image fit the height of the screen
    bg_image_rect1 = bg_image1.get_rect()
    bg_image_rect1.topleft = (0, 0)

    #Text
    highest_score_font = pygame.font.SysFont('impact', 20)
    highest_score_font = highest_score_font.render(f'Highest score: {highest_score}', True, TEXT_COLOR)
    highest_score_font_rect = highest_score_font.get_rect()
    highest_score_font_rect.center = (HIGH_SCORE_TEXT_POSITION_X, HIGH_SCORE_TEXT_POSITION_Y)

    score_font = pygame.font.SysFont('impact', 20)
    score_font = score_font.render(f'Your score in this round: {score}', True, TEXT_COLOR)
    score_font_rect = score_font.get_rect()
    score_font_rect.center = (SCORE_TEXT_POSITION_X, SCORE_TEXT_POSITION_Y)

    title = pygame.font.SysFont('Verdana', 60)
    title = title.render("GAME OVER!", True, GAMEOVER_COLOR)
    title_rect = title.get_rect()
    title_rect.center = (GAMEOVER_POSITION_X, GAMEOVER_POSITION_Y)

    #Initial setting
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), 'theme.json')
    run_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((RUN_BUTTON_POSITION_X, RUN_BUTTON_POSITION_Y), (BUTTON_WIDTH, BUTTON_HEIGHT)), text=TRY_AGAIN_TEXT, manager=manager)
    exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((EXIT_BUTTON_POSITION_X, EXIT_BUTTON_POSITION_Y), (BUTTON_WIDTH, BUTTON_HEIGHT)), text=APP_EXIT_TEXT, manager=manager)
    menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((MENU_BUTTON_POSITION_X, MENU_BUTTON_POSITION_Y), (BUTTON_WIDTH, BUTTON_HEIGHT)), text=TO_MENU_TEXT, manager=manager)

    FPS = pygame.time.Clock()

    running = True

    while running:
        time_delta = FPS.tick(60)/1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == run_button: #play again
                    return 1
                elif event.ui_element == exit_button: #exit the app
                    return -1
                elif event.ui_element == menu_button: #go to menu
                    return 0
                    
            manager.process_events(event)

        manager.update(time_delta)

        DISPLAYSURF.blit(bg_image1, bg_image_rect1)
        DISPLAYSURF.blit(title, title_rect)
        DISPLAYSURF.blit(highest_score_font, highest_score_font_rect)
        DISPLAYSURF.blit(score_font, score_font_rect)
        manager.draw_ui(DISPLAYSURF)
        pygame.display.update() #update display
