@ECHO off
python ParseDot.py
dot -Tpng packages.dot -o packages.png -x