from Utilities import Utils


class Settings:
    Clock24: bool = True
    ClockPow: int = 0
    ClockPowRange: tuple = (-4, 4)

    @property
    def ClockSpeed(self) -> float:
        return pow(2, self.ClockPow)

    # TODO - Fix 1PM on 12hr clock
    @property
    def ClockDivisor(self) -> int:
        return 13 if not self.Clock24 else 25

    def ChangeClockMul(self, value):
        self.ClockPow = Utils.Bind(self.ClockPow + value, self.ClockPowRange)
        print(self.ClockPow)

    def AMPM(self, hour):
        tag = " AM" if hour < 12 else " PM"
        return tag if not self.Clock24 else ""


GameSettings = Settings()
