#! /bin/sh
echo Project built and gethered in bin/debug/
g++ -c src/*.cpp -I include && g++ *.o -o bin/debug/hex -lsfml-graphics -lsfml-system -lsfml-window
