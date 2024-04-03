import pygame
from imageSprite import ImageSprite

class Player(ImageSprite):
    def __init__(self,x,y,image,speed,screen,dx=0,dy=0):
        super().__init__(x,y,image)
        self.image = image
        self.__speed = speed
        self.screen = screen #tuple
        self.dx = dx
        self.dy = dy
        self.flap_strength = 5
        self.gravity = 0.3
        self.jump_pressed = False
        self.__start = False

    def speed(self):
        return self.__speed

    @property
    def start(self):
        return self.__start
    @start.setter
    def start(self, value):
        self.__start = value


    def update(self,elapsedTime):
        if self.start:
            if not self.jump_pressed:
                self.dy += self.gravity
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and not self.jump_pressed:
                self.dy = -self.flap_strength
                self.jump_pressed = True
            elif not keys[pygame.K_SPACE]:
                self.jump_pressed = False

            self._y += self.dy
            self._x += self.dx
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.start = True
