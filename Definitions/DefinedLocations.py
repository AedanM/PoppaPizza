"""Class for DefinedLocations"""


class DefinedLocations:
    @property
    def LockerRoom1(self) -> tuple:
        return (350, 65)

    @property
    def LockerRoom2(self) -> tuple:
        return (530, 65)

    @property
    def LockerRoom3(self) -> tuple:
        return (710, 65)

    @property
    def LockerRoom4(self) -> tuple:
        return (890, 65)

    @property
    def LockerRoom5(self) -> tuple:
        return (1070, 65)

    @property
    def KitchenLocation(self) -> tuple:
        return (200, 225)

    @property
    def CustomerExit(self) -> tuple:
        return (1200, 1000)

    @property
    def CustomerEntrance(self) -> tuple:
        return (1150, 325)

    @property
    def CustomerSpawn(self) -> tuple:
        return (1150, 1000)


LocationDefs = DefinedLocations()


class SeatingPlan:
    TableRows = [400, 550, 700, 850, 1000]
    TableCols = [300, 400, 500, 600, 700]
