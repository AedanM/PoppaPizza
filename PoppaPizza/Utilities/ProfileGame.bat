@ECHO OFF
cd ..

python -m cProfile -o program.prof Main.py
snakeviz program.prof

del program.prof