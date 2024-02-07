@ECHO OFF
cd ..
del __init__.py
pyinstaller ^
--onefile ^
--noconsole ^
--collect-all Classes ^
--collect-all Handlers ^
--collect-all Generators ^
--collect-all Utilities ^
--collect-all Assets ^
--add-data Assets:. ^
Main.py

del Main.spec
type nul > __init__.py
.\dist\Main.exe

