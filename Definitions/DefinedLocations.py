"""Class for DefinedLocations"""

import math

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
        location = (50, 100)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)


LocationDefs = DefinedLocations()


class SeatingPlanClass:
    MinX = 150
    MaxX = 1050
    MinY = 300
    MaxY = 1000
    TableXSpacingRange = (150, 400)
    TableYSpacingRange = (100, 500)
    NumRows = 2
    NumCols = 2
    MaxRows = 7
    MaxCols = 5

    @property
    def TableXSpacing(self) -> None:
        return math.floor(
            min(
                self.TableXSpacingRange[0] * (self.MaxRows / self.NumRows),
                self.TableXSpacingRange[1],
            )
        )

    @property
    def TableYSpacing(self) -> None:
        return math.floor(
            min(
                self.TableYSpacingRange[0] * (self.MaxCols / self.NumCols),
                self.TableYSpacingRange[1],
            )
        )

    @property
    def TableXStart(self) -> int:
        return max(math.floor((self.MaxX - self.MinX) / (self.NumRows)), self.MinX)

    @property
    def TableYStart(self) -> int:
        return max(math.floor((self.MaxY - self.MinY) / (self.NumCols)), self.MinY)

    def TableRows(self) -> list[int]:
        lastTableRow = (self.NumRows * self.TableXSpacing) + self.TableXStart
        return list(range(self.TableXStart, lastTableRow, self.TableXSpacing))

    def TableCols(self) -> list[int]:
        lastTableCol = (self.NumCols * self.TableYSpacing) + self.TableYStart
        return list(range(self.TableYStart, lastTableCol, self.TableYSpacing))


SeatingPlan = SeatingPlanClass()
