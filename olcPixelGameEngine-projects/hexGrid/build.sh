#! /bin/sh
echo Project built and gethered in bin/debug/
g++ -c src/*.cpp -I include && g++ *.o -o bin/debug/main -lGL -lpng -lX11
