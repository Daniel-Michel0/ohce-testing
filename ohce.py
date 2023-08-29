import sys
import datetime

def ohce(nombre):
    hora_actual = int(datetime.datetime.now().hour)
    if 12 <= hora_actual and hora_actual < 20:
        return "¡Buenas tardes " + nombre + "!"
    elif 6 <= hora_actual < 12:
        return "¡Buenos días " + nombre + "!"
    else:
        return "¡Buenas noches " + nombre + "!"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nombre = sys.argv[1]