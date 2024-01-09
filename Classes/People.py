from dataclasses import dataclass
import Classes.Job as jc
import pygame_menu
import programUtils as util
import names

WorkerIDCount = 0
CustomerIDCount = 0


@dataclass
class Person():
    firstName: str
    lastName: str
    idNum: int
    body: None = None
    isAssigned: bool = False
    currentJobId: int = 0
    @classmethod
    def Create(self):
        if(util.checkInternet):
            lName = names.get_first_name(gender="female")
            fName = names.get_last_name()
        else:
            lName,fName = ('A','A')
        selfid = self.GenerateID()
        return self(firstName=fName, lastName=lName, idNum=selfid)


@dataclass
class Worker(Person):
    basePay: float = 1.0

    @staticmethod
    def GenerateID():
        global WorkerIDCount
        WorkerIDCount += 1
        return WorkerIDCount


@dataclass
class Customer(Person):
    desiredJob: jc.Job = None

    @staticmethod
    def GenerateID():
        global CustomerIDCount
        CustomerIDCount += 1
        return CustomerIDCount


if __name__ == "__main__":
    currentJob = jc.Job.SpawnJob()
    worker = Worker(idNum=Worker.GenerateID(), firstName="Anne", lastName="Smith")
    customer = Customer(idNum=Customer.GenerateID(), firstName="Anne", lastName="Smith")
    currentJob.Assign(customer)
    currentJob.Assign(worker)
    print(worker)
    print(customer)
