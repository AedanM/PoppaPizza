"""Class for Game Object BaseClass"""

import pygame


class GameObject(pygame.sprite.Sprite):
    """Base class for all images in game"""

    IsBackground: bool = False
    IsRendered: bool = False
    Moveable: bool = False
    Collision: bool = False

    def __init__(self, backgroundFlag, moveFlag, collisionFlag) -> None:
        """Init for Game Object

        Args:
            backgroundFlag (bool): Is the object in the background
            moveFlag (bool): Can the object move
            collisionFlag (bool): Can the object collide
        """
        super().__init__()
        self.IsBackground = backgroundFlag
        self.Moveable = moveFlag
        self.Collision = collisionFlag

    def UpdateSprite(self) -> None:
        """Virtual method for inherited classes to update"""
        self.Update()

    def Update(self) -> None:
        """Update the sprite on screen"""
        if self.Moveable and "MvmHandler" in dir(self):
            self.MvmHandler.CalcNewPosition(self)
