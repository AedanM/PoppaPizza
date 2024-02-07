"""Class for Timer Bars"""

import math

import pygame

from Classes import Game, Matching
from Definitions import ColorTools


class TimerBar:
    """Class for Progress Bars with a Running Timer"""

    Width: int = 0
    MaxWidth: int = 50
    Height: int = 25
    Color: ColorTools.Color = ColorTools.LimeGreen
    MaxColor: ColorTools.Color = ColorTools.Grey
    FillColor: ColorTools.Color = ColorTools.LimeGreen
    StartTime: int = 0
    AssocId: int = 0
    StartingState: int = 0
    Running: bool = False
    CompletionPercentage: float = 0.0

    def __init__(
        self,
        duration: float,
        position: tuple,
        assocId=0,
        activeGame=Game.MasterGame,
        offset=(0, 0),
    ) -> None:
        """Init for Timer Bar

        Args:
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
        self.MaxTimerRect = pygame.Rect(
            position[0] + offset[0], position[1] + offset[1], self.MaxWidth, self.Height
        )
        self.StartTime = activeGame.GameClock.Minute
        self.CompletionPercentage = 0.0
        self.Duration = duration
        self.Running = True

    @property
    def DynamicColor(
        self,
    ) -> Color.RGB:
        """Generates the gradient transistion between start and end colors

        Returns:
            Color.RGB: RGB representation of color
        """
        color1 = self.Color.HSV
        color2 = self.FillColor.HSV
        color1Scale = 1.0 - (self.CompletionPercentage)
        color2Scale = self.CompletionPercentage
        color3 = ColorTools.Color(
            h=math.floor(color1[0] * color1Scale + color2[0] * color2Scale),
            s=math.floor(color1[1] * color1Scale + color2[1] * color2Scale),
            v=math.floor(color1[2] * color1Scale + color2[2] * color2Scale),
        )
        return color3.RGB

    def SetMaxSize(self, size) -> None:
        """Update the maximum size of the timer bar

        Args:
            size (int | float): Max Width of Timer Bar
        """
        self.MaxWidth = size
        self.MaxTimerRect = pygame.Rect(
            # pylint: disable=E1136
            self.TimerRect.topleft[0],
            self.TimerRect.topleft[1],
            self.MaxWidth,
            self.Height,
        )

    def StartTimer(self, activeGame=Game.MasterGame) -> None:
        """Begins the timer and sets the reference start time

        Args:
            activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.
        """
        self.StartTime = activeGame.GameClock.Minute
        self.Running = True

    def AgeTimer(self, activeGame=Game.MasterGame) -> None:
        """Increments timer based on the game clock

        Args:
            activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.
        """
        if self.Running:
            self.CompletionPercentage = (
                (activeGame.GameClock.Minute - self.StartTime)
            ) / self.Duration
            self.Width = int(
                math.floor(
                    min(self.CompletionPercentage * self.MaxWidth, self.MaxWidth)
                )
            )
            self.TimerRect.width = self.Width
            self.TimerRect.height = self.Height
            if self.CompletionPercentage >= 1:
                self.OnComplete()
                self.Running = False
                self.AssocId = 0

    def UpdateAndDraw(self, activeGame=Game.MasterGame) -> None:
        """Update Timer Dimensions and Redraw if active

        Args:
            activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.
        """
        if self.Running:
            self.AgeTimer()
            customerObj = Matching.MatchIdToPerson(
                activeGame=activeGame, inputId=self.AssocId, targetOutput="customer"
            )
            if (
                self.StartingState != 0
                and self.AssocId != 0
                and (
                    customerObj is None
                    or customerObj.CurrentState.value != self.StartingState
                )
            ):
                self.Running = False
            else:
                pygame.draw.rect(
                    activeGame.Screen,
                    self.MaxColor.RGB,
                    self.MaxTimerRect,
                )
                pygame.draw.rect(
                    activeGame.Screen,
                    self.DynamicColor,
                    self.TimerRect,
                )
