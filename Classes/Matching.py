"""Matching Functions for Person Objects"""

from Definitions import AssetLibrary
from Definitions.Restaurants import Restaurant, RestaurantList



def MatchIdToPerson(activeGame, inputId, targetOutput="all") -> dict:
    """Match an id to corresponding people and sprites

    Args:
        activeGame (Game): Current Game
        inputId (int): ID of object to find
        targetOutput (str, optional): Defines what the requested reponse is. Defaults to "all".

    Returns:
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

    Args:
        activeGame (Game): Current Game
        targetSprite (CharImageSprite): Sprite to delete
    """
    responseDict = MatchIdToPerson(
        activeGame=activeGame, inputId=targetSprite.CorrespondingID
    )
    if "customer" in responseDict:
        activeGame.CustomerList.remove(responseDict["customer"])
    elif "worker" in responseDict:
        activeGame.WorkerList.remove(responseDict["worker"])
    targetSprite.kill()


def RemoveButtonFromLocation(activeGame, location) -> None:
    """Remove a given button

    Args:
        activeGame (Game): Current Game
        location (tuple): Location of button to be destroyed
    """
    corrButton = [x for x in activeGame.ButtonList if x.position == location]
    for button in corrButton:
        activeGame.ButtonList.remove(button)


def FindRestaurant(imageType) -> Restaurant | None:
    """Matches image type to Restaurant

    Args:
        imageType (Image Type): Input Type

    Returns:
        Restaurant | None: Matched Restaurant Object
    """
    potentialList = [None]
    if imageType in AssetLibrary.WorkerOutfits:
        potentialList = [x for x in RestaurantList if imageType in x.WorkerImageTypes]
    elif imageType in AssetLibrary.CustomerOutfits:
        potentialList = [x for x in RestaurantList if imageType in x.CustomerImageTypes]
    return potentialList[0]


def CostumeMatch(workerSprite, customerSprite) -> bool:
    """Checks if customer and worker match outfits

    Args:
        workerSprite (CharImageSprite): Active Worker
        customerSprite (CharImageSprite): Active Customer

    Returns:
        bool: Do they belong to same Restaurants
    """
    if workerSprite is not None:
        desiredRest = FindRestaurant(imageType=customerSprite.ImageType)
        return workerSprite.ImageType in desiredRest.WorkerImageTypes

    return False
