import sys
from ejercicio1 import main as ejercicio1_main
import ejercicio2
import ejercicio3

def main():
    while True:
        ejercicio = input("Ingrese el número del ejercicio que desea ejecutar (1, 2 o 3), o 0 para salir: ")
        
        if ejercicio == "0":
            sys.exit()
        if ejercicio == "1":
            ejercicio1_main()
        elif ejercicio == "2":
            ejercicio2.main()
        elif ejercicio == "3":
            ejercicio3.main()
        else:
            print("Ejercicio inválido")

if __name__ == "__main__":
    main()