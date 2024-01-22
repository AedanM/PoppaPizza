"""Handler for Sprite Movement Tasks"""
from enum import Enum
import Utilities.Utils as utils
from Classes import Game

# from Handlers import PathfindingHandler as Path


class MovementSpeeds(Enum):
    Slow: int = 1
    Medium: int = 10
    Fast: int = 100
    Instant: int = 1000


class CharacterMovementHandler:
    OnComplete = None
    Dest: tuple = (0, 0)
    MaxMovementSpeed: MovementSpeeds = MovementSpeeds.Medium
    MovementTolerance: float = 0.01
    InMotion: bool = False
    DstSet: bool = False
    PointsList: list = []
    CurrentPointIdx: int = 0

    @property
    def DestY(self) -> int | float:
        return self.Dest[1]

    @property
    def DestX(self) -> int | float:
        return self.Dest[0]

    def StartNewMotion(self, start, dst, speed=MovementSpeeds.Medium) -> None:
        if not self.InMotion:
            self.OnComplete = lambda: None
            backgroundObs = [
                x.rect for x in Game.MasterGame.BackgroundSpriteGroup if x.Collision
            ]
            self.PointsList = [start, dst]  # Path.CreatePath(
            #    startPoint=start,
            #    endPoint=dst,
            #    speed=self.MaxMovementSpeed.value,
            #    backgroundObs=backgroundObs,
            # )
            self.Dest = self.PointsList[0]
            self.DstSet = True
            self.InMotion: bool = True
            self.MaxMovementSpeed = speed

    def StartNewListedMotion(self, pointList, speed=MovementSpeeds.Medium) -> None:
        if not self.InMotion:
            self.OnComplete = lambda: None
            self.PointsList = pointList
            self.Dest = self.PointsList[0]
            self.DstSet = True
            self.InMotion: bool = True
            self.MaxMovementSpeed = speed

    def IsFinished(self, obj) -> bool:
        return utils.InPercentTolerance(
            num1=obj.rect.centerx, num2=self.DestX, tolerance=self.MovementTolerance
        ) and utils.InPercentTolerance(
            num1=obj.rect.centery, num2=self.DestY, tolerance=self.MovementTolerance
        )

    def CalcNewPosition(self, obj):
        if self.DstSet:
            # print(
            # obj.rect.centerx,
            # obj.rect.centery,
            # self.DestX,
            # self.DestY,
            # self.InMotion,
            # )
            xDir = utils.Sign(num=self.DestX - obj.rect.centerx)
            yDir = utils.Sign(num=self.DestY - obj.rect.centery)
            obj.rect.centerx += (
                max(
                    min(
                        self.MaxMovementSpeed.value * Game.MasterGame.Clock.ClockMul,
                        abs(self.DestX - obj.rect.centerx),
                    ),
                    1,
                )
                * xDir
            )
            obj.rect.centery += (
                max(
                    min(
                        self.MaxMovementSpeed.value * Game.MasterGame.Clock.ClockMul,
                        abs(self.DestY - obj.rect.centery),
                    ),
                    1,
                )
                * yDir
            )
            # Collision.checkCollision(obj)
            if self.IsFinished(obj=obj):
                if self.Dest == self.PointsList[len(self.PointsList) - 1]:
                    self.FinishMovement()
                else:
                    self.CurrentPointIdx += 1
                    self.Dest = self.PointsList[self.CurrentPointIdx]

    def FinishMovement(self) -> None:
        self.DstSet = False
        self.InMotion = False
        self.PointsList = []
        self.CurrentPointIdx = 0
        if self.OnComplete is not None:
            self.OnComplete()
