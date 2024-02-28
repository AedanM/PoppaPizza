"""Clock class for daily and monthly working cycle"""

# BUG- Weird Flickering between 1:00 and 8:00 in 24hr clock
import math
from dataclasses import dataclass

import pygame


@dataclass
class Month:
    """Class to define a Month"""

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


class Clock:
    """Class for a clock with custom speeds"""

    Day: int = 1
    CurrMonth: Month = Months[0]
    Second: int = 1

    ClockMul: float = 1.0
    Running: bool = False

    def __init__(self, clock: pygame.Clock) -> None:
        """Creates an overloaded pygame clock class"""
        self.PygameClock = clock
        self.LastTime = pygame.time.get_ticks()
        self.Running = True

    def SetRunning(self, setRun: bool) -> None:
        """Set the clock to running or not

        Args-
            state (bool): Running or Not
        """
        if setRun != self.Running:
            self.Running = setRun
            self.LastTime = pygame.time.get_ticks()

    def UpdateClock(self, clockSpeed: float, frameCap: int) -> None:
        """Update the clock and wait for next frame"""
        if self.Running:

            self.ClockMul = clockSpeed
            self.Second += math.floor((pygame.time.get_ticks() - self.LastTime) * self.ClockMul)
            self.LastTime = pygame.time.get_ticks()

            if self.Hour >= 24:
                self.DayChange()
            if self.Day >= self.CurrMonth.Days:
                self.MonthChange()

            if frameCap:
                self.PygameClock.tick(60)
            else:
                self.PygameClock.tick()

    @property
    def DayPercentage(self) -> float:
        """Represents the percentage of the day that has passed"""
        return self.Minute / float(24 * 60)

    @property
    def DateTime(self) -> str:
        """String of Current time and date

        Returns-
            str: Formatted String
        """
        return (
            f"{self.CurrMonth.Name} {self.DayOfMonth} "
            + f"{(self.Hour):02d}:{(self.Minute % 60):02d}"
        )

    def DayChange(self) -> None:
        """Update the day as the previous ends"""
        self.Day += 1
        self.Second = 0

        self.LastTime = pygame.time.get_ticks()

    def MonthChange(self) -> None:
        """Update the month as the previous month"""

        self.CurrMonth = [
            x for x in Months if x.MonthOrder == ((self.CurrMonth.MonthOrder + 1) % 12)
        ][0]

    @property
    def DayOfMonth(self) -> int:
        """Number Day in Month

        Returns-
            int: Current Day in the Month
        """
        return self.Day - self.CurrMonth.PreceedingDays

    @property
    def Minute(self) -> int:
        """Current Minute in Day

        Returns-
            int: Minute since midnight
        """
        return math.floor(self.Second / 60)

    @property
    def Hour(self) -> int:
        """Current hour in Day

        Returns-
            int: Hour since midnight
        """
        return math.floor(self.Minute / 60)

    @property
    def UnixTime(self) -> int:
        """Seconds since start of game

        Returns-
            int: Seconds since start of game
        """
        return self.Hour + ((self.Day - 1) * 24) + self.Second

    def SetUnixTime(self, time: int) -> None:
        """Force the current time to be reset"""
        self.Second = (time % 24) * 60 * 60
        self.Day = time // 24
