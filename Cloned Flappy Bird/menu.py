import pygame 
import sys
import pygame_gui

def menu():
    pygame.display.set_caption("Flappy Bird by Sunny - Menu")

    #Constant
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 500
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 50
    RUN_BUTTON_POSITION_X = SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2
    RUN_BUTTON_POSITION_Y = SCREEN_HEIGHT / 5 * 3
    EXIT_BUTTON_POSITION_X = SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2
    EXIT_BUTTON_POSITION_Y = SCREEN_HEIGHT / 5 * 4
    TITLE_POSITION_X = SCREEN_WIDTH / 2 
    TITLE_POSITION_Y = SCREEN_HEIGHT / 5 * 1.3
    GAME_START_TEXT = 'PLAY'
    APP_EXIT_TEXT = 'EXIT'
    TITLE_COLOR = (166, 0, 255)

    #Background 
    bg_image = pygame.image.load('./image/bg_image2.jpg')
    bg_image1 = pygame.transform.scale(bg_image, (bg_image.get_width(), SCREEN_HEIGHT)) #let image fit the height of the screen
    bg_image_rect1 = bg_image1.get_rect()
    bg_image_rect1.topleft = (0, 0)

    #Text
    title = pygame.font.SysFont('Verdana', 60)
    title = title.render("Flappy Bird", True, TITLE_COLOR)
    title_rect = title.get_rect()
    title_rect.center = (TITLE_POSITION_X, TITLE_POSITION_Y)

    #Inital setting
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), 'theme.json')
    run_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((RUN_BUTTON_POSITION_X, RUN_BUTTON_POSITION_Y), (BUTTON_WIDTH, BUTTON_HEIGHT)), text=GAME_START_TEXT, manager=manager)
    exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((EXIT_BUTTON_POSITION_X, EXIT_BUTTON_POSITION_Y), (BUTTON_WIDTH, BUTTON_HEIGHT)), text=APP_EXIT_TEXT, manager=manager)

    FPS = pygame.time.Clock()

    running = True

    while running:
        time_delta = FPS.tick(60)/1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == run_button: #play the game
                    return 1
                elif event.ui_element == exit_button: #leave the app
                    return -1

            manager.process_events(event)

        manager.update(time_delta)

        DISPLAYSURF.blit(bg_image1, bg_image_rect1)
        DISPLAYSURF.blit(title, title_rect)
        manager.draw_ui(DISPLAYSURF)
        pygame.display.update() #update display

    pygame.quit()
    sys.exit()