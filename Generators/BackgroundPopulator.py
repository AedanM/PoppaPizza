import pygame
from Classes import Game, Sprite
from Assets import AssetLibrary
from Definitions import DefinedLocations, LockerRooms

RowCoords = DefinedLocations.SeatingPlan().TableRows
ColCoords = DefinedLocations.SeatingPlan().TableCols


def generateTablePlaces() -> list:
    locationArray = []
    for row in RowCoords:
        for col in ColCoords:
            locationArray.append(tuple((row, col)))
    return locationArray


def AddTables(activeGame=Game.MasterGame) -> None:
    for location in generateTablePlaces():
        table = Sprite.BackgroundElementSprite(
            position=location, path=AssetLibrary.ImagePath.TablePath, maxSize=60
        )
        table.Collision = True
        Game.MasterGame.BackgroundSpriteGroup.add(table)


def AddLogos() -> None:
    for location, imagePath in LockerRooms.LockerRoomPaths.items():
        logo = Sprite.BackgroundElementSprite(
            position=LockerRooms.LockerRooms[location], path=imagePath, maxSize=100
        )
        Game.MasterGame.ForegroundSpriteGroup.add(logo)


def AddLockerRooms() -> None:
    for location, color in LockerRooms.LockerRoomColors.items():
        rectObj = Sprite.RectangleObject(
            position=location, color=color, size=[180, 150]
        )
        Game.MasterGame.ForegroundSpriteGroup.add(rectObj)


def SetupBackground(activeGame=Game.MasterGame) -> None:
    AddTables()
    AddLockerRooms()
    AddLogos()
