"""Handler for Sprite Movement Tasks"""
from Definitions import CustomerDefs, AssetLibrary
from Utilities import Utils as utils
from Classes import Game

# from Handlers import PathfindingHandler as Path

MAXMOVEMENT = 3
QUEUEDISTANCE = 75


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

    def NeedsToQueue(self, movingSprite) -> bool:
        match movingSprite.DataObject.CurrentState:
            case CustomerDefs.CustomerStates.Queuing:
                if self.FirstInLine(movingSprite=movingSprite):
                    movingSprite.DataObject.CurrentState = (
                        CustomerDefs.CustomerStates.FirstInLine
                    )
                    return False
                else:
                    movingSprite.DataObject.CurrentState = (
                        CustomerDefs.CustomerStates.WalkingIn
                    )
                    return self.NeedsToQueue(movingSprite=movingSprite)
            case CustomerDefs.CustomerStates.WalkingIn:
                for sprite in Game.MasterGame.CharSpriteGroup:
                    if (
                        sprite.ImageType in AssetLibrary.CustomerOutfits
                        and sprite is not movingSprite
                        and sprite.DataObject.CurrentState in CustomerDefs.QueueStates
                    ):
                        if utils.PositionInTolerance(
                            pos1=sprite.rect.center,
                            pos2=movingSprite.rect.center,
                            tolerance=QUEUEDISTANCE,
                        ):
                            return True
            # pylint: disable=unused-variable
            case other:
                return False

    def FirstInLine(self, movingSprite) -> bool:
        for sprite in Game.MasterGame.CharSpriteGroup:
            if (
                sprite is not movingSprite
                and sprite.rect.centerx == movingSprite.rect.centerx
                and sprite.rect.centery < movingSprite.rect.centery
            ):
                return False
        return True

    def CalcNewPosition(self, obj) -> None:
        if self.DstSet and Game.MasterGame.GameClock.Running:
            if obj.ImageType in AssetLibrary.CustomerOutfits and self.NeedsToQueue(
                movingSprite=obj
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
