"""Game Clock Logic"""

import math
from dataclasses import dataclass

import pygame

from Classes import Settings
from Definitions import ColorTools, CustomEvents
from Utilities import Utils


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


# TODO- Weird Flickering between 1:00 and 8:00 in 24hr clock
class GameClock:
    """Class for a clock with custom speeds"""

    LightColor: ColorTools.Color = ColorTools.BurntOrange
    LightOpacity: int = 0
    MaxNightLight: float = 200
    LightScreenCover: float = 0.05
    NightTransitionStart: int = 12 * 60
    Day: int = 1
    CurrMonth: Month = Months[0]
    Second: int = 1
    WorkingDayStart: int = 9
    WorkingDayEnd: int = 17
    ClockMul = Settings.GameSettings.ClockSpeed
    Running: bool = False

    def __init__(self, clock) -> None:
        self.PygameClock = clock
        self.LastTime = pygame.time.get_ticks()
        self.Running = True

    def SetRunning(self, state) -> None:
        """Set the clock to running or not

        Args:
            state (bool): Running or Not
        """
        if state != self.Running:
            self.Running = state
            self.LastTime = pygame.time.get_ticks()

    def UpdateClock(self) -> None:
        """Update the clock and wait for next frame"""
        if self.Running:
            self.Second += math.floor(
                (pygame.time.get_ticks() - self.LastTime)
                * Settings.GameSettings.ClockSpeed
            )
            self.LastTime = pygame.time.get_ticks()
            self.CheckWorkingDay()
            self.ClockMul = Settings.GameSettings.ClockSpeed
            if self.Hour >= 24:
                self.DayChange()
            if self.Day >= self.CurrMonth.Days:
                self.MonthChange()
            self.UpdateLightColor()
            self.PygameClock.tick()

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

        Returns:
            int: Current Day in the Month
        """
        return self.Day - self.CurrMonth.PreceedingDays

    @property
    def Minute(self) -> int:
        """Current Minute in Day

        Returns:
            int: Minute since midnight
        """
        return math.floor(self.Second / 60)

    @property
    def Hour(self) -> int:
        """Current hour in Day

        Returns:
            int: Hour since midnight
        """
        return math.floor(self.Minute / 60)

    @property
    def DisplayHour(self) -> int:
        """Formats the hour based on game config

        Returns:
            int: Hour to display in Clock
        """
        returnVal = self.Hour % Settings.GameSettings.ClockDivisor
        if (not Settings.GameSettings.Clock24) and (self.Hour > 12 and returnVal < 12):
            returnVal += 1
        return returnVal

    @property
    def DateTime(self) -> str:
        """String of Current time and date

        Returns:
            str: Formatted String
        """
        return (
            f"{self.CurrMonth.Name} {self.DayOfMonth} "
            + f"{(self.DisplayHour):02d}:{(self.Minute % 60):02d}"
            + f"{Settings.GameSettings.AMPM(hour=self.Hour)}"
        )

    @property
    def UnixTime(self) -> int:
        """Hours since start of game

        Returns:
            int: Hours since start of game
        """
        return self.Hour + ((self.Day - 1) * 24)

    def CheckWorkingDay(self) -> None:
        """Checks if working day is over and runs the night cycle event if so"""
        if self.Hour < self.WorkingDayStart:
            self.Second = (self.WorkingDayStart - self.Hour) * 60 * 60
        elif self.Hour >= self.WorkingDayEnd:
            pygame.event.post(CustomEvents.NightCycle)
            self.Day += 1
            self.Second = self.WorkingDayStart * 60 * 60

    def UpdateLightColor(self) -> None:
        if self.Minute > self.NightTransitionStart:
            nightLight = self.MaxNightLight * (
                (self.Minute - self.NightTransitionStart)
                / (((self.WorkingDayEnd * 60) - self.NightTransitionStart))
            )
        else:
            nightLight = 0

        self.LightOpacity = Utils.Bind(
            val=nightLight,
            inRange=(
                0,
                self.MaxNightLight,
            ),
        )
