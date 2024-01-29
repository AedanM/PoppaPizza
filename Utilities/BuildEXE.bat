@ECHO OFF
cd ..
pyinstaller ^
--noconsole ^
-p .\Classes ^
-p .\Handlers ^
-p .\Generators ^
-p .\Utilities ^
-p .\Assets ^
--collect-all Classes ^
--collect-all Handlers ^
--collect-all Generators ^
--collect-all Utilities ^
--hidden-import Classes ^
--hidden-import Handlers ^
--hidden-import Generators ^
--hidden-import Utilities ^
Main.py