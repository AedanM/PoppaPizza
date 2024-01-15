import pygame
import math
import sys

sys.path.insert(0, "..")
import Classes.utils as utils
from dataclasses import dataclass

std_dimensions = {"Medium": (1200, 800), "Small": (600, 400), "Large": (2400, 1600)}


@dataclass
class Month:
    Days: int = 31
    Name: str = ""
    MonthOrder: int = 0


Months = [
    Month(Name="January", MonthOrder=1),
    Month(Name="February", MonthOrder=2, Days=28),
    Month(Name="March", MonthOrder=3),
    Month(Name="April", MonthOrder=4, Days=30),
    Month(Name="May", MonthOrder=5),
    Month(Name="June", MonthOrder=6, Days=30),
    Month(Name="July", MonthOrder=7),
    Month(Name="August", MonthOrder=8),
    Month(Name="September", MonthOrder=9, Days=30),
    Month(Name="October", MonthOrder=10),
    Month(Name="November", MonthOrder=11, Days=30),
    Month(Name="December", MonthOrder=0),
]


class GameClock:
    clockMulRange: tuple = (0.0625, 16)
    ClockMul: float = 0.5
    Day: int = 1
    CurrentMonth: Month = Months[0]
    Minute: int = 1
    Second: int = 1

    def __init__(self, clock):
        self.pygameClock = clock
        self.lastTime = pygame.time.get_ticks()

    def UpdateClock(self):
        self.pygameClock.tick(60)
        self.Second += math.floor(
            (pygame.time.get_ticks() - self.lastTime) * self.ClockMul
        )
        self.lastTime = pygame.time.get_ticks()
        if self.Hour >= 24:
            self.DayChange()
        if self.Day >= 31:
            self.MonthChange()

    def DayChange(self):
        self.Day += 1
        self.Second = 0

        self.lastTime = pygame.time.get_ticks()

    def MonthChange(self):
        self.Day = 1
        self.CurrentMonth = [
            x
            for x in Months
            if x.MonthOrder == ((self.CurrentMonth.MonthOrder + 1) % 12)
        ][0]

    def ChangeClockMul(self, value):
        newVal = pow(2, value)
        self.ClockMul = utils.Bind(self.ClockMul * newVal, self.clockMulRange)

    @property
    def Minute(self):
        return math.floor(self.Second / 60)

    @property
    def Hour(self):
        return math.floor(self.Minute / 60)

    @property
    def dateTime(self):
        return f"{self.CurrentMonth.Name} {self.Day} {self.Hour:02d}:{(self.Minute % 60):02d}"


class Game:
    ActiveTimerBars: list = []
    CharSpriteGroup = pygame.sprite.Group()
    BackgroundSpriteGroup = pygame.sprite.Group()
    SpriteGroups: list = [BackgroundSpriteGroup, CharSpriteGroup]
    LineList: list = [(-1, -1), (1, 1)]
    WorkerList: list = []
    CustomerList: list = []
    JobList: list = []
    Money: int = 0
    TimerBars: list = []

    def __init__(self, size=std_dimensions["Medium"]):
        pygame.init()

        self.Clock = GameClock(pygame.time.Clock())
        self.startTime = pygame.time.get_ticks()

        width, height = std_dimensions[size]
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Poppa Pizza Clone")

        self.font = pygame.font.Font(None, 36)

    def DrawScreenClock(self, locationTopLeft, foreColor, backColor):
        text = self.font.render(str(self.Clock.dateTime), True, foreColor, backColor)
        textRect = text.get_rect()
        textRect.x = locationTopLeft[0]
        textRect.y = locationTopLeft[1]
        self.screen.blit(text, textRect)

    def RemoveObj(self, targetSprite):
        targetSprite.kill()
        self.CustomerList = [
            x for x in self.CustomerList if x.idNum != targetSprite.correspondingID
        ]
        self.WorkerList = [
            x for x in self.WorkerList if x.idNum != targetSprite.correspondingID
        ]
        print(self.CharSpriteGroup)


MasterGame = Game("Medium")
