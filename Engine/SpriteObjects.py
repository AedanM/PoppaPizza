"""Class for Game Object BaseClass"""

from typing import Any

import pygame
from Engine import Color, Game, MovementHandler, Utils


class GameObject(pygame.sprite.Sprite):
    """Base class for all images in game"""

    Rectangle: pygame.Rect = pygame.Rect(0, 0, 0, 0)
    IsBackground: bool = False
    IsRendered: bool = False
    Moveable: bool = False
    Collision: bool = False

    def __init__(self, backgroundFlag: bool, moveFlag: bool, collisionFlag: bool) -> None:
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

    def UpdateSprite(self, activeGame: Game.Game) -> None:
        """Virtual method for inherited classes to update"""
        self.Update(activeGame=activeGame)

    def Update(self, activeGame: Game.Game) -> None:
        """Update the sprite on screen"""
        if self.Moveable:
            self.MvmHandler.CalcNewPosition(obj=self, activeGame=activeGame)  # type: ignore

    def __hash__(self) -> int:
        """Overload of hash method"""
        return super().__hash__() + sum(self.Rectangle)


class RectangleObject(GameObject):
    """Base Rectangle Object Class"""

    # pylint: disable=invalid-name
    def __init__(
        self,
        position: tuple[int, int],
        color: Color.Color = Color.Color(hexstring="#000000"),
        size: tuple[int, int] = (100, 100),
    ) -> None:
        """Init for rectangle objects

        Args-
            position (tuple): Center position
            color (tuple, optional): Color of Rectangle. Defaults to (0, 0, 0).
            size (tuple, optional): Dimensions of Rectangle. Defaults to (100, 100).
        """
        super().__init__(backgroundFlag=True, moveFlag=False, collisionFlag=False)
        self.image = pygame.Surface(size=size)
        self.image.fill(color.RGB)
        self.Rectangle = self.image.get_rect()
        self.Rectangle.center = position


class CharacterSprite(GameObject):
    Rectangle: pygame.rect.Rect = pygame.rect.Rect(0, 0, 0, 0)
    MvmHandler: MovementHandler.MovementHandler = None  # type: ignore

    def __init__(
        self,
        path: str,
        backgroundFlag: bool,
        moveFlag: bool,
        collisionFlag: bool,
        maxSize: int,
        position: tuple[int, int] = None,  # type: ignore
        center: tuple[int, int] = None,  # type: ignore
    ) -> None:
        super().__init__(
            backgroundFlag=backgroundFlag,
            moveFlag=moveFlag,
            collisionFlag=collisionFlag,
        )
        # pylint:disable=C0103
        self.image = pygame.image.load(path).convert_alpha()
        self.Rectangle = self.image.get_rect()
        newSize = Utils.ResizeMaxLength(
            dim=(self.Rectangle.width, self.Rectangle.height), maxSide=maxSize
        )
        self.image = pygame.transform.scale(
            surface=self.image,
            size=newSize,
        )
        self.Rectangle = self.image.get_rect()
        if position:
            self.Rectangle.x = position[0]
            self.Rectangle.y = position[1]
        elif center:
            self.Rectangle.center = center
        self.MvmHandler = MovementHandler.MovementHandler()

    def UpdateSprite(self, activeGame: Game.Game) -> None:
        """Update sprite for each frame"""
        self.Update(activeGame=activeGame)

    @property
    def DataObject(self) -> Any:
        return 0

    def __hash__(self) -> int:
        """Overload of hash method"""
        return super().__hash__() + hash(self.DataObject)
