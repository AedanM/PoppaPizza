"""Handler for Sprite Movement Tasks"""

from Engine import Utils


class MovementSpeeds:
    """Defined Speeds for Motion"""

    Slow: int = 1
    Medium: int = 10
    Fast: int = 100
    Instant: int = 1000


class MovementHandler:
    OnComplete = None
    Dest: tuple = (0, 0)
    MaxMovementSpeed: int = MovementSpeeds.Medium
    MovementTolerance: float = 0.01
    InMotion: bool = False
    DstSet: bool = False
    PointsList: list = []
    CurrentPointIdx: int = 0
    StartTime: float = 0.0

    def Reset(self) -> None:
        """Reset OnComplete function and Finish any active movements"""
        self.OnComplete = None
        self.FinishMovement()

    @property
    def DestY(self) -> int | float:
        """Y Coord of Destination"""
        return self.Dest[1]

    @property
    def DestX(self) -> int | float:
        """X Coord of Destination"""
        return self.Dest[0]

    def StartNewListedMotion(self, pointList, speed=10) -> None:
        """Start point for Motion

            Takes a list of positions and begins the animation of a sprite between them

        Args-
            pointList (list[tuple]): List of Tuple Positions
            speed (CustomerDefs.MovementSpeeds, optional): Speed of Motion. Defaults to CustomerDefs.MovementSpeeds.Medium.
        """
        if not self.InMotion:
            self.OnComplete = lambda: None
            self.PointsList = pointList
            self.Dest = self.PointsList[0]
            self.DstSet = True
            self.InMotion: bool = True
            self.MaxMovementSpeed = speed

    def MoveChar(self, obj, gameSpeed) -> None:
        """Update Location of Character

        Args-
            obj (Sprite): Moving Sprite
        """
        xDir = Utils.Sign(num=self.DestX - obj.rect.centerx)
        yDir = Utils.Sign(num=self.DestY - obj.rect.centery)

        xMotion = Utils.Bind(
            val=abs(self.DestX - obj.rect.centerx),
            inRange=(
                1,
                self.MaxMovementSpeed * gameSpeed,
            ),
        )

        yMotion = Utils.Bind(
            val=abs(self.DestY - obj.rect.centery),
            inRange=(
                1,
                self.MaxMovementSpeed * gameSpeed,
            ),
        )

        obj.rect.centerx += xMotion * xDir
        obj.rect.centery += yMotion * yDir

    def IsFinished(self, obj) -> bool:
        """Checks if final destination reached within a tolerance

        Args-
            obj (Sprite): Moving Sprite

        Returns-
            bool: Is Motion Finished
        """
        return Utils.InPercentTolerance(
            num1=obj.rect.centerx, num2=self.DestX, tolerance=self.MovementTolerance
        ) and Utils.InPercentTolerance(
            num1=obj.rect.centery, num2=self.DestY, tolerance=self.MovementTolerance
        )

    def FinishMovement(self) -> None:
        """Wraps up motion and activates on complete function if exists"""
        self.DstSet = False
        self.InMotion = False
        self.PointsList = []
        self.CurrentPointIdx = 0
        if self.OnComplete is not None:
            self.OnComplete()

    def CalcNewPosition(self, obj, gameSpeed) -> None:
        if self.DstSet:
            self.MoveChar(obj=obj, gameSpeed=gameSpeed)
            if self.IsFinished(obj=obj):
                if self.Dest == self.PointsList[len(self.PointsList) - 1]:
                    self.FinishMovement()
                else:
                    self.CurrentPointIdx += 1
                    self.Dest = self.PointsList[self.CurrentPointIdx]
