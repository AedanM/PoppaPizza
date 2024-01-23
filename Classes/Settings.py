from Utilities import Utils


class Settings:
    Clock24: bool = True
    ClockPow: int = 0
    ClockPowRange: tuple = (-4, 4)

    @property
    def ClockSpeed(self) -> float:
        return pow(base=2, exp=self.ClockPow)

    @property
    def ClockDivisor(self) -> int:
        return 13 if not self.Clock24 else 25

    def ChangeClockMul(self, value) -> None:
        self.ClockPow = Utils.Bind(self.ClockPow + value, inRange=self.ClockPowRange)
        print(self.ClockPow)

    def AMPM(self, hour) -> str:
        tag = " AM" if hour < 12 else " PM"
        return tag if not self.Clock24 else ""

    def ToggleClock24(self) -> None:
        self.Clock24 = not self.Clock24


GameSettings = Settings()
