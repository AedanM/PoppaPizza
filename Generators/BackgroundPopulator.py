"""Populate Background with Elements"""

from Classes import Game, Matching, Sprite
from Definitions import AssetLibrary, ColorTools, DefinedLocations, Restaurants
from Utilities import Utils


def GenerateTablePlaces() -> list:
    """Generates list of table position tuples

    Returns:
        list: Array of Tuple Positions
    """
    locationArray = []
    for row in DefinedLocations.SeatingPlan.TableRows():
        for col in DefinedLocations.SeatingPlan.TableCols():
            locationArray.append(tuple((row, col)))
    return locationArray


# TODO - Stop Recalcing Tables


def AddTables(activeGame=Game.MasterGame) -> None:
    """Places tables as they are unlocked

    Args:
        activeGame (Game, optional): Current Game being used. Defaults to Game.MasterGame.
    """
    if DefinedLocations.TablePlaces is []:
        DefinedLocations.TablePlaces = GenerateTablePlaces()
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
    """Generates a Button on a specified location

    Args:
        location (tuple): tuple position of button center
        text (str): Button Label
        color (Color): Main Color
        backColor (Color): Background Color of Button
        enabled (bool): Button Enable
        activeGame (Game, optional): Current Game being used. Defaults to Game.MasterGame.
    """
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
    """Generate and Add Locker Rooms based on locked status

    Args:
        activeGame (Game, optional): Current Game Class being used. Defaults to Game.MasterGame.
    """
    for restaurant in Restaurants.RestaurantList:
        lockerRoom = restaurant.LockerRoom
        Matching.RemoveButtonFromLocation(
            activeGame=activeGame, location=lockerRoom.Location
        )
        if lockerRoom.Unlocked:
            color = lockerRoom.Color
            path = restaurant.LogoPath
            maxSize = 100
            offset = Utils.ScaleToSize(
                value=(-50, -50), newSize=DefinedLocations.LocationDefs.ScreenSize
            )
        else:
            path = AssetLibrary.ImagePath.LogoLockedPath
            color = ColorTools.Grey
            maxSize = 180
            offset = Utils.ScaleToSize(
                value=(-90, -50), newSize=DefinedLocations.LocationDefs.ScreenSize
            )

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
    """Updates the locker rooms to unlock the purchased rooms

    Args:
        activeGame (Game): Current Game Class being used
    """
    for button in activeGame.ButtonList:
        matchingRestaurant = [
            x
            for x in Restaurants.RestaurantList
            if x.LockerRoom.Location == button.position
        ][0]
        if matchingRestaurant.LockerRoom.Unlocked:
            activeGame.ButtonList.remove(button)


def SetupBackground(activeGame=Game.MasterGame) -> None:
    """Regenerates the Background Elements

    Args:
        activeGame (Game, optional): Current Game Class being used. Defaults to Game.MasterGame.
    """
    activeGame.BackgroundSpriteGroup.empty()
    AddTables(activeGame=activeGame)
    AddLockerRooms(activeGame=activeGame)
    UnlockLockerRooms(activeGame=activeGame)
