"""Class for Timer Bars"""

import pygame
import Classes.Game as Game


class TimerBar:
    Width: int = 0
    MaxWidth: int = 300
    Height: int = 25
    Color: tuple = (0, 255, 0)
    StartTime: int = 0
    CompletionPercentage: float = 0.0

    def __init__(
        self,
        duration: float,
        position: tuple,
    ):
        self.OnComplete = lambda: None
        self.Rect = pygame.Rect(position[0], position[1], self.Width, self.Height)
        self.StartTime = Game.MasterGame.Clock.Minute
        self.Duration = duration

    def StartTimer(self):
        self.StartTime = Game.MasterGame.Clock.Minute

    def AgeTimer(self):
        self.CompletionPercentage = (
            (Game.MasterGame.Clock.Minute - self.StartTime)
        ) / self.Duration
        self.Width = min(self.CompletionPercentage * self.MaxWidth, self.MaxWidth)
        self.Rect.width = self.Width
        self.Rect.height = self.Height
        if self.CompletionPercentage >= 1:
            self.OnComplete()
            Game.MasterGame.TimerBars.remove(self)


def CreatePersonTimerBar(sprite, completeTask, length=5.0):
    Game.MasterGame.TimerBars.append(TimerBar(length, (sprite.rect.topleft)))
    Game.MasterGame.TimerBars[-1].OnComplete = completeTask
    Game.MasterGame.TimerBars[-1].Rect.y -= 25
    Game.MasterGame.TimerBars[-1].MaxWidth = sprite.rect.width
    Game.MasterGame.TimerBars[-1].StartTimer()
