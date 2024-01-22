"""Class for Timer Bars"""
import math
import pygame
from Classes.Game import MasterGame


class TimerBar:
    Width: int = 0
    MaxWidth: int = 300
    Height: int = 25
    Color: tuple = (0, 255, 0)
    StartTime: int = 0
    CompletionPercentage: float = 0.0

    def __init__(self, duration: float, position: tuple, activeGame=MasterGame) -> None:
        self.OnComplete = lambda: None
        self.Rect = pygame.Rect(position[0], position[1], self.Width, self.Height)
        self.StartTime = activeGame.Clock.Minute
        self.Duration = duration

    def StartTimer(self, activeGame=MasterGame) -> None:
        self.StartTime = activeGame.Clock.Minute

    def AgeTimer(self, activeGame=MasterGame) -> None:
        self.CompletionPercentage = (
            (activeGame.Clock.Minute - self.StartTime)
        ) / self.Duration
        self.Width = int(
            math.floor(min(self.CompletionPercentage * self.MaxWidth, self.MaxWidth))
        )
        self.Rect.width = self.Width
        self.Rect.height = self.Height
        if self.CompletionPercentage >= 1:
            self.OnComplete()
            activeGame.TimerBars.remove(self)

    def UpdateAndDraw(self, activeGame=MasterGame) -> None:
        self.AgeTimer()
        pygame.draw.rect(activeGame.Screen, self.Color, self.Rect)


def CreatePersonTimerBar(
    sprite, completeTask, length=5.0, activeGame=MasterGame
) -> None:
    activeGame.TimerBars.append(
        TimerBar(duration=length, position=(sprite.rect.topleft))
    )
    activeGame.TimerBars[-1].OnComplete = completeTask
    activeGame.TimerBars[-1].Rect.y -= 25
    activeGame.TimerBars[-1].MaxWidth = sprite.rect.width
    activeGame.TimerBars[-1].StartTimer()
