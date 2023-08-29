import sys

def ohce(nombre):
    return "¡Buenas noches " + nombre + "!"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nombre = sys.argv[1]