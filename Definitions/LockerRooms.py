from Assets import AssetLibrary
from Definitions import DefinedLocations

LockerRooms = {
    AssetLibrary.ImageTypes.CoffeeLogo: DefinedLocations.LocationDefs.YellowLockerRoom,
    AssetLibrary.ImageTypes.CowboyLogo: DefinedLocations.LocationDefs.BlueLockerRoom,
    AssetLibrary.ImageTypes.LuauLogo: DefinedLocations.LocationDefs.PinkLockerRoom,
    AssetLibrary.ImageTypes.SuitLogo: DefinedLocations.LocationDefs.GreyLockerRoom,
}


LockerRoomPaths = {
    AssetLibrary.ImageTypes.CoffeeLogo: AssetLibrary.ImagePaths.CoffeePath,
    AssetLibrary.ImageTypes.CowboyLogo: AssetLibrary.ImagePaths.CowboyPath,
    AssetLibrary.ImageTypes.LuauLogo: AssetLibrary.ImagePaths.LuauPath,
    AssetLibrary.ImageTypes.SuitLogo: AssetLibrary.ImagePaths.SuitPath,
}
