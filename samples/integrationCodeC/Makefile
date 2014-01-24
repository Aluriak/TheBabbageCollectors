# But : utiliser du code C dans du python
# Moyen : utilisation de ctypes
#
# le code C est compilé en library (options -fPIC et -shared, extensions en .so).
# la library ainsi créée est appelée et utilisée par python et les méthodes de ctypes.
# le code C est exécuté.
#
# -fPIC permet de le linking de fonctions lors de la compilation. 

all:
	gcc -c cCode.c -fPIC -o cCode.o
	gcc -shared -o cCode.so cCode.o
	python main.py

