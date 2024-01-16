import pygame


class GameObject(pygame.sprite.Sprite):
    isBackground: bool = False
    isRendered: bool = False
    Moveable: bool = False
    Collision: bool = False

    def __init__(self, backgroundFlag, moveFlag, collisionFlag):
        super().__init__()
        self.isBackground = backgroundFlag
        self.Moveable = moveFlag
        self.Collision = collisionFlag

    def updateSprite(self):
        pass

    def update(self):
        if self.Moveable and "MvmHandler" in dir(self):
            self.MvmHandler.calcNewPosition(self)
        self.updateSprite()
