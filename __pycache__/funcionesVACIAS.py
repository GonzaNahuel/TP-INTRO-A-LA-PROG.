from funcionesSeparador import separador
from principal import *
from configuracion import *
from extras import *
import random
import math



def lectura(archivo, salida):
    for linea in archivo.readlines():
        salida.append(linea[0:-1])

def nuevaPalabra(lista):
    return lista[random.randint(0,len(lista))]

def silabasTOpalabra(silaba):
    pass

def palabraTOsilaba(palabra):
    palabraSilabas=separador(palabra)
    return palabraSilabas

def esCorrecta(palabraEnSilabasEnPantalla, palabra):
    palabraNueva = ""
    for letra in palabra:
        if letra == " ":
            palabraNueva=palabraNueva+"-"
        else:
            palabraNueva=palabraNueva+letra
    if palabraEnSilabasEnPantalla == palabraNueva:
        return True

def puntaje(palabra):
    return 5

