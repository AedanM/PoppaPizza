from Definitions import DefinedLocations, ColorTools, AssetLibrary

LockerRooms = {
    AssetLibrary.ImageTypes.CoffeeLogo: DefinedLocations.LocationDefs.YellowLockerRoom,
    AssetLibrary.ImageTypes.CowboyLogo: DefinedLocations.LocationDefs.BlueLockerRoom,
    AssetLibrary.ImageTypes.LuauLogo: DefinedLocations.LocationDefs.PinkLockerRoom,
    AssetLibrary.ImageTypes.SuitLogo: DefinedLocations.LocationDefs.GreyLockerRoom,
    AssetLibrary.ImageTypes.SafariLogo: DefinedLocations.LocationDefs.GreenLockerRoom,
}


LockerRoomPaths = {
    AssetLibrary.ImageTypes.CoffeeLogo: AssetLibrary.ImagePaths.CoffeePath,
    AssetLibrary.ImageTypes.CowboyLogo: AssetLibrary.ImagePaths.CowboyPath,
    AssetLibrary.ImageTypes.LuauLogo: AssetLibrary.ImagePaths.LuauPath,
    AssetLibrary.ImageTypes.SuitLogo: AssetLibrary.ImagePaths.SuitPath,
    AssetLibrary.ImageTypes.SafariLogo: AssetLibrary.ImagePaths.SafariPath,
}

LockerRoomColors = {
    DefinedLocations.LocationDefs.YellowLockerRoom: ColorTools.Yellow,
    DefinedLocations.LocationDefs.BlueLockerRoom: ColorTools.Blue,
    DefinedLocations.LocationDefs.GreenLockerRoom: ColorTools.Green,
    DefinedLocations.LocationDefs.PinkLockerRoom: ColorTools.Pink,
    DefinedLocations.LocationDefs.GreyLockerRoom: ColorTools.Grey,
}

LockerRoomOutfits = {
    DefinedLocations.LocationDefs.YellowLockerRoom: AssetLibrary.ImagePath.WorkerCoffeePath,
    DefinedLocations.LocationDefs.BlueLockerRoom: AssetLibrary.ImagePath.WorkerCowboyPath,
    DefinedLocations.LocationDefs.GreenLockerRoom: AssetLibrary.ImagePath.WorkerSafariPath,
    DefinedLocations.LocationDefs.PinkLockerRoom: AssetLibrary.ImagePath.WorkerLuauPath,
    DefinedLocations.LocationDefs.GreyLockerRoom: AssetLibrary.ImagePath.WorkerSuitPath,
}
