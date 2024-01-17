"""Class for Game Object BaseClass"""

import pygame


class GameObject(pygame.sprite.Sprite):
    IsBackground: bool = False
    IsRendered: bool = False
    Moveable: bool = False
    Collision: bool = False

    def __init__(self, backgroundFlag, moveFlag, collisionFlag):
        super().__init__()
        self.IsBackground = backgroundFlag
        self.Moveable = moveFlag
        self.Collision = collisionFlag

    def UpdateSprite(self):
        pass

    def Update(self):
        if self.Moveable and "MvmHandler" in dir(self):
            self.MvmHandler.CalcNewPosition(self)
        self.UpdateSprite()
