@ECHO OFF
black ..\..\PoppaPizza
ECHO ~~~~~~~~~~~~
set disabledEffects=--disable import-error,global-statement,missing-function-docstring,consider-using-from-import,missing-class-docstring,too-few-public-methods
set NamingStyles=--attr-naming-style PascalCase --method-naming-style PascalCase --function-naming-style PascalCase --variable-naming-style camelCase --argument-naming-style camelCase --module-naming-style PascalCase --class-const-naming-style PascalCase --class-attribute-naming-style PascalCase
pylint  %disabledEffects% %NamingStyles% --recursive True --source-roots Classes,Utilities,Handlers ..\..\PoppaPizza 
ECHO ~~~~~~~~~~~~
mypy --explicit-package-bases  --ignore-missing-imports --check-untyped-defs  ..\..\PoppaPizza
ECHO ~~~~~~~~~~~~
vulture ..\..\PoppaPizza --min-confidence 70 
ECHO ~~~~~~~~~~~~
pyreverse -o png --source-roots ..\..\PoppaPizza ..\..\PoppaPizza
move packages.png ..\..\PoppaPizza\Utilities
move classes.png ..\..\PoppaPizza\Utilities
pause