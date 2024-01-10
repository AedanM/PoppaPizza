from dataclasses import dataclass
import pygame_menu
import programUtils as util
import names
import random
import Classes.Jobs as Jobs
import Classes.Game as Game
import Classes.Sprite as Sprite
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
        if util.checkInternet:
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

    


@dataclass
class Customer(Person):
    desiredJob: Jobs.Job = None

    @classmethod
    def CreateCustomer(self):
        customer = self.Create()
        Game.MasterGame.JobList.append(Jobs.Job.SpawnJob())
        Game.MasterGame.JobList[-1].Assign(customer)
        customerSprite = Sprite.CharImageSprite(
        (800, random.randint(1, 12) * 50), Sprite.iPaths.customerPath, customer.idNum
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
