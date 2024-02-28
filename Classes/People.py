"""Class for People DataClasses"""

import random
from dataclasses import dataclass

from Classes import Jobs, Sprite
from Definitions import AssetLibrary, CustomerDefs
from Definitions.DefinedLocations import LocationDefs
from Engine import Person, Utils

IDCOUNT = 1


@dataclass
class Worker(Person.Person):
    """Data class for Workers, inherits from Person Class"""

    BasePay: float = 1.0

    @classmethod
    def CreateWorker(
        cls,
        activeGame,
        startLocation=LocationDefs.WorkerSpawn,
    ) -> tuple:
        """Create and Spawn in Worker and Worker Sprite

        Args-
            startLocation (tuple, optional): Spawn Location. Defaults to DefinedLocations.LocationDefs.KitchenLocation.
            activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.

        Returns-
            tuple: (Dataclass, Image Classs)
        """
        worker = cls.Create()
        workerSprite = Sprite.CharImageSprite(
            center=Utils.OffsetTuple(inputTuple=startLocation, offset=(0, random.randint(-500, 0))),
            path=AssetLibrary.ImagePath.WorkerSuitPath,
            objID=worker.IdNum,
        )
        worker.BasePay = random.uniform(0.25, 5.0)
        activeGame.CharSpriteGroup.add(workerSprite)
        activeGame.WorkerList.append(worker)
        return worker, workerSprite

    def __hash__(self) -> int:
        return super().__hash__()


@dataclass
class Customer(Person.Person):
    """Data Class for Customers, inherits from Person Class"""

    DesiredJob: Jobs.Job = None  # type: ignore
    WorkerAssigned: bool = False
    CurrentState: CustomerDefs.CustomerStates = CustomerDefs.CustomerStates.Null

    @classmethod
    def CreateCustomer(
        cls,
        activeGame,
        startLocation=LocationDefs.CustomerSpawn,
        imageType=AssetLibrary.ImageTypes.CustomerSuit,
    ) -> tuple:
        """Creates a Customer nad Customer Sprite

        Args-
            startLocation (tuple, optional): Spawn Location. Defaults to DefinedLocations.LocationDefs.CustomerEntrance.
            activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.
            imageType (AssetLibrary.ImageType, optional): Type of Image to Load onto Customer. Defaults to AssetLibrary.ImageTypes.CustomerSuit.

        Returns-
            tuple: (Dataclass, Image Class)
        """
        cust = cls.Create()
        activeGame.JobList.append(Jobs.Job.SpawnJob())
        activeGame.JobList[-1].Assign(cust)
        customerSprite = Sprite.CharImageSprite(
            position=Utils.PositionRandomVariance(
                position=startLocation,
                percentVariance=(0.0005, 0.1),
                screenSize=activeGame.ScreenSize,
            ),
            path=AssetLibrary.PathLookup(imageType),
            objID=cust.IdNum,
        )
        activeGame.CharSpriteGroup.add(customerSprite)
        activeGame.CustomerList.append(cust)
        return cust, customerSprite

    def __hash__(self) -> int:
        return super().__hash__()
