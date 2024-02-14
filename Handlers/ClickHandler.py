"""Handler for User Clicks"""

from enum import Enum

from Classes import GameBase, MiniGames
from Definitions import AssetLibrary, CustomerDefs, Restaurants
from Engine import Utils
from Handlers import CustomerHandler, ShopHandler, WorkerHandler


class ClickState(Enum):
    """Enumeration for Click States"""

    Neutral, ClickedWorker = range(2)


# pylint: disable=invalid-name, global-statement, W0602
GlobalClickState = ClickState.Neutral
GlobalTarget = None


def TriviaMouseHandler(mousePos) -> None:
    clickedText = ""
    for button in GameBase.MasterGame.MiniGame.MasterSpriteGroup:
        if button.rect.collidepoint(mousePos[0], mousePos[1]):
            clickedText = (
                [
                    x.Text
                    for x in GameBase.MasterGame.MiniGame.DisplayedText.values()
                    if x.Center == button.rect.center
                ]
            )[0]
    GameBase.MasterGame.MiniGame.UpdateStateMachine(inputStr=clickedText)


def MainMouseHandler(mousePos, lClick) -> None:
    """Handler for mouse clicks

    Args-
        mousePos (tuple): Position of Mouse Click
        lClick (bool): Left or Right Mouse Button, True is Left
    """
    global GlobalClickState, GlobalTarget
    if GlobalClickState is ClickState.ClickedWorker:
        for restaurant in Restaurants.RestaurantList:
            lockerRoom = restaurant.LockerRoom
            if (
                Utils.PositionInTolerance(
                    pos1=mousePos, pos2=lockerRoom.Location, tolerance=75
                )
                and lockerRoom.Unlocked
                and GlobalTarget.ImageType not in restaurant.WorkerImageTypes #type: ignore
                and restaurant.WorkerImageTypes
            ):
                WorkerHandler.GetChanged(
                    workerSprite=GlobalTarget, restaurant=restaurant
                )
        GlobalClickState = ClickState.Neutral
    elif GlobalClickState is ClickState.Neutral:
        for button in GameBase.MasterGame.ButtonList:
            if button.rect.collidepoint(mousePos[0], mousePos[1]):
                ShopHandler.BuyLockerRoom(position=button.position)
                return
        for sprite in GameBase.MasterGame.CharSpriteGroup:
            if sprite.rect.collidepoint(mousePos[0], mousePos[1]):
                if sprite.ImageType in AssetLibrary.CustomerOutfits:
                    CustomerClickRoutine(target=sprite, leftClick=lClick)
                elif sprite.ImageType in AssetLibrary.WorkerOutfits:
                    WorkerClickRoutine(target=sprite)
    else:
        GlobalClickState = ClickState.Neutral


def CustomerClickRoutine(target, leftClick) -> None:
    """Handler for Customer Clicks

    Args-
        target (CharImageSprite): Clicked Sprite
        leftClick (bool): Left or Right Mouse Button, True is Left
    """
    global GlobalClickState
    # TODO - Stop customers being served in queue
    if GlobalClickState is ClickState.Neutral:
        match target.DataObject.CurrentState:
            case CustomerDefs.CustomerStates.FirstInLine:
                if leftClick:
                    CustomerHandler.SitAtTable(target=target)
                else:
                    CustomerHandler.GetUpAndGo(spriteImg=target)
            case CustomerDefs.CustomerStates.WaitingForService:
                CustomerHandler.AssignWorker(target=target)
            case CustomerDefs.CustomerStates.Queuing:
                pass


def WorkerClickRoutine(target) -> None:
    """Handler for Worker Clicks

    Args-
        target (CharImageSprite): Sprite Clicked
    """
    global GlobalClickState, GlobalTarget

    if GlobalClickState is ClickState.Neutral and not target.DataObject.IsAssigned:
        GlobalTarget = target
        GlobalClickState = ClickState.ClickedWorker
