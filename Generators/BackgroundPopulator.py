from Classes import Game, Sprite, DefinedLocations

RowCoords = DefinedLocations.SeatingPlan().TableRows
ColCoords = DefinedLocations.SeatingPlan().TableCols


def generateTablePlaces() -> list:
    locationArray = []
    for row in RowCoords:
        for col in ColCoords:
            locationArray.append(tuple((row, col)))
    return locationArray


def AddTables() -> None:
    for location in generateTablePlaces():
        table = Sprite.BackgroundElementSprite(
            position=location, path=Sprite.iPaths.TablePath
        )
        table.Collision = True
        Game.MasterGame.BackgroundSpriteGroup.add(table)
