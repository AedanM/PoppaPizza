@ECHO OFF
cd ..\

pdoc3 --html Main.py -o Docs\Documentation --force

pdoc3 --html Classes -o Docs\Documentation --force
python Utilities\RestructureDocumentation.py -f .\Docs\Documentation\Classes\index.html

pdoc3 --html Generators -o Docs\Documentation --force
python Utilities\RestructureDocumentation.py -f .\Docs\Documentation\Generators\index.html

pdoc3 --html Handlers -o Docs\Documentation --force
python Utilities\RestructureDocumentation.py -f .\Docs\Documentation\Handlers\index.html

pdoc3 --html Definitions -o Docs\Documentation --force
python Utilities\RestructureDocumentation.py -f .\Docs\Documentation\Definitions\index.html

pdoc3 --html Testing -o Docs\Documentation --force
python Utilities\RestructureDocumentation.py -f .\Docs\Documentation\Testing\index.html

pdoc3 --html Engine -o Docs\Documentation\ --force
python Utilities\RestructureDocumentation.py -f .\Docs\Documentation\Engine\index.html

