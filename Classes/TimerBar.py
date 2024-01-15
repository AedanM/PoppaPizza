import pygame
import Classes.Game as Game


class TimerBar:
    width: int = 0
    maxWidth: int = 300
    height: int = 25
    color: tuple = (0, 255, 0)
    startTime: int = 0
    completionPercentage: float = 0.0

    def __init__(
        self,
        duration: float,
        position: tuple,
    ):
        self.OnComplete = lambda: None
        self.Rect = pygame.Rect(position[0], position[1], self.width, self.height)
        self.startTime = Game.MasterGame.Clock.Minute
        self.duration = duration

    def startTimer(self):
        self.startTime = Game.MasterGame.Clock.Minute

    def ageTimer(self):
        self.completionPercentage = (
            (Game.MasterGame.Clock.Minute - self.startTime)
        ) / self.duration
        self.width = min(self.completionPercentage * self.maxWidth, self.maxWidth)
        self.Rect.width = self.width
        self.Rect.height = self.height
        if self.completionPercentage >= 1:
            self.OnComplete()
            Game.MasterGame.TimerBars.remove(self)


def CreatePersonTimerBar(sprite, obj, completeTask, length=5.0):
    Game.MasterGame.TimerBars.append(TimerBar(length, (sprite.rect.topleft)))
    Game.MasterGame.TimerBars[-1].OnComplete = completeTask
    Game.MasterGame.TimerBars[-1].Rect.y -= 25
    Game.MasterGame.TimerBars[-1].maxWidth = sprite.rect.width
    Game.MasterGame.TimerBars[-1].startTimer()
