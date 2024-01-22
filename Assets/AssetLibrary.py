from dataclasses import dataclass
from enum import Enum


@dataclass
class ImagePaths:
    AssetFolder = r"Assets"
    WorkerPath = AssetFolder + r"\waiter.png"
    CustomerPath = AssetFolder + r"\person.png"
    TablePath = AssetFolder + r"\table.png"
    BackgroundPath = AssetFolder + r"\background.png"


class ImageTypes(Enum):
    Null, Worker, Customer, Table = range(4)


ImagePath = ImagePaths()


PathToTypeDict = {
    ImagePath.WorkerPath: ImageTypes.Worker,
    ImagePath.CustomerPath: ImageTypes.Customer,
    ImagePath.TablePath: ImageTypes.Table,
}
