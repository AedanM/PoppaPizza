import pygame
from dataclasses import dataclass
import math
from Utilities import Utils
from Classes.Settings import GameSettings


@dataclass
class Month:
    Days: int = 31
    Name: str = ""
    MonthOrder: int = 0
    PreceedingDays: int = 0


Months = [
    Month(Name="January", MonthOrder=1, PreceedingDays=0),
    Month(Name="February", MonthOrder=2, Days=28, PreceedingDays=31),
    Month(Name="March", MonthOrder=3, PreceedingDays=59),
    Month(Name="April", MonthOrder=4, Days=30, PreceedingDays=90),
    Month(Name="May", MonthOrder=5, PreceedingDays=120),
    Month(Name="June", MonthOrder=6, Days=30, PreceedingDays=151),
    Month(Name="July", MonthOrder=7, PreceedingDays=181),
    Month(Name="August", MonthOrder=8, PreceedingDays=212),
    Month(Name="September", MonthOrder=9, Days=30, PreceedingDays=243),
    Month(Name="October", MonthOrder=10, PreceedingDays=273),
    Month(Name="November", MonthOrder=11, Days=30, PreceedingDays=304),
    Month(Name="December", MonthOrder=0, PreceedingDays=334),
]


class GameClock:
    Day: int = 1
    CurrMonth: Month = Months[0]
    Second: int = 1
    WorkingDayStart: int = 9
    WorkingDayEnd: int = 17
    ClockMul = GameSettings.ClockSpeed

    def __init__(self, clock) -> None:
        self.PygameClock = clock
        self.LastTime = pygame.time.get_ticks()

    def UpdateClock(self) -> None:
        self.PygameClock.tick(60)
        self.Second += math.floor(
            (pygame.time.get_ticks() - self.LastTime) * GameSettings.ClockSpeed
        )
        self.LastTime = pygame.time.get_ticks()
        self.CheckWorkingDay()
        self.ClockMul = GameSettings.ClockSpeed
        if self.Hour >= 24:
            self.DayChange()
        if self.Day >= self.CurrMonth.Days:
            self.MonthChange()

    def DayChange(self) -> None:
        self.Day += 1
        self.Second = 0

        self.LastTime = pygame.time.get_ticks()

    def MonthChange(self) -> None:
        self.CurrMonth = [
            x for x in Months if x.MonthOrder == ((self.CurrMonth.MonthOrder + 1) % 12)
        ][0]

    @property
    def DayOfMonth(self) -> int:
        return self.Day - self.CurrMonth.PreceedingDays

    @property
    def Minute(self) -> int:
        return math.floor(self.Second / 60)

    @property
    def Hour(self) -> int:
        return math.floor(self.Minute / 60)

    @property
    def DateTime(self) -> str:
        return f"{self.CurrMonth.Name} {self.DayOfMonth} {(self.Hour % GameSettings.ClockDivisor):02d}:{(self.Minute % 60):02d}{GameSettings.AMPM(self.Hour)}"

    @property
    def UnixTime(self) -> int:
        return self.Hour + ((self.Day - 1) * 24)

    def CheckWorkingDay(self) -> None:
        if self.Hour < self.WorkingDayStart:
            self.Second = (self.WorkingDayStart - self.Hour) * 60 * 60
        elif self.Hour >= self.WorkingDayEnd:
            self.NightCycle()
            self.Day += 1  #

            self.Second = self.WorkingDayStart * 60 * 60

    def NightCycle(self) -> None:
        pass
