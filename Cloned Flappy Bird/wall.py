import pygame 

class Wall(pygame.sprite.Sprite):
    def __init__(self, inverted, height, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        image = pygame.image.load('./image/pipe2.png').convert_alpha()
        self.image = pygame.transform.scale(image,(75, height)) #(width,height) of the wall
        self.rect = self.image.get_rect()
        self.inverted = inverted
        self.pass_bird = False
        if inverted: #inverted == True mean wall is on top
            self.image = pygame.transform.flip(self.image, False, True) #flip the wall in y-axis if there is an image
            self.rect.topleft = (SCREEN_WIDTH, 0)
        else: #otherwise ,wall is in bottom
            self.rect.topleft = (SCREEN_WIDTH, SCREEN_HEIGHT - height)

    def update(self):
        self.rect.x -= 5 #Move left
        if self.rect.right < 0:
            self.kill() #remove the object from all sprite group