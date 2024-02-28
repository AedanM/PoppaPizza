"""Populate Background with Elements"""

from Classes import Sprite
from Definitions import AssetLibrary, ColorDefines, Restaurants
from Definitions.DefinedLocations import LocationDefs, SeatingPlan
from Engine import SpriteObjects, Utils
from Handlers import Matching

# TODO - Stop Recalcing Tables


def AddTables(activeGame) -> None:
    """Places tables as they are unlocked

    Args-
        activeGame (Game, optional): Current Game being used. Defaults to Game.MasterGame.
    """
    for location in SeatingPlan.GenerateTablePlaces():
        table = Sprite.BackgroundElementSprite(
            position=location,
            path=AssetLibrary.ImagePath.TablePath,
            maxSize=60,
            offset=(-75, 25),
        )
        table.Collision = False
        activeGame.BackgroundSpriteGroup.add(table)


def AddLockerRooms(activeGame) -> None:
    """Generate and Add Locker Rooms based on locked status

    Args-
        activeGame (Game, optional): Current Game Class being used. Defaults to Game.MasterGame.
    """
    for restaurant in Restaurants.RestaurantList:
        lockerRoom = restaurant.LockerRoom

        Matching.RemoveButtonFromLocation(activeGame=activeGame, location=lockerRoom.Location)

        if lockerRoom.Unlocked:
            color = lockerRoom.Color
            path = restaurant.LogoPath
            maxSize = 100
            offset = Utils.ScaleToSize(value=(-50, -50), newSize=LocationDefs.ScreenSize)
        else:
            path = AssetLibrary.ImagePath.LogoLockedPath
            color = ColorDefines.Grey
            maxSize = 180
            offset = Utils.ScaleToSize(value=(-90, -50), newSize=LocationDefs.ScreenSize)
        logo = None
        if restaurant.LogoPath:
            logo = Sprite.BackgroundElementSprite(
                position=lockerRoom.Location,
                path=path,
                maxSize=maxSize,
                offset=offset,
            )

        rectObj = SpriteObjects.RectangleObject(
            position=lockerRoom.Location, color=color, size=restaurant.Size
        )
        activeGame.ForegroundSpriteGroup.add(rectObj)
        if logo:
            activeGame.ForegroundSpriteGroup.add(logo)
        if not lockerRoom.Unlocked:
            Sprite.ButtonObject.AddButton(
                location=lockerRoom.Location,
                text="Buy Me",
                backColor=ColorDefines.CautionTapeYellow,
                color=ColorDefines.Black,
                enabled=lockerRoom.Price < activeGame.UserInventory.Money,
                activeGame=activeGame,
            )


def UnlockLockerRooms(activeGame) -> None:
    """Updates the locker rooms to unlock the purchased rooms

    Args-
        activeGame (Game): Current Game Class being used
    """
    for button in activeGame.ButtonList:
        matchingRestaurant = [
            x for x in Restaurants.RestaurantList if x.LockerRoom.Location == button.position
        ][0]
        if matchingRestaurant.LockerRoom.Unlocked:
            activeGame.ButtonList.remove(button)


