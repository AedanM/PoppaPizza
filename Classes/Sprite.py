"""Class for visibile sprites"""
from dataclasses import dataclass
from enum import Enum
import pygame
from Classes import GameObject, Game, TimerBar
from Utilities import Utils as utils
from Handlers.MovementHandler import CharacterMovementHandler
from Assets import AssetLibrary

ImageTypes = AssetLibrary.ImageTypes


class CharImageSprite(GameObject.GameObject):
    # pylint: disable=invalid-name
    CorrespondingID: int = 0
    ImageType: ImageTypes = ImageTypes.Null
    rect: pygame.rect.Rect = pygame.rect.Rect(0, 0, 0, 0)
    MvmHandler: CharacterMovementHandler = None
    PersonalTimer: TimerBar.TimerBar = None

    def __init__(self, position, path, objID, activateGame=Game.MasterGame) -> None:
        super().__init__(backgroundFlag=False, moveFlag=True, collisionFlag=True)
        self.image = pygame.image.load(
            path
        )  # Replace with the actual sprite image file

        self.image = pygame.transform.scale_by(surface=self.image, factor=0.08)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.MvmHandler = CharacterMovementHandler()
        self.ImageType = AssetLibrary.PathToTypeDict[path]
        self.CheckSpawnCollision()

        self.CorrespondingID = objID

    def CheckSpawnCollision(self, activeGame=Game.MasterGame) -> None:
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
        if self.PersonalTimer is not None:
            self.PersonalTimer.UpdateAndDraw()
            self.PersonalTimer.Rect = self.rect.topleft
        self.Update()

    def CreatePersonTimerBar(
        sprite,
        completeTask,
        assocId=0,
        length=29.0,
        startingState=0,
    ) -> None:
        sprite.PersonalTimer = TimerBar.TimerBar(
            duration=length if length != 0 else 29.0,
            position=(sprite.rect.topleft),
            assocId=assocId,
        )
        sprite.PersonalTimer.StartingState = startingState
        sprite.PersonalTimer.OnComplete = completeTask
        sprite.PersonalTimer.TimerRect.y -= 25
        sprite.PersonalTimer.MaxWidth = sprite.rect.width
        sprite.PersonalTimer.StartTimer()

    def __repr__(self) -> str:
        return str(self.CorrespondingID) + " " + str(self.ImageType)


class BackgroundElementSprite(GameObject.GameObject):
    ImageType: ImageTypes = ImageTypes.Null

    # pylint: disable=invalid-name
    def __init__(
        self, position, path, activateGame=Game.MasterGame, maxSize=60
    ) -> None:
        super().__init__(backgroundFlag=True, moveFlag=False, collisionFlag=False)
        self.image = pygame.image.load(
            path
        )  # Replace with the actual sprite image file
        self.rect = self.image.get_rect()
        dim = utils.ResizeMaxLength(
            dim=(self.rect.width, self.rect.height), maxSide=maxSize
        )
        self.image = pygame.transform.scale(self.image, dim)
        self.rect.x = position[0] - dim[0] / 2

        self.rect.y = position[1] - dim[1] / 2
        self.ImageType = AssetLibrary.PathToTypeDict[path]
