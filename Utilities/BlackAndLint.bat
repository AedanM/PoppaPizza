cd ..
black ..\PoppaPizza
set disabledEffects=--disable global-statement,missing-function-docstring,consider-using-from-import,missing-class-docstring,too-few-public-methods
set NamingStyles=--attr-naming-style PascalCase --method-naming-style PascalCase --function-naming-style PascalCase --variable-naming-style camelCase --argument-naming-style camelCase --module-naming-style PascalCase --class-const-naming-style PascalCase --class-attribute-naming-style PascalCase
pylint  %disabledEffects% %NamingStyles% --recursive True --source-roots Classes,Utilities,Handlers ..\PoppaPizza 
pause