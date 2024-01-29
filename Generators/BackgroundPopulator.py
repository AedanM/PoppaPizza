"""Populate Background with ELements"""
from Classes import Game, Sprite
from Definitions import DefinedLocations, LockerRooms, AssetLibrary

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


def AddLogos(activeGame=Game.MasterGame) -> None:
    for location, imagePath in LockerRooms.LockerRoomPaths.items():
        logo = Sprite.BackgroundElementSprite(
            position=LockerRooms.LockerRooms[location],
            path=imagePath,
            maxSize=100,
            offset=(-50, -50),
        )
        activeGame.ForegroundSpriteGroup.add(logo)


def AddLockerRooms(activeGame=Game.MasterGame) -> None:
    for location, color in LockerRooms.LockerRoomColors.items():
        rectObj = Sprite.RectangleObject(
            position=location, color=color, size=[180, 150]
        )
        activeGame.ForegroundSpriteGroup.add(rectObj)


def SetupBackground(activeGame=Game.MasterGame) -> None:
    AddTables(activeGame=activeGame)
    AddLockerRooms(activeGame=activeGame)
    AddLogos(activeGame=activeGame)
