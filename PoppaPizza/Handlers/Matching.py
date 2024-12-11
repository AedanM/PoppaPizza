"""Matching Functions for Person Objects"""

from typing import Any

from Definitions import AssetLibrary, Restaurants
from Engine import Person
from Handlers import WorkerHandler


def MatchIdToPerson(activeGame, inputId, targetOutput="all") -> dict[str, Any] | None:
    """Match an id to corresponding people and sprites

    Args-
        activeGame (Game): Current Game
        inputId (int): ID of object to find
        targetOutput (str, optional): Defines what the requested reponse is. Defaults to "all".

    Returns-
        dict: _description_
    """
    output = {}
    if inputId != 0:
        for sprite in activeGame.CharSpriteGroup:
            if sprite.CorrespondingID == inputId:
                output["sprite"] = sprite
        for worker in activeGame.WorkerList:
            if worker.IdNum == inputId:
                output["worker"] = worker
        for customer in activeGame.CustomerList:
            if customer.IdNum == inputId:
                output["customer"] = customer
        return output if targetOutput == "all" else output[targetOutput]
    return None


def RemoveObjFromSprite(activeGame, targetSprite) -> None:
    """Delete data class and kill sprite

    Args-
        activeGame (Game): Current Game
        targetSprite (CharImageSprite): Sprite to delete
    """
    responseDict = MatchIdToPerson(activeGame=activeGame, inputId=targetSprite.CorrespondingID)

    if responseDict is None:
        pass
    else:
        responseDict.pop("sprite")
        personObj = list(responseDict.values())[0]
        Person.FIRSTNAMES.discard(personObj.FirstName)
        Person.LASTNAMES.discard(personObj.LastName)
        if "customer" in responseDict:
            activeGame.CustomerList.remove(responseDict["customer"])
        elif "worker" in responseDict:
            activeGame.WorkerList.remove(responseDict["worker"])
    targetSprite.kill()


def RemoveButtonFromLocation(activeGame, location) -> None:
    """Remove a given button

    Args-
        activeGame (Game): Current Game
        location (tuple): Location of button to be destroyed
    """
    corrButton = [x for x in activeGame.ButtonList if x.position == location]
    for button in corrButton:
        activeGame.ButtonList.remove(button)


def FindRestaurant(imageType) -> Restaurants.Restaurant | None:
    """Matches image type to Restaurant

    Args-
        imageType (Image Type): Input Type

    Returns-
        Restaurant | None: Matched Restaurant Object
    """
    potentialList = [None]
    if imageType in AssetLibrary.WorkerOutfits:
        potentialList = [x for x in Restaurants.RestaurantList if imageType in x.WorkerImageTypes]
    elif imageType in AssetLibrary.CustomerOutfits:
        potentialList = [x for x in Restaurants.RestaurantList if imageType in x.CustomerImageTypes]
    return potentialList[0]


def CostumeMatch(workerSprite, customerSprite) -> bool:
    """Checks if customer and worker match outfits

    Args-
        workerSprite (CharImageSprite): Active Worker
        customerSprite (CharImageSprite): Active Customer

    Returns-
        bool: Do they belong to same Restaurants
    """
    if workerSprite is not None:
        desiredRest = FindRestaurant(imageType=customerSprite.ImageType)
        return workerSprite.ImageType in desiredRest.WorkerImageTypes  # type: ignore

    return False


def ResetSprites(activeGame) -> None:
    """Reset all Sprites

        Kill Customer Sprites
        Reset Workers to Kitchen

    Args-
        activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.
    """
    for sprite in activeGame.CharSpriteGroup:
        if sprite.ImageType in AssetLibrary.CustomerOutfits:
            RemoveObjFromSprite(activeGame=activeGame, targetSprite=sprite)
        elif sprite.ImageType in AssetLibrary.WorkerOutfits:
            WorkerHandler.DailyReset(sprite=sprite)
