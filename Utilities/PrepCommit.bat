@ECHO OFF
black ..\..\PoppaPizza
ECHO ~~~~~~~~~~~~
vulture ..\..\PoppaPizza --min-confidence 70 
ECHO ~~~~~~~~~~~~
pyreverse --source-roots ..\..\PoppaPizza ..\..\PoppaPizza
move packages.dot ..\..\PoppaPizza\Utilities
move classes.dot ..\..\PoppaPizza\Utilities
python ParseDot.py
dot -Tpng packages.dot -o packages.png -x -y
dot -Tpng classes.dot -o classes.png -x -y