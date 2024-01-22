@ECHO OFF
black ..\..\PoppaPizza
ECHO ~~~~~~~~~~~~
vulture ..\..\PoppaPizza --min-confidence 70 
ECHO ~~~~~~~~~~~~
pyreverse -o png --source-roots ..\..\PoppaPizza ..\..\PoppaPizza
pyreverse --source-roots ..\..\PoppaPizza ..\..\PoppaPizza
move packages.png ..\..\PoppaPizza\Utilities
move packages.dot ..\..\PoppaPizza\Utilities
move classes.png ..\..\PoppaPizza\Utilities
move classes.dot ..\..\PoppaPizza\Utilities
