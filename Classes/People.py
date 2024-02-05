"""Class for People DataClasses"""

import random
from dataclasses import dataclass

import names

import Utilities.Utils as utils
from Classes import Game, Jobs, Sprite
from Definitions import AssetLibrary, CustomerDefs, DefinedLocations

IDCOUNT = 1


@dataclass
class Person:
    FirstName: str
    LastName: str
    IdNum: int
    Body: None = None
    IsAssigned: bool = False

    @classmethod
    def Create(cls):
        fName = names.get_first_name(gender="female")
        lName = names.get_last_name()
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
    ) -> tuple:
        worker = cls.Create()
        workerSprite = Sprite.CharImageSprite(
            position=utils.PositionRandomVariance(
                position=startLocation,
                percentVarianceTuple=(0.05, 0.5),
                screenSize=activeGame.ScreenSize,
            ),
            path=AssetLibrary.ImagePath.WorkerSuitPath,
            objID=worker.IdNum,
        )
        worker.BasePay = random.uniform(0.25, 5.0)
        activeGame.CharSpriteGroup.add(workerSprite)
        activeGame.WorkerList.append(worker)
        return worker, workerSprite


@dataclass
class Customer(Person):
    DesiredJob: Jobs.Job = None
    WorkerAssigned: bool = False
    CurrentState: CustomerDefs.CustomerStates = CustomerDefs.CustomerStates.Null

    @classmethod
    def CreateCustomer(
        cls,
        startLocation=DefinedLocations.LocationDefs.CustomerEntrance,
        activeGame=Game.MasterGame,
        imageType=AssetLibrary.ImageTypes.CustomerSuit,
    ) -> tuple:
        cust = cls.Create()
        activeGame.JobList.append(Jobs.Job.SpawnJob())
        activeGame.JobList[-1].Assign(cust)
        customerSprite = Sprite.CharImageSprite(
            position=utils.PositionRandomVariance(
                position=startLocation,
                percentVarianceTuple=(0.0005, 0.1),
                screenSize=activeGame.ScreenSize,
            ),
            path=AssetLibrary.PathLookup(imageType),
            objID=cust.IdNum,
        )
        activeGame.CharSpriteGroup.add(customerSprite)
        activeGame.CustomerList.append(cust)
        return cust, customerSprite
