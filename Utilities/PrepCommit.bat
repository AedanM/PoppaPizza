@ECHO OFF
black ..\..\PoppaPizza
ECHO ~~~~~~~~~~~~
vulture ..\..\PoppaPizza --min-confidence 40 
ECHO ~~~~~~~~~~~~
code2flow -q --o .\Structure\UtilsCallGraph.png .
del .\Structure\UtilsCallGraph.gv
code2flow -q --o .\Structure\ClassesCallGraph.png ..\Classes
del .\Structure\ClassesCallGraph.gv
code2flow -q --o .\Structure\HandlersCallGraph.png ..\Handlers
del .\Structure\HandlersCallGraph.gv
code2flow -q --o .\Structure\DefinitionsCallGraph.png ..\Definitions
del .\Structure\DefinitionsCallGraph.gv
code2flow -q --o .\Structure\GeneratorsCallGraph.png ..\Generators
del .\Structure\GeneratorsCallGraph.gv
code2flow -q --o .\Structure\MainCallGraph.png ..
del .\Structure\MainCallGraph.gv
ECHO ~~~~~~~~~~~~
pyreverse --source-roots ..\..\PoppaPizza ..\..\PoppaPizza
move packages.dot ..\..\PoppaPizza\Utilities\Structure
move classes.dot ..\..\PoppaPizza\Utilities\Structure
cd .\Structure
python ParseDot.py
dot -Tpng packages.dot -o packages.png -y
dot -Tpng classes.dot -o classes.png -x -y

del packages.dot
del classes.dot

ECHO ~~~~~~~~~~~~