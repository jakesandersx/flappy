from sprite import Sprite
import pygame
import random

class Pipe(Sprite):
    def __init__(self, x, y, width, height, color, speed):
        super().__init__(x, y, width, height)
        self._speed = speed
        self._color = color
        self._gap = random.randint(150, 450)
        self.__start = False

    def draw(self, screen):
        topPipe = pygame.Rect(self._x, 0, self._width, (self.gap - 100))
        bottomPipe = pygame.Rect(self._x, (self.gap + 100), self._width, 800)

        pygame.draw.rect(screen, self._color, topPipe)
        pygame.draw.rect(screen, self._color, bottomPipe)

    @property
    def rect(self):
        topPipe = pygame.Rect(self._x, 600 - (self.gap + 25), self._width, self._height)
        bottomPipe = pygame.Rect(self._x, 0 + (self.gap - 25), self._width, self._height)
        return topPipe, bottomPipe

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def gap(self):
        return self._gap

    def speed(self):
        return self._speed

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, value):
        self.__start = value

    def intersect(self, box):
        gap = self.gap
        topPipeLimit = gap - 100
        bottomPipeLimit = gap + 100
        x = self._x

        for i in range(box.x, box.x + 61):
            if (box.y <= topPipeLimit or box.y >= bottomPipeLimit) and i == x:
                return True
        return False

    def update(self, elapsedTime):
        self._x += self._speed
