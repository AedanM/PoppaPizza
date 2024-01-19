"""Class for Game Object BaseClass"""

import pygame


class GameObject(pygame.sprite.Sprite):
    IsBackground: bool = False
    IsRendered: bool = False
    Moveable: bool = False
    Collision: bool = False

    def __init__(self, backgroundFlag, moveFlag, collisionFlag) -> None:
        super().__init__()
        self.IsBackground = backgroundFlag
        self.Moveable = moveFlag
        self.Collision = collisionFlag

    def UpdateSprite(self) -> None:
        pass

    def Update(self) -> None:
        if self.Moveable and "MvmHandler" in dir(self):
            self.MvmHandler.CalcNewPosition(self)
        self.UpdateSprite()
