from Classes import Game, Sprite

RowCoords = [450, 650, 850, 1050]
ColCoords = [50, 250, 450, 650]


def generateTablePlaces() -> list:
    locationArray = []
    for row in RowCoords:
        for col in ColCoords:
            locationArray.append(tuple((row, col)))
    return locationArray


def AddTables() -> None:
    for location in generateTablePlaces():
        table = Sprite.BackgroundElementSprite(position=location, path=Sprite.iPaths.TablePath)
        table.Collision = True
        Game.MasterGame.BackgroundSpriteGroup.add(table)
