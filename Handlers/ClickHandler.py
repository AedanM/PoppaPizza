"""Handler for User Clicks"""

from enum import Enum

from Definitions import AssetLibrary, Restaurants
from Definitions.CustomerDefs import CustomerStates
from Handlers import CustomerHandler, ShopHandler, WorkerHandler


class ClickState(Enum):
    """Enumeration for Click States"""

    Neutral, ClickedWorker = range(2)


# pylint: disable=invalid-name, global-statement, W0602
GlobalClickState = ClickState.Neutral
GlobalTarget = None


def TriviaMouseHandler(mousePos, activeGame) -> None:
    clickedText = ""
    for button in activeGame.MiniGame.MasterSpriteGroup:
        if button.rect.collidepoint(mousePos[0], mousePos[1]):
            clickedText = (
                [
                    x.Text
                    for x in activeGame.MiniGame.DisplayedText.values()
                    if x.Center == button.rect.center
                ]
            )[0]
    activeGame.MiniGame.UpdateStateMachine(inputStr=clickedText)


def MainMouseHandler(mousePos, isLeftClick, activeGame) -> None:
    """Handler for mouse clicks

    Args-
        mousePos (tuple): Position of Mouse Click
        lClick (bool): Left or Right Mouse Button, True is Left
    """
    global GlobalClickState, GlobalTarget
    entryState = GlobalClickState
    match GlobalClickState:
        case ClickState.ClickedWorker:
            for restaurant in Restaurants.RestaurantList:
                if restaurant.RequiresChange(mousePos=mousePos, target=GlobalTarget):
                    WorkerHandler.GetChanged(
                        workerSprite=GlobalTarget, restaurant=restaurant, activeGame=activeGame
                    )
        case ClickState.Neutral:
            for button in activeGame.ButtonList:
                if button.rect.collidepoint(mousePos[0], mousePos[1]) and isLeftClick:
                    ShopHandler.BuyLockerRoom(position=button.position, activeGame=activeGame)
                    return
            for sprite in activeGame.CharSpriteGroup:
                if sprite.rect.collidepoint(mousePos[0], mousePos[1]):
                    if sprite.ImageType in AssetLibrary.CustomerOutfits:
                        CustomerClickRoutine(
                            target=sprite, leftClick=isLeftClick, activeGame=activeGame
                        )
                    elif sprite.ImageType in AssetLibrary.WorkerOutfits and isLeftClick:
                        WorkerClickRoutine(target=sprite)

        case other:
            pass
    if entryState is GlobalClickState:
        GlobalClickState = ClickState.Neutral


def CustomerClickRoutine(target, leftClick, activeGame) -> None:
    """Handler for Customer Clicks

    Args-
        target (CharImageSprite): Clicked Sprite
        leftClick (bool): Left or Right Mouse Button, True is Left
    """
    global GlobalClickState
    # BUG - Stop customers being served in queue
    if GlobalClickState is ClickState.Neutral:
        match target.DataObject.CurrentState:
            case CustomerStates.FirstInLine:
                if leftClick:
                    CustomerHandler.SitAtTable(target=target, activeGame=activeGame)
                else:
                    CustomerHandler.GetUpAndGo(spriteImg=target, activeGame=activeGame)
            case CustomerStates.WaitingForService:
                CustomerHandler.AssignWorker(target=target, activeGame=activeGame)
            case CustomerStates.Queuing:
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
