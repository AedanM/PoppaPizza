@ECHO OFF
>PrepOutput.txt (
ECHO ~~~~~~~~~~~~
ECHO ~Vulture~~~~
vulture ..\..\PoppaPizza --min-confidence 40 
ECHO ~~~~~~~~~~~~
ECHO ~code2Flow~~

code2flow -q --o .\Structure\UtilsCallGraph.png .
code2flow -q --o .\Structure\ClassesCallGraph.png ..\Classes
code2flow -q --o .\Structure\HandlersCallGraph.png ..\Handlers
code2flow -q --o .\Structure\DefinitionsCallGraph.png ..\Definitions
code2flow -q --o .\Structure\GeneratorsCallGraph.png ..\Generators
code2flow -q --o .\Structure\EngineCallGraph.png ..\Engine
code2flow -q --o .\Structure\MainCallGraph.png ..

ECHO ~~~~~~~~~~~~
ECHO ~PyReverse~~
pyreverse --source-roots ..\..\PoppaPizza ..\..\PoppaPizza --ignore Utilities

move packages.dot ..\..\PoppaPizza\Utilities\Structure
move classes.dot ..\..\PoppaPizza\Utilities\Structure

cd .\Structure

dot -Tpng packages.dot -o busyPackages.png -y
dot -Tpng classes.dot -o busyClasses.png -y

python ParseDot.py

dot -Tpng packages.dot -o packages.png -y
dot -Tpng enginePackages.dot -o enginePackages.png -x -y
dot -Tpng classes.dot -o inheritanceStructure.png -x -y
dot -Tpng classesAndMembers.dot -o classes.png -x -y

ECHO ~~~~~~~~~~~~
ECHO ~Cleanup~~~~
del UtilsCallGraph.gv
del ClassesCallGraph.gv
del HandlersCallGraph.gv
del DefinitionsCallGraph.gv
del GeneratorsCallGraph.gv
del EngineCallGraph.gv
del MainCallGraph.gv

del enginePackages.dot
del packages.dot
del classes.dot
del classesAndMembers.dot
ECHO ~~~~~~~~~~~~
)