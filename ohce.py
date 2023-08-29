import sys
import datetime

def ohce(nombre):
    hora_actual = int(datetime.datetime.now().hour)
    if 12 <= hora_actual and hora_actual < 20:
        return ("¡Buenas tardes " + nombre + "!")
    elif 6 <= hora_actual < 12:
        return ("¡Buenos días " + nombre + "!")
    else:
        print("¡Buenas noches " + nombre + "!")    
    stop = False
    while not stop:
        voltear = input()
        print(voltear[::-1])

def saludos(nombre):
    hora_actual = int(datetime.datetime.now().hour)
    if 12 <= hora_actual and hora_actual < 20:
        return ("¡Buenas tardes " + nombre + "!")
    elif 6 <= hora_actual < 12:
        return ("¡Buenos días " + nombre + "!")
    else:
        return ("¡Buenas noches " + nombre + "!")   

def voltear(palabra):
        voltear = input()
        print(voltear[::-1])

def main():
    ohce()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nombre = sys.argv[1]