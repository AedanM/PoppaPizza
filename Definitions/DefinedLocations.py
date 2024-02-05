"""Class for DefinedLocations"""

from Utilities import Utils

StandardDimensions = {"Medium": (1200, 800), "Small": (600, 400), "Large": (2400, 1600)}


class DefinedLocations:
    ScreenSize = StandardDimensions["Medium"]

    @property
    def LockerRoom1(self) -> tuple:
        location = (350, 65)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def LockerRoom2(self) -> tuple:
        location = (530, 65)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def LockerRoom3(self) -> tuple:
        location = (710, 65)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def LockerRoom4(self) -> tuple:
        location = (890, 65)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def LockerRoom5(self) -> tuple:
        location = (1070, 65)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def KitchenLocation(self) -> tuple:
        location = (220, 225)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def CustomerExit(self) -> tuple:
        location = (1200, 1000)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def CustomerEntrance(self) -> tuple:
        location = (1150, 325)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def CustomerSpawn(self) -> tuple:
        location = (1150, 1000)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def WorkerSpawn(self) -> tuple:
        location = (100, 225)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)


LocationDefs = DefinedLocations()


class SeatingPlan:
    TableRows = [400, 550, 700, 850, 1000]
    TableCols = [300, 400, 500, 600, 700]
