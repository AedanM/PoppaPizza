"""Class for People DataClasses"""

import random
from dataclasses import dataclass

from Classes import GameBase, Jobs, Sprite
from Definitions import AssetLibrary, CustomerDefs, DefinedLocations
from Engine import Person, Utils

IDCOUNT = 1


@dataclass
class Worker(Person.Person):
    """Data class for Workers, inherits from Person Class"""

    BasePay: float = 1.0

    @classmethod
    def CreateWorker(
        cls,
        startLocation=DefinedLocations.LocationDefs.WorkerSpawn,
        activeGame=GameBase.MasterGame,
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
            center=Utils.OffsetTuple(
                inputTuple=startLocation, offset=(0, random.randint(-500, 0))
            ),
            path=AssetLibrary.ImagePath.WorkerSuitPath,
            objID=worker.IdNum,
        )
        worker.BasePay = random.uniform(0.25, 5.0)
        activeGame.CharSpriteGroup.add(workerSprite)
        activeGame.WorkerList.append(worker)
        return worker, workerSprite


@dataclass
class Customer(Person.Person):
    """Data Class for Customers, inherits from Person Class"""

    DesiredJob: Jobs.Job = None
    WorkerAssigned: bool = False
    CurrentState: CustomerDefs.CustomerStates = CustomerDefs.CustomerStates.Null

    @classmethod
    def CreateCustomer(
        cls,
        startLocation=DefinedLocations.LocationDefs.CustomerSpawn,
        activeGame=GameBase.MasterGame,
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
                percentVarianceTuple=(0.0005, 0.1),
                screenSize=activeGame.ScreenSize,
            ),
            path=AssetLibrary.PathLookup(imageType),
            objID=cust.IdNum,
        )
        activeGame.CharSpriteGroup.add(customerSprite)
        activeGame.CustomerList.append(cust)
        return cust, customerSprite
