"""Class for visibile sprites"""
from dataclasses import dataclass
from enum import Enum
import pygame
from Classes import GameObject
from Classes.Game import MasterGame
from Utilities import Utils as utils
from Handlers.MovementHandler import CharacterMovementHandler

ImageTypes = MasterGame.ImageTypes


class CharImageSprite(GameObject.GameObject):
    # pylint: disable=invalid-name
    CorrespondingID: int = 0
    ImageType: ImageTypes = ImageTypes.Null
    rect: pygame.rect.Rect = pygame.rect.Rect(0, 0, 0, 0)
    MvmHandler: CharacterMovementHandler = None

    def __init__(self, position, path, objID, activateGame=MasterGame) -> None:
        super().__init__(backgroundFlag=False, moveFlag=True, collisionFlag=True)
        self.image = pygame.image.load(
            path
        )  # Replace with the actual sprite image file

        self.image = pygame.transform.scale_by(surface=self.image, factor=0.1)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.MvmHandler = CharacterMovementHandler()
        self.ImageType = activateGame.PathToTypeDict[path]
        self.CheckSpawnCollision()

        self.CorrespondingID = objID

    def CheckSpawnCollision(self, activeGame=MasterGame) -> None:
        currentCenter = self.rect.center
        for group in activeGame.SpriteGroups:
            for sprite in group:
                while sprite.rect.colliderect(self.rect) and sprite is not self:
                    self.rect.center = utils.PositionRandomVariance(
                        position=currentCenter,
                        percentVarianceTuple=(0.1, 1),
                        screenSize=activeGame.ScreenSize,
                    )

    def UpdateSprite(self) -> None:
        ## Place to add Dynamic Sprites
        pass

    def __repr__(self) -> str:
        return str(self.CorrespondingID) + " " + str(self.ImageType)


class BackgroundElementSprite(GameObject.GameObject):
    ImageType: ImageTypes = ImageTypes.Null

    # pylint: disable=invalid-name
    def __init__(self, position, path, activateGame=MasterGame) -> None:
        super().__init__(backgroundFlag=True, moveFlag=False, collisionFlag=False)
        self.image = pygame.image.load(
            path
        )  # Replace with the actual sprite image file
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect.y = position[1]
        self.ImageType = activateGame.PathToTypeDict[path]
