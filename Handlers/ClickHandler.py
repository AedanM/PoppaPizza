"""Handler for User Clicks"""
from enum import Enum
import pygame
from Utilities import Utils
from Classes import Game, Sprite, People
from Handlers import CustomerHandler as CH, WorkerHandler as WH
from Definitions import LockerRooms


class ClickState(Enum):
    Neutral, ClickedCustomer, ClickedWorker = range(3)


GlobalClickState = ClickState.Neutral
GlobalTarget = None


def MouseHandler() -> None:
    global GlobalClickState, GlobalTarget
    mouseX, mouseY = pygame.mouse.get_pos()
    if GlobalClickState is ClickState.ClickedWorker:
        for imageType, location in LockerRooms.LockerRooms.items():
            if Utils.PositionInTolerance(
                pos1=(mouseX, mouseY), pos2=location, tolerance=75
            ):
                WH.GetChanged(ws=GlobalTarget, dest=location)
                GlobalClickState = ClickState.Neutral
    elif GlobalClickState is ClickState.Neutral:
        for sprite in Game.MasterGame.CharSpriteGroup:
            if sprite.rect.collidepoint(mouseX, mouseY):
                if sprite.ImageType == Sprite.ImageTypes.Customer:
                    CustomerClickRoutine(target=sprite)
                    GlobalClickState = ClickState.Neutral
                elif sprite.ImageType == Sprite.ImageTypes.Worker:
                    WorkerClickRoutine(target=sprite)
    else:
        GlobalClickState = ClickState.Neutral


def CustomerClickRoutine(target) -> None:
    global GlobalClickState
    customerObj = Game.MasterGame.MatchIdToPerson(
        inputId=target.CorrespondingID, targetOutput="customer"
    )
    if GlobalClickState is ClickState.Neutral:
        if (
            not customerObj.WorkerAssigned
            and customerObj.CurrentState is People.CustomerStates.Queuing
        ):
            CH.SitAtTable(target=target, customer=customerObj)
        elif customerObj.CurrentState == People.CustomerStates.WaitingForService:
            CH.AssignWorker(target=target, targetObj=customerObj)

    GlobalClickState = ClickState.ClickedCustomer


def WorkerClickRoutine(target) -> None:
    global GlobalClickState, GlobalTarget
    workerObj = Game.MasterGame.MatchIdToPerson(
        inputId=target.CorrespondingID, targetOutput="worker"
    )
    if GlobalClickState is ClickState.Neutral and not workerObj.IsAssigned:
        GlobalTarget = target
        GlobalClickState = ClickState.ClickedWorker
