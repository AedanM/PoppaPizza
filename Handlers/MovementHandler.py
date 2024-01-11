import pygame
import programUtils as utils
from enum import Enum


class MovementSpeeds(Enum):
    Slow: int = 1
    Medium: int = 10
    Fast: int = 100
    Instant: int = 1000


class CharacterMovementHandler:
    destX: int = 0
    destY: int = 0
    MaxMovementSpeed: int = MovementSpeeds.Slow
    MovementTolerance: float = 0.01
    InMotion: bool = False
    dstSet: bool = False

    def startNewMotion(self, dest, speed=MovementSpeeds.Medium):
        if not self.InMotion:
            self.destX = dest[0]
            self.destY = dest[1]
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
            print(
                obj.rect.centerx,
                obj.rect.centery,
                self.destX,
                self.destY,
                self.InMotion,
            )
            xDir = utils.sign(self.destX - obj.rect.centerx)
            yDir = utils.sign(self.destY - obj.rect.centery)
            obj.rect.centerx += (
                min(self.MaxMovementSpeed.value, abs(self.destX - obj.rect.centerx))
                * xDir
            )
            obj.rect.centery += (
                min(self.MaxMovementSpeed.value, abs(self.destY - obj.rect.centery))
                * yDir
            )
            if self.isFinished(obj):
                self.finishMovement()

    def finishMovement(self):
        self.dstSet = False
        self.InMotion = False
