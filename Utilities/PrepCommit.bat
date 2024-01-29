@ECHO OFF
black ..\..\PoppaPizza
ECHO ~~~~~~~~~~~~
vulture ..\..\PoppaPizza --min-confidence 40 
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