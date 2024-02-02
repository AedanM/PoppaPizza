"""Populate Background with ELements"""

from Classes import Game, Matching, Sprite
from Definitions import AssetLibrary, ColorTools, DefinedLocations, Restaurants

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


def AddButton(
    location, text, color, backColor, enabled, activeGame=Game.MasterGame
) -> None:
    buttonObj = Sprite.ButtonObject(
        position=location,
        color=color,
        backColor=backColor,
        text=text,
        size=[125, 50],
        enabled=enabled,
    )

    activeGame.ForegroundSpriteGroup.add(buttonObj)
    if not [x for x in activeGame.ButtonList if x.position == location]:
        activeGame.ButtonList.append(buttonObj)


def AddLockerRooms(activeGame=Game.MasterGame) -> None:
    for restaurant in Restaurants.RestaurantList:
        lockerRoom = restaurant.LockerRoom
        Matching.RemoveButtonFromLocation(
            activeGame=activeGame, location=lockerRoom.Location
        )
        if lockerRoom.Unlocked:
            color = lockerRoom.Color
            path = restaurant.LogoPath
            maxSize = 100
            offset = (-50, -50)
        else:
            path = AssetLibrary.ImagePath.LockedLockerRoomPath
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
        if not lockerRoom.Unlocked:
            AddButton(
                location=lockerRoom.Location,
                text="Buy Me",
                backColor=ColorTools.CautionTapeYellow,
                color=ColorTools.Black,
                enabled=lockerRoom.Price < activeGame.UserInventory.Money,
            )


def UnlockLockerRooms(activeGame) -> None:
    for button in activeGame.ButtonList:
        matchingRestaurant = [
            x
            for x in Restaurants.RestaurantList
            if x.LockerRoom.Location == button.position
        ][0]
        if matchingRestaurant.LockerRoom.Unlocked:
            activeGame.ButtonList.remove(button)


def SetupBackground(activeGame=Game.MasterGame) -> None:
    activeGame.BackgroundSpriteGroup.empty()
    AddTables(activeGame=activeGame)
    AddLockerRooms(activeGame=activeGame)
    UnlockLockerRooms(activeGame=activeGame)
