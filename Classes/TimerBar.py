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

    def __init__(
        self, duration: float, position: tuple, assocId=0, activeGame=Game.MasterGame
    ) -> None:
        self.AssocId = assocId
        self.OnComplete = lambda: None
        self.Rect = pygame.Rect(position[0], position[1], self.Width, self.Height)
        self.StartTime = activeGame.Clock.Minute
        self.Duration = duration

    def StartTimer(self, activeGame=Game.MasterGame) -> None:
        self.StartTime = activeGame.Clock.Minute

    def AgeTimer(self, activeGame=Game.MasterGame) -> None:
        completionPercentage = (
            (activeGame.Clock.Minute - self.StartTime)
        ) / self.Duration
        self.Width = int(
            math.floor(min(completionPercentage * self.MaxWidth, self.MaxWidth))
        )
        self.Rect.width = self.Width
        self.Rect.height = self.Height
        if completionPercentage >= 1:
            self.OnComplete()
            activeGame.TimerBars.remove(self)

    def UpdateAndDraw(self, activeGame=Game.MasterGame) -> None:
        self.AgeTimer()
        customerObj = activeGame.MatchIdToPerson(self.AssocId, "customer")
        if self.StartingState != 0 and (
            customerObj is None or customerObj.CurrentState.value != self.StartingState
        ):
            activeGame.TimerBars.remove(self)
            del self
        else:
            pygame.draw.rect(activeGame.Screen, self.Color, self.Rect)


def CreatePersonTimerBar(
    sprite,
    completeTask,
    assocId=0,
    length=29.0,
    activeGame=Game.MasterGame,
    startingState=0,
) -> None:
    activeGame.TimerBars.append(
        TimerBar(
            duration=length if length != 0 else 29.0,
            position=(sprite.rect.topleft),
            assocId=assocId,
        )
    )
    activeGame.TimerBars[-1].StartingState = startingState
    activeGame.TimerBars[-1].OnComplete = completeTask
    activeGame.TimerBars[-1].Rect.y -= 25
    activeGame.TimerBars[-1].MaxWidth = sprite.rect.width
    activeGame.TimerBars[-1].StartTimer()
