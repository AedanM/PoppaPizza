from dataclasses import dataclass
from enum import Enum


@dataclass
class ImagePaths:
    AssetFolder = r"Assets"
    WorkerPath = AssetFolder + r"\waiter.png"
    CustomerPath = AssetFolder + r"\person.png"
    TablePath = AssetFolder + r"\table.png"
    BackgroundPath = AssetFolder + r"\background.png"
    CoffeePath = AssetFolder + r"\coffee.png"
    CowboyPath = AssetFolder + r"\cowboySaloon.png"
    LuauPath = AssetFolder + r"\Luau.png"
    SuitPath = AssetFolder + r"\suit.png"


class ImageTypes(Enum):
    Null, Worker, Customer, Table, CoffeeLogo, CowboyLogo, LuauLogo, SuitLogo = range(8)


ImagePath = ImagePaths()


PathToTypeDict = {
    ImagePath.WorkerPath: ImageTypes.Worker,
    ImagePath.CustomerPath: ImageTypes.Customer,
    ImagePath.TablePath: ImageTypes.Table,
    ImagePath.CoffeePath: ImageTypes.CoffeeLogo,
    ImagePath.CowboyPath: ImageTypes.CowboyLogo,
    ImagePath.LuauPath: ImageTypes.LuauLogo,
    ImagePath.SuitPath: ImageTypes.SuitLogo,
}
