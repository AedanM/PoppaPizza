"""Populate Background with ELements"""
from Classes import Game, Sprite
from Definitions import AssetLibrary, ColorTools, DefinedLocations, LockerRooms

RowCoords = DefinedLocations.SeatingPlan().TableRows
ColCoords = DefinedLocations.SeatingPlan().TableCols


def GenerateTablePlaces() -> list:
    locationArray = []
    for row in RowCoords:
        for col in ColCoords:
            locationArray.append(tuple((row, col)))
    return locationArray


def AddTables(activeGame=Game.MasterGame) -> None:
    for location in GenerateTablePlaces():
        table = Sprite.BackgroundElementSprite(
            position=location,
            path=AssetLibrary.ImagePath.TablePath,
            maxSize=60,
            offset=(-75, 25),
        )
        table.Collision = False
        activeGame.BackgroundSpriteGroup.add(table)


def AddLockerRooms(activeGame=Game.MasterGame) -> None:
    for lockerRoom in LockerRooms.LockerRooms:
        if lockerRoom.Unlocked:
            color = lockerRoom.Color
            path = lockerRoom.Path
            maxSize = 100
            offset = (-50, -50)
        else:
            path = AssetLibrary.ImagePaths.LockedLockerRoomPath
            color = ColorTools.Grey
            maxSize = 180
            offset = (-90, -50)

        logo = Sprite.BackgroundElementSprite(
            position=lockerRoom.Location,
            path=path,
            maxSize=maxSize,
            offset=offset,
        )

        rectObj = Sprite.RectangleObject(
            position=lockerRoom.Location, color=color, size=[180, 150]
        )

        activeGame.ForegroundSpriteGroup.add(rectObj)
        activeGame.ForegroundSpriteGroup.add(logo)


def SetupBackground(activeGame=Game.MasterGame) -> None:
    AddTables(activeGame=activeGame)
    AddLockerRooms(activeGame=activeGame)
