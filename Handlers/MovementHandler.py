"""Handler for Sprite Movement Tasks"""

from Classes import Game
from Definitions import AssetLibrary, CustomerDefs
from Handlers import QueueHandler
from Utilities import Utils as utils


class CharacterMovementHandler:
    OnComplete = None
    Dest: tuple = (0, 0)
    MaxMovementSpeed: CustomerDefs.MovementSpeeds = CustomerDefs.MovementSpeeds.Medium
    MovementTolerance: float = 0.01
    InMotion: bool = False
    DstSet: bool = False
    PointsList: list = []
    CurrentPointIdx: int = 0
    StartTime: float = 0.0

    def Reset(self) -> None:
        self.OnComplete = None
        self.FinishMovement()

    @property
    def DestY(self) -> int | float:
        return self.Dest[1]

    @property
    def DestX(self) -> int | float:
        return self.Dest[0]

    def StartNewListedMotion(
        self, pointList, speed=CustomerDefs.MovementSpeeds.Medium
    ) -> None:
        if not self.InMotion:
            self.OnComplete = lambda: None
            self.PointsList = pointList
            self.Dest = self.PointsList[0]
            self.DstSet = True
            self.InMotion: bool = True
            self.MaxMovementSpeed = speed
            self.StartTime = Game.MasterGame.GameClock.UnixTime

    def CalcNewPosition(self, obj) -> None:
        if self.DstSet and Game.MasterGame.GameClock.Running:
            if (
                obj.ImageType in AssetLibrary.CustomerOutfits
                and QueueHandler.NeedsToQueue(movingSprite=obj)
            ):
                obj.DataObject.CurrentState = CustomerDefs.CustomerStates.Queuing
            else:
                self.MoveChar(obj=obj)

            if self.IsFinished(obj=obj):
                if self.Dest == self.PointsList[len(self.PointsList) - 1]:
                    self.FinishMovement()
                else:
                    self.CurrentPointIdx += 1
                    self.Dest = self.PointsList[self.CurrentPointIdx]

    def MoveChar(self, obj) -> None:
        xDir = utils.Sign(num=self.DestX - obj.rect.centerx)
        yDir = utils.Sign(num=self.DestY - obj.rect.centery)

        xMotion = utils.Bind(
            val=abs(self.DestX - obj.rect.centerx),
            inRange=(
                1,
                self.MaxMovementSpeed.value * Game.MasterGame.GameClock.ClockMul,
            ),
        )

        yMotion = utils.Bind(
            val=abs(self.DestY - obj.rect.centery),
            inRange=(
                1,
                self.MaxMovementSpeed.value * Game.MasterGame.GameClock.ClockMul,
            ),
        )

        obj.rect.centerx += xMotion * xDir
        obj.rect.centery += yMotion * yDir

    def IsFinished(self, obj) -> bool:
        return utils.InPercentTolerance(
            num1=obj.rect.centerx, num2=self.DestX, tolerance=self.MovementTolerance
        ) and utils.InPercentTolerance(
            num1=obj.rect.centery, num2=self.DestY, tolerance=self.MovementTolerance
        )

    def FinishMovement(self) -> None:
        self.DstSet = False
        self.InMotion = False
        self.PointsList = []
        self.CurrentPointIdx = 0
        if self.OnComplete is not None:
            self.OnComplete()
