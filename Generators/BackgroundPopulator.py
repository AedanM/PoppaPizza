from Classes import Game, Sprite, DefinedLocations
from Assets import AssetLibrary

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
    locationToLogos = {
        DefinedLocations.LocationDefs.PinkLockerRoom: AssetLibrary.ImagePath.LuauPath,
        DefinedLocations.LocationDefs.YellowLockerRoom: AssetLibrary.ImagePath.CoffeePath,
        DefinedLocations.LocationDefs.BlueLockerRoom: AssetLibrary.ImagePath.CowboyPath,
        DefinedLocations.LocationDefs.GreyLockerRoom: AssetLibrary.ImagePath.SuitPath,
    }
    for location, imagePath in locationToLogos.items():
        logo = Sprite.BackgroundElementSprite(
            position=location, path=imagePath, maxSize=100
        )
        Game.MasterGame.BackgroundSpriteGroup.add(logo)


def SetupBackground(activeGame=Game.MasterGame) -> None:
    AddTables()
    AddLogos()
