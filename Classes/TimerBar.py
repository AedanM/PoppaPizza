"""Class for Timer Bars"""
import math
import pygame
from Classes import Game


class TimerBar:
    Width: int = 0
    MaxWidth: int = 300
    Height: int = 25
    Color: tuple = (0, 255, 0)
    StartTime: int = 0
    AssocId: int = 0
    StartingState: int = 0
    Running: bool = False

    def __init__(
        self, duration: float, position: tuple, assocId=0, activeGame=Game.MasterGame
    ) -> None:
        self.AssocId = assocId
        self.OnComplete = lambda: None
        self.TimerRect = pygame.Rect(position[0], position[1], self.Width, self.Height)
        self.StartTime = activeGame.GameClock.Minute
        self.Duration = duration
        self.Running = True

    def StartTimer(self, activeGame=Game.MasterGame) -> None:
        self.StartTime = activeGame.GameClock.Minute
        self.Running = True

    def AgeTimer(self, activeGame=Game.MasterGame) -> None:
        if self.Running:
            completionPercentage = (
                (activeGame.GameClock.Minute - self.StartTime)
            ) / self.Duration
            self.Width = int(
                math.floor(min(completionPercentage * self.MaxWidth, self.MaxWidth))
            )
            self.TimerRect.width = self.Width
            self.TimerRect.height = self.Height
            if completionPercentage >= 1:
                self.OnComplete()
                self.Running = False
                self.AssocId = 0

    def UpdateAndDraw(self, activeGame=Game.MasterGame) -> None:
        if self.Running:
            self.AgeTimer()
            customerObj = activeGame.MatchIdToPerson(self.AssocId, "customer")
            if self.StartingState != 0 and (
                customerObj is None
                or customerObj.CurrentState.value != self.StartingState
            ):
                self.Running = False
            else:
                pygame.draw.rect(activeGame.Screen, self.Color, self.TimerRect)
