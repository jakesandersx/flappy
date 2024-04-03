from abc import ABC, abstractmethod,abstractproperty
import pygame


class Sprite(ABC):
    def __init__(self,x,y,width,height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._rect = pygame.Rect(x,y,width,height)

    @abstractproperty
    def x(self):
        pass
    @abstractproperty
    def y(self):
        pass
    @abstractproperty
    def rect(self):
        pass

    @abstractmethod
    def draw(self,screen):
        pass