"""Populate Background with Elements"""

from Classes import Game, Matching, Sprite
from Definitions import AssetLibrary, ColorTools, DefinedLocations, Restaurants
from Utilities import Utils

# TODO - Stop Recalcing Tables


def AddTables(activeGame=Game.MasterGame) -> None:
    """Places tables as they are unlocked

    Args:
        activeGame (Game, optional): Current Game being used. Defaults to Game.MasterGame.
    """
    for location in DefinedLocations.SeatingPlan.GenerateTablePlaces():
        table = Sprite.BackgroundElementSprite(
            position=location,
            path=AssetLibrary.ImagePath.TablePath,
            maxSize=60,
            offset=(-75, 25),
        )
        table.Collision = False
        activeGame.BackgroundSpriteGroup.add(table)


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
        logo = None
        if restaurant.LogoPath:
            logo = Sprite.BackgroundElementSprite(
                position=lockerRoom.Location,
                path=path,
                maxSize=maxSize,
                offset=offset,
            )

        rectObj = Sprite.RectangleObject(
            position=lockerRoom.Location, color=color, size=restaurant.Size
        )

        activeGame.ForegroundSpriteGroup.add(rectObj)
        if logo:
            activeGame.ForegroundSpriteGroup.add(logo)
        if not lockerRoom.Unlocked:
            Sprite.ButtonObject.AddButton(
                location=lockerRoom.Location,
                text="Buy Me",
                backColor=ColorTools.CautionTapeYellow,
                color=ColorTools.Black,
                enabled=lockerRoom.Price < activeGame.UserInventory.Money,
                activeGame=Game.MasterGame,
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
