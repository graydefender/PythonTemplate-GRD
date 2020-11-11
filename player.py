import pygame
from pygame.locals import *
from settings import *

#** 
# Player Control and movement through keyboard
#**
class Player(pygame.sprite.Sprite):

    def __init__(self):

  
        super().__init__()
  

        self.width = 15
        self.height =15

        # Make our top-left corner the passed-in location.
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill((YELLOW))

        self.rect = self.image.get_rect()

        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2

    def update(self):
        keys=pygame.key.get_pressed()
        if keys[K_LEFT]:            
            self.rect.x -= 10
        elif keys[K_RIGHT]:
            self.rect.x += 10
        if keys[K_UP]:            
            self.rect.y -= 10
        elif keys[K_DOWN]:
            self.rect.y += 10
 

      