import pygame
import Classes.utils as utils
import Classes.Game as Game
import Handlers.CollisionHandler as Collision
import Handlers.PathfindingHandler as Path
from enum import Enum


class MovementSpeeds(Enum):
    Slow: int = 1
    Medium: int = 10
    Fast: int = 100
    Instant: int = 1000


class CharacterMovementHandler:
    OnComplete = None
    dest: tuple = (0, 0)
    MaxMovementSpeed: int = MovementSpeeds.Medium
    MovementTolerance: float = 0.01
    InMotion: bool = False
    dstSet: bool = False
    finalDst: bool = False
    PointsList: list = []
    currentPointIdx: int = 0

    @property
    def destY(self):
        return self.dest[1]

    @property
    def destX(self):
        return self.dest[0]

    def startNewMotion(self, start, dest, speed=MovementSpeeds.Slow):
        if not self.InMotion:
            self.OnComplete = lambda: None
            backgroundObs = [
                x.rect for x in Game.MasterGame.BackgroundSpriteGroup if x.Collision
            ]
            self.PointsList = Path.CreatePath(
                start, dest, self.MaxMovementSpeed.value, backgroundObs
            )
            self.dest = self.PointsList[0]
            self.dstSet = True
            self.InMotion: bool = True
            self.MaxMovementSpeed = speed

    def startNewListedMotion(self, pointList, speed=MovementSpeeds.Slow):
        if not self.InMotion:
            self.OnComplete = lambda: None
            self.PointsList = pointList
            self.dest = self.PointsList[0]
            self.dstSet = True
            self.InMotion: bool = True
            self.MaxMovementSpeed = speed

    def isFinished(self, obj) -> bool:
        return utils.inPercentTolerance(
            obj.rect.centerx, self.destX, self.MovementTolerance
        ) and utils.inPercentTolerance(
            obj.rect.centery, self.destY, self.MovementTolerance
        )

    def calcNewPosition(self, obj):
        if self.dstSet:
            # print(
            # obj.rect.centerx,
            # obj.rect.centery,
            # self.destX,
            # self.destY,
            # self.InMotion,
            # )
            xDir = utils.sign(self.destX - obj.rect.centerx)
            yDir = utils.sign(self.destY - obj.rect.centery)
            obj.rect.centerx += (
                max(
                    min(
                        self.MaxMovementSpeed.value * Game.MasterGame.Clock.ClockMul,
                        abs(self.destX - obj.rect.centerx),
                    ),
                    1,
                )
                * xDir
            )
            obj.rect.centery += (
                max(
                    min(
                        self.MaxMovementSpeed.value * Game.MasterGame.Clock.ClockMul,
                        abs(self.destY - obj.rect.centery),
                    ),
                    1,
                )
                * yDir
            )
            # Collision.checkCollision(obj)
            if self.isFinished(obj):
                if self.dest == self.PointsList[len(self.PointsList) - 1]:
                    self.finishMovement()
                else:
                    self.currentPointIdx += 1
                    self.dest = self.PointsList[self.currentPointIdx]

    def finishMovement(self):
        self.dstSet = False
        self.InMotion = False
        self.PointsList = []
        self.currentPointIdx = 0
        if self.OnComplete is not None:
            self.OnComplete()
