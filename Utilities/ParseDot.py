"""Get stats from Dot file"""
from dataclasses import dataclass


@dataclass
class Module:
    NumDepends: int = 0
    NumImports: int = 0
    Name: str = ""

    def __repr__(self):
        return f"{self.Name} D:{self.NumDepends} I:{self.NumImports}"


ModuleList: list[Module] = []

with open("packages.dot", "r") as fp:
    for line in fp:
        if "->" in line:
            importer = line.split(" ")[0].replace('"', "")
            imported = line.split(" ")[2].replace('"', "")
            # print(ModuleList, imported, importer)
            importerModule = [x for x in ModuleList if x.Name == importer][0]
            importedModule = [x for x in ModuleList if x.Name == imported][0]
            importerModule.NumImports += 1
            importedModule.NumDepends += 1
        elif "[" in line:
            modName = line.split(" ")[0].replace('"', "")
            mod = Module(Name=modName)
            ModuleList.append(mod)
    x = sorted(ModuleList, key=lambda x: x.NumDepends, reverse=True)
    for i in x:
        print(i)
