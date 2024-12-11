"""Settings Object"""

from Engine import Utils


class Settings:
    """Game Configuration Settings"""

    Clock24: bool = True
    ClockPow: int = 0
    ClockPowRange: tuple = (-4, 4)
    CapFrames: bool = True

    @property
    def ClockSpeed(self) -> int:
        """Find the current multiplier of the clock speed

        Returns-
            int: Clock Speed Multiplier
        """
        return pow(base=2, exp=self.ClockPow)

    @property
    def ClockDivisor(self) -> int:
        """Clock Divisor for 24hr or 12hr

        Returns-
            int: Divisor to Determine Clock Range
        """
        return 13 if not self.Clock24 else 25

    def ChangeClockMul(self, value) -> None:
        """Increment the clock multiplier power

        Args-
            value (int): Increment to Clock Power
        """
        self.ClockPow = int(Utils.Bind(val=self.ClockPow + value, inRange=self.ClockPowRange))

    def SetClockMul(self, value) -> None:
        """Force certain speed of clock

        Args-
            value (int): New Speed
        """
        self.ClockPow = int(Utils.Bind(val=value, inRange=self.ClockPowRange))

    def AMPM(self, hour) -> str:
        """String for if it is AM or PM

        Args-
            hour (int): Current Hour
        """
        tag = " AM" if hour < 12 else " PM"
        return tag if not self.Clock24 else ""

    def ToggleClock24(self) -> None:
        """Toggles 24 hour clock on or off"""
        self.Clock24 = not self.Clock24

    def SetClock24(self, value) -> None:
        """Forces 24hr clock setting"""
        self.Clock24 = bool(value)


GameSettings = Settings()
