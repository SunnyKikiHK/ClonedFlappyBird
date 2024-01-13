import pygame 

class Bird(pygame.sprite.Sprite):
    def __init__(self, HEIGHT) :
        super().__init__()
        image = pygame.image.load('./image/bird.png').convert_alpha()
        self.image = pygame.transform.scale(image,(50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (50, int(HEIGHT / 2))
        self.vertical_velocity = 0
        self.outside = True # it is used for bird2, which see whether the game is using bird2 or not

    #Change the vertical velocity of the bird
    def change_velocity(self, value):
        self.vertical_velocity += value

    #relocate position of the bird
    def draw(self, screen):
        screen.blit(self.image, self.rect)
