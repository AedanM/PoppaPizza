"""Class for Game Object BaseClass"""

import pygame

from Engine import MovementHandler, Utils


class GameObject(pygame.sprite.Sprite):
    """Base class for all images in game"""

    IsBackground: bool = False
    IsRendered: bool = False
    Moveable: bool = False
    Collision: bool = False

    def __init__(self, backgroundFlag, moveFlag, collisionFlag) -> None:
        """Init for Game Object

        Args-
            backgroundFlag (bool): Is the object in the background
            moveFlag (bool): Can the object move
            collisionFlag (bool): Can the object collide
        """
        super().__init__()
        self.IsBackground = backgroundFlag
        self.Moveable = moveFlag
        self.Collision = collisionFlag

    def UpdateSprite(self, activeGame) -> None:
        """Virtual method for inherited classes to update"""
        self.Update(activeGame=activeGame)

    def Update(self, activeGame) -> None:
        """Update the sprite on screen"""
        if self.Moveable:
            self.MvmHandler.CalcNewPosition(obj=self, activeGame=activeGame)


class RectangleObject(GameObject):
    """Base Rectange Object Class"""

    # pylint: disable=invalid-name
    def __init__(
        self,
        position,
        color=(0, 0, 0),
        size=(100, 100),
    ) -> None:
        """Init for rectange objects

        Args-
            position (tuple): Center position
            color (tuple, optional): Color of Rectange. Defaults to (0, 0, 0).
            size (tuple, optional): Dimensions of Rectangle. Defaults to (100, 100).
        """
        super().__init__(backgroundFlag=True, moveFlag=False, collisionFlag=False)
        self.image = pygame.Surface(size=size)
        self.image.fill(color.RGB)
        self.rect = self.image.get_rect()
        self.rect.center = position


class CharacterSprite(GameObject):
    rect: pygame.rect.Rect = pygame.rect.Rect(0, 0, 0, 0)
    MvmHandler: MovementHandler.MovementHandler = None

    def __init__(
        self,
        path,
        backgroundFlag,
        moveFlag,
        collisionFlag,
        maxSize,
        position=None,
        center=None,
    ) -> None:
        super().__init__(
            backgroundFlag=backgroundFlag,
            moveFlag=moveFlag,
            collisionFlag=collisionFlag,
        )
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        newSize = Utils.ResizeMaxLength(
            dim=(self.rect.width, self.rect.height), maxSide=maxSize
        )
        self.image = pygame.transform.scale(
            surface=self.image,
            size=newSize,
        )
        self.rect = self.image.get_rect()
        if position:
            self.rect.x = position[0]
            self.rect.y = position[1]
        elif center:
            self.rect.center = center
        self.MvmHandler = MovementHandler.MovementHandler()

    def UpdateSprite(self, activeGame) -> None:
        """Update sprite for each frame"""
        self.Update(activeGame=activeGame)
