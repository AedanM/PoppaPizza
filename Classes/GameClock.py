"""Game Clock Logic"""

import pygame

from Classes import Settings
from Definitions import CustomEvents
from AtomicbritEngine.Engine import Clock


class GameClock(Clock.Clock):
    WorkingDayStart: int = 9  # 9 AM start of day
    WorkingDayEnd: int = 17  # 5 PM end of day

    def __init__(self, clock) -> None:
        super().__init__(clock=clock)

    def UpdateClock(self, clockSpeed, frameCap) -> None:
        super().UpdateClock(clockSpeed, frameCap)
        self.CheckWorkingDay()

    def CheckWorkingDay(self) -> None:
        """Checks if working day is over and runs the night cycle event if so"""
        if self.Hour < self.WorkingDayStart:
            self.Second = (self.WorkingDayStart - self.Hour) * 60 * 60
        elif self.Hour >= self.WorkingDayEnd:
            pygame.event.post(CustomEvents.NightCycle)
            self.Day += 1
            self.Second = self.WorkingDayStart * 60 * 60

    @property
    def DisplayHour(self) -> int:
        """Formats the hour based on game config

        Returns-
            int: Hour to display in Clock
        """
        returnVal = self.Hour % Settings.GameSettings.ClockDivisor
        if (not Settings.GameSettings.Clock24) and (self.Hour > 12 and returnVal < 12):
            returnVal += 1
        return returnVal

    @property
    def DateTime(self) -> str:
        """Overlaod of String of Current time and date with formatting

        Returns-
            str: Formatted String
        """
        return (
            f"{self.CurrMonth.Name} {self.DayOfMonth} "
            + f"{(self.DisplayHour):02d}:{(self.Minute % 60):02d}"
            + f"{Settings.GameSettings.AMPM(hour=self.Hour)}"
        )

    @property
    def DayPercentage(self) -> float:
        """Represents the percentage of the working day that has passed"""
        return (self.Minute - (self.WorkingDayStart * 60)) / float(
            (self.WorkingDayEnd - self.WorkingDayStart) * 60
        )
