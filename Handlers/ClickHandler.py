"""Handler for User Clicks"""
from enum import Enum
from Utilities import Utils
from Classes import Game
from Handlers import CustomerHandler as CH, WorkerHandler as WH
from Definitions import CustomerDefs, LockerRooms, AssetLibrary


class ClickState(Enum):
    Neutral, ClickedCustomer, ClickedWorker = range(3)


# pylint: disable=invalid-name, global-statement, W0602
GlobalClickState = ClickState.Neutral
GlobalTarget = None


def MouseHandler(event) -> None:
    global GlobalClickState, GlobalTarget
    if GlobalClickState is ClickState.ClickedWorker:
        for location in LockerRooms.LockerRooms.values():
            if Utils.PositionInTolerance(pos1=event.pos, pos2=location, tolerance=75):
                WH.GetChanged(ws=GlobalTarget, dest=location)
        GlobalClickState = ClickState.Neutral
    elif GlobalClickState is ClickState.Neutral:
        for sprite in Game.MasterGame.CharSpriteGroup:
            if sprite.rect.collidepoint(event.pos[0], event.pos[1]):
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
