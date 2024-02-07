"""Class for DefinedLocations"""

import math

from Utilities import Utils

StandardDimensions = {"Medium": (1200, 800), "Small": (600, 400), "Large": (2400, 1600)}


class DefinedLocations:
    """Defined Locations and their scaling"""

    ScreenSize = StandardDimensions["Medium"]

    @property
    def LockerRoom1(self) -> tuple:
        """Location of First Locker Room

        Returns:
            tuple: Scaled Location
        """
        location = (350, 65)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def LockerRoom2(self) -> tuple:
        """Location of Second Locker Room

        Returns:
            tuple: Scaled Location
        """
        location = (530, 65)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def LockerRoom3(self) -> tuple:
        """Location of Third Locker Room

        Returns:
            tuple: Scaled Location
        """
        location = (710, 65)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def LockerRoom4(self) -> tuple:
        """Location of Fourth Locker Room

        Returns:
            tuple: Scaled Location
        """
        location = (890, 65)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def LockerRoom5(self) -> tuple:
        """Location of Fifth Locker Room

        Returns:
            tuple: Scaled Location
        """
        location = (1070, 65)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def KitchenLocation(self) -> tuple:
        """Location of Kitchen Entrance

        Returns:
            tuple: Scaled Location
        """
        location = (220, 225)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def CustomerExit(self) -> tuple:
        """Location of Customer Exit Location

        Returns:
            tuple: Scaled Location
        """
        location = (1200, 1000)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def CustomerEntrance(self) -> tuple:
        """Location of Start of Customer Queue

        Returns:
            tuple: Scaled Location
        """
        location = (1150, 325)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def EndOfLine(self) -> tuple:
        """Location of End of Queue

        Returns:
            tuple: Scaled Location
        """
        location = (1050, 700)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def CustomerSpawn(self) -> tuple:
        """Location of Customer Spawn in

        Returns:
            tuple: Scaled Location
        """
        location = (1150, 1000)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)

    @property
    def WorkerSpawn(self) -> tuple:
        """Location of Worker Spawn

        Returns:
            tuple: Scaled Location
        """
        location = (50, 100)
        return Utils.ScaleToSize(value=location, newSize=self.ScreenSize)


LocationDefs = DefinedLocations()
TablePlaces = []


class SeatingPlanClass:
    """Generates the current seating plan"""

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
    def TableXSpacing(self) -> int:
        """Calculates the Horz Spacing between tables

        Returns:
            int: Horz Spacing
        """
        return math.floor(
            min(
                self.TableXSpacingRange[0] * (self.MaxRows / self.NumRows),
                self.TableXSpacingRange[1],
            )
        )

    @property
    def TableYSpacing(self) -> int:
        """Calculates the Vertical Spacing between tables

        Returns:
            int: Vertical Spacing
        """
        return math.floor(
            min(
                self.TableYSpacingRange[0] * (self.MaxCols / self.NumCols),
                self.TableYSpacingRange[1],
            )
        )

    @property
    def TableXStart(self) -> int:
        """Calcs the 1st tables X position

        Returns:
            int: 1st tables X position
        """
        return max(math.floor((self.MaxX - self.MinX) / (self.NumRows)), self.MinX)

    @property
    def TableYStart(self) -> int:
        """Calcs the 1st tables Y position

        Returns:
            int: 1st tables Y position
        """
        return max(math.floor((self.MaxY - self.MinY) / (self.NumCols)), self.MinY)

    def TableRows(self) -> list[int]:
        """Calculates the current table row locations

        Returns:
            list[int]: List of Row Locations
        """
        lastTableRow = (self.NumRows * self.TableXSpacing) + self.TableXStart
        return list(range(self.TableXStart, lastTableRow, self.TableXSpacing))

    def TableCols(self) -> list[int]:
        """Calculates the current table column locations

        Returns:
            list[int]: List of Column Locations
        """
        lastTableCol = (self.NumCols * self.TableYSpacing) + self.TableYStart
        return list(range(self.TableYStart, lastTableCol, self.TableYSpacing))


SeatingPlan = SeatingPlanClass()
