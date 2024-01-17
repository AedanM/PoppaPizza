"""Class for People DataClasses"""
from dataclasses import dataclass
import random
from enum import Enum
import names
import Classes.Jobs as Jobs
import Classes.Game as Game
import Classes.Sprite as Sprite
import Classes.DefinedLocations as DL
import Utilities.Utils as utils

IDCOUNT = 0


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
            lName = names.get_first_name(gender="female")
            fName = names.get_last_name()
        else:
            lName, fName = ("A", "A")
        selfid = cls.GenerateID()
        return cls(FirstName=fName, LastName=lName, IdNum=selfid)

    @staticmethod
    def GenerateID():
        global IDCOUNT
        IDCOUNT += 1
        return IDCOUNT


@dataclass
class Worker(Person):
    BasePay: float = 1.0

    @classmethod
    def CreateWorker(cls):
        worker = cls.Create()
        workerSprite = Sprite.CharImageSprite(
            utils.PositionRandomVariance(
                DL.LocationDefs.KitchenLocation, (0.05, 0.75), Game.MasterGame.ScreenSize
            ),
            Sprite.iPaths.WorkerPath,
            worker.IdNum,
        )
        Game.MasterGame.CharSpriteGroup.add(workerSprite)
        Game.MasterGame.WorkerList.append(worker)
        return worker


class CustomerStates(Enum):
    Queuing, Waiting, BeingServed, Served, LeavingAngry, *_ = range(100)


@dataclass
class Customer(Person):
    DesiredJob: Jobs.Job = None
    WorkerAssigned: bool = False
    CurrentState: CustomerStates = None

    @classmethod
    def CreateCustomer(cls):
        cust = cls.Create()
        Game.MasterGame.JobList.append(Jobs.Job.SpawnJob())
        Game.MasterGame.JobList[-1].Assign(cust)
        customerSprite = Sprite.CharImageSprite(
            utils.PositionRandomVariance(
                DL.LocationDefs.CustomerEntrance, (0.05, 0.1), Game.MasterGame.ScreenSize
            ),
            Sprite.iPaths.CustomerPath,
            cust.IdNum,
        )
        Game.MasterGame.CharSpriteGroup.add(customerSprite)
        Game.MasterGame.CustomerList.append(cust)
        return cust


def UnitTest():
    currentJob = Jobs.Job.SpawnJob()
    w = Worker(IdNum=Worker.GenerateID(), FirstName="Anne", LastName="Smith")
    customer = Customer(IdNum=Customer.GenerateID(), FirstName="Anne", LastName="Smith")
    currentJob.Assign(customer)
    currentJob.Assign(w)


if __name__ == "__main__":
    UnitTest()
