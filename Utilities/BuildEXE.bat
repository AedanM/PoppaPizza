@ECHO OFF
cd ..
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


.\dist\Main.exe