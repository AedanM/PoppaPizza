"""Class for People DataClasses"""
from dataclasses import dataclass
from enum import Enum
import names
import random
from Classes import Jobs, Sprite, Game
from Definitions import DefinedLocations
import Utilities.Utils as utils
from Assets import AssetLibrary

IDCOUNT = 1


@dataclass
class Person:
    FirstName: str
    LastName: str
    IdNum: int
    Body: None = None
    IsAssigned: bool = False
    CurrentJobId: int = 0

    @classmethod
    def Create(cls):
        if utils.CheckInternet():
            fName = names.get_first_name(gender="female")
            lName = names.get_last_name()
        else:
            lName, fName = ("A", "A")
        selfid = cls.GenerateID()
        return cls(FirstName=fName, LastName=lName, IdNum=selfid)

    @staticmethod
    def GenerateID() -> int:
        # pylint: disable=global-statement
        global IDCOUNT
        IDCOUNT += 1
        return IDCOUNT


@dataclass
class Worker(Person):
    BasePay: float = 1.0

    @classmethod
    def CreateWorker(
        cls,
        startLocation=DefinedLocations.LocationDefs.KitchenLocation,
        activeGame=Game.MasterGame,
    ) -> "Worker":
        worker = cls.Create()
        workerSprite = Sprite.CharImageSprite(
            position=utils.PositionRandomVariance(
                position=startLocation,
                percentVarianceTuple=(0.05, 0.5),
                screenSize=activeGame.ScreenSize,
            ),
            path=AssetLibrary.ImagePath.WorkerPath,
            objID=worker.IdNum,
        )
        worker.BasePay = random.uniform(0.25, 5.0)
        activeGame.CharSpriteGroup.add(workerSprite)
        activeGame.WorkerList.append(worker)
        return worker, workerSprite


class CustomerStates(Enum):
    (
        Null,
        Queuing,
        Seated,
        WaitingForService,
        BeingServed,
        Served,
        LeavingAngry,
        *_,
    ) = range(100)


@dataclass
class Customer(Person):
    DesiredJob: Jobs.Job = None
    WorkerAssigned: bool = False
    CurrentState: CustomerStates = CustomerStates.Null

    @classmethod
    def CreateCustomer(
        cls,
        startLocation=DefinedLocations.LocationDefs.CustomerEntrance,
        activeGame=Game.MasterGame,
    ) -> "Customer":
        cust = cls.Create()
        activeGame.JobList.append(Jobs.Job.SpawnJob())
        activeGame.JobList[-1].Assign(cust)
        customerSprite = Sprite.CharImageSprite(
            position=utils.PositionRandomVariance(
                position=startLocation,
                percentVarianceTuple=(0.0005, 0.1),
                screenSize=activeGame.ScreenSize,
            ),
            path=AssetLibrary.ImagePath.CustomerPath,
            objID=cust.IdNum,
        )
        activeGame.CharSpriteGroup.add(customerSprite)
        activeGame.CustomerList.append(cust)
        return cust, customerSprite
