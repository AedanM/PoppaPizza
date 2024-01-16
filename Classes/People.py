from dataclasses import dataclass
import pygame_menu
import names
import random
from enum import Enum
import Classes.Jobs as Jobs
import Classes.Game as Game
import Classes.Sprite as Sprite
import Classes.utils as utils
import Classes.DefinedLocations as DL


IDCount = 0


@dataclass
class Person:
    firstName: str
    lastName: str
    idNum: int
    body: None = None
    isAssigned: bool = False
    currentJobId: int = 0

    @classmethod
    def Create(self):
        if utils.checkInternet:
            lName = names.get_first_name(gender="female")
            fName = names.get_last_name()
        else:
            lName, fName = ("A", "A")
        selfid = self.GenerateID()
        return self(firstName=fName, lastName=lName, idNum=selfid)

    @staticmethod
    def GenerateID():
        global IDCount
        IDCount += 1
        return IDCount


@dataclass
class Worker(Person):
    basePay: float = 1.0

    @classmethod
    def CreateWorker(self):
        worker = self.Create()
        workerSprite = Sprite.CharImageSprite(
            utils.PositionRandomVariance(DL.LocationDefs.KitchenLocation, (0.1, 1)),
            Sprite.iPaths.workerPath,
            worker.idNum,
        )
        Game.MasterGame.CharSpriteGroup.add(workerSprite)
        Game.MasterGame.WorkerList.append(worker)
        return worker


class CustomerStates(Enum):
    Queuing, Waiting, BeingServed, Served, LeavingAngry, *_ = range(100)


@dataclass
class Customer(Person):
    desiredJob: Jobs.Job = None
    workerAssigned: bool = False

    @classmethod
    def CreateCustomer(self):
        customer = self.Create()
        Game.MasterGame.JobList.append(Jobs.Job.SpawnJob())
        Game.MasterGame.JobList[-1].Assign(customer)
        customerSprite = Sprite.CharImageSprite(
            utils.PositionRandomVariance(DL.LocationDefs.CustomerEntrance, (0.1, 1)),
            Sprite.iPaths.customerPath,
            customer.idNum,
        )
        Game.MasterGame.CharSpriteGroup.add(customerSprite)
        Game.MasterGame.CustomerList.append(customer)
        return customer


if __name__ == "__main__":
    currentJob = Jobs.Job.SpawnJob()
    worker = Worker(idNum=Worker.GenerateID(), firstName="Anne", lastName="Smith")
    customer = Customer(idNum=Customer.GenerateID(), firstName="Anne", lastName="Smith")
    currentJob.Assign(customer)
    currentJob.Assign(worker)
    print(worker)
    print(customer)
