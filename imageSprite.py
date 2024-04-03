from sprite import Sprite

class ImageSprite(Sprite):
    def __init__(self,x,y,image,isVisible=True):
        rect= image.get_rect()
        Sprite.__init__(self,x,y,rect.width,rect.height)
        self._image= image #protected
        self.__visible=isVisible #private

    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y

    @x.setter
    def x(self,value):
        self._x=value

    @y.setter
    def y(self,value):
        self._y = value
    @property
    def rect(self):
        return self._rect
    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self,isVisile):
        self.__visible = isVisile

    def draw(self,screen):
        if(self.__visible):
            screen.blit(self._image, (self._x,self._y))