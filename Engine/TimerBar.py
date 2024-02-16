"""Class for Timer Bars"""

import math

import pygame

from Engine import Color, Utils


class TimerBar:
    """Class for Progress Bars with a Running Timer"""

    Width: int = 0
    MaxWidth: int = 50
    Height: int = 25
    TimerColor: Color.Color = Color.Color(hexstring="#7eff37")
    MaxColor: Color.Color = Color.Color(hexstring="#c8c8c8")
    FillColor: Color.Color = Color.Color(hexstring="#7eff37")
    StartTime: int = 0
    AssocId: int = 0
    StartingState: int = 0
    Running: bool = False
    CompletionPercentage: float = 0.0
    AutoReset: bool = False

    def __init__(
        self,
        duration: float,
        position: tuple[int, int],
        startTime: int,
        assocId: int = 0,
        offset: tuple[int, int] = (0, 0),
        maxWidth: int = 50,
        height: int = 25,
        autoReset: bool = False,
    ) -> None:
        """Init for Timer Bar

        Args-
            duration (float): Length of timer in game minutes
            position (tuple): Poisiton of top left of timer bar
            assocId (int, optional): Character to Bind the Timer to. Defaults to 0, meaning no character.
            activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.
            offset (tuple, optional): Offset for the timer bar from position. Defaults to (0, 0).
        """
        self.AssocId = assocId
        self.OnComplete = lambda: None
        self.TimerRect = pygame.Rect(
            position[0] + offset[0],
            position[1] + offset[1] - 5,
            self.Width,
            (self.Height - 10),
        )
        self.MaxWidth = maxWidth
        self.Height = height
        self.AutoReset = autoReset
        self.MaxTimerRect = pygame.Rect(
            position[0] + offset[0], position[1] + offset[1], self.MaxWidth, self.Height
        )
        self.StartTime = startTime
        self.CompletionPercentage = 0.0
        self.Duration = duration
        self.Running = True

    @property
    def DynamicColor(self) -> tuple[int, int, int]:
        """Generates the gradient transistion between start and end colors

        Returns-
            Color.RGB: RGB representation of color
        """
        color1 = self.TimerColor.HSV
        color2 = self.FillColor.HSV
        color1Scale = 1.0 - (self.CompletionPercentage)
        color2Scale = self.CompletionPercentage
        color3 = Color.Color(
            h=math.floor(color1[0] * color1Scale + color2[0] * color2Scale),
            s=math.floor(color1[1] * color1Scale + color2[1] * color2Scale),
            v=math.floor(color1[2] * color1Scale + color2[2] * color2Scale),
        )
        return color3.RGB

    def SetMaxSize(self, size: int) -> None:
        """Update the maximum size of the timer bar

        Args-
            size (int): Max Width of Timer Bar
        """
        self.MaxWidth = size
        self.MaxTimerRect = pygame.Rect(
            # pylint: disable=E1136
            self.TimerRect.topleft[0],
            self.TimerRect.topleft[1],
            self.MaxWidth,
            self.Height,
        )

    def RestartTimer(self, currentTime: int) -> None:
        """Begins the timer and sets the reference start time

        Args-
            activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.
        """
        self.StartTime = currentTime
        self.Running = True
        self.UpdateTimer(currentTime=currentTime)

    def UpdateTimer(self, currentTime: int) -> None:
        """Increments timer based on the game clock

        Args-
            activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.
        """
        if self.Running and currentTime >= self.StartTime:
            self.CompletionPercentage = ((currentTime - self.StartTime)) / self.Duration
            self.Width = int(
                math.floor(
                    Utils.Bind(val=self.CompletionPercentage, inRange=(0, 1)) * self.MaxWidth,
                )
            )
            self.TimerRect.width = self.Width
            self.TimerRect.height = self.Height
            if self.CompletionPercentage >= 1:
                self.OnComplete()
                self.Running = False
                self.AssocId = 0
                if self.AutoReset:
                    self.RestartTimer(currentTime=currentTime)
