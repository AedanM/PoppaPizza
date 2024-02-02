"""Handler for User Clicks"""

from enum import Enum

from Classes import Game
from Definitions import AssetLibrary, CustomerDefs, LockerRooms
from Handlers import CustomerHandler as CH
from Handlers import WorkerHandler as WH
from Utilities import Utils


class ClickState(Enum):
    Neutral, ClickedWorker = range(2)


# pylint: disable=invalid-name, global-statement, W0602
GlobalClickState = ClickState.Neutral
GlobalTarget = None


def MouseHandler(mousePos) -> None:
    global GlobalClickState, GlobalTarget
    if GlobalClickState is ClickState.ClickedWorker:
        for lockerRoom in LockerRooms.LockerRooms:
            if (
                Utils.PositionInTolerance(
                    pos1=mousePos, pos2=lockerRoom.Location, tolerance=75
                )
                and lockerRoom.Unlocked
                and GlobalTarget.ImageType not in lockerRoom.WorkerImageTypes
            ):
                WH.GetChanged(ws=GlobalTarget, lockerRoom=lockerRoom)
        GlobalClickState = ClickState.Neutral
    elif GlobalClickState is ClickState.Neutral:
        for button in Game.MasterGame.ButtonList:
            if button.rect.collidepoint(mousePos[0], mousePos[1]):
                price = LockerRooms.UnlockLockerRoom(
                    currentCash=Game.MasterGame.UserInventory.Money,
                    position=button.position,
                )
                Game.MasterGame.UserInventory.PayMoney(amount=price)
                return
        for sprite in Game.MasterGame.CharSpriteGroup:
            if sprite.rect.collidepoint(mousePos[0], mousePos[1]):
                if sprite.ImageType in AssetLibrary.CustomerOutfits:
                    CustomerClickRoutine(target=sprite)
                elif sprite.ImageType in AssetLibrary.WorkerOutfits:
                    WorkerClickRoutine(target=sprite)
    else:
        GlobalClickState = ClickState.Neutral


def CustomerClickRoutine(target) -> None:
    global GlobalClickState

    if GlobalClickState is ClickState.Neutral:
        match target.DataObject.CurrentState:
            case CustomerDefs.CustomerStates.FirstInLine:
                CH.SitAtTable(target=target)
            case CustomerDefs.CustomerStates.WaitingForService:
                CH.AssignWorker(target=target)
            case CustomerDefs.CustomerStates.Queuing:
                pass


def WorkerClickRoutine(target) -> None:
    global GlobalClickState, GlobalTarget

    if GlobalClickState is ClickState.Neutral and not target.DataObject.IsAssigned:
        GlobalTarget = target
        GlobalClickState = ClickState.ClickedWorker
