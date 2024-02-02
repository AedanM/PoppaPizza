"""Matching Functions for Person Objects"""

from Definitions import Restaurants


def MatchIdToPerson(activeGame, inputId, targetOutput="all") -> dict:
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
    responseDict = MatchIdToPerson(
        activeGame=activeGame, inputId=targetSprite.CorrespondingID
    )
    if "customer" in responseDict:
        activeGame.CustomerList.remove(responseDict["customer"])
    elif "worker" in responseDict:
        activeGame.WorkerList.remove(responseDict["worker"])
    targetSprite.kill()


def RemoveButtonFromLocation(activeGame, location) -> None:
    corrButton = [x for x in activeGame.ButtonList if x.position == location]
    for button in corrButton:
        activeGame.ButtonList.remove(button)


def CostumeMatch(workerSprite, customerSprite) -> bool:
    if workerSprite is not None:
        desiredRest = Restaurants.FindRestaurant(imageType=customerSprite.ImageType)
        return workerSprite.ImageType in desiredRest.WorkerImageTypes

    return False
