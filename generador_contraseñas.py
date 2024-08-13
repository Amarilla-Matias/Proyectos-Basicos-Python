import string
import random

def generar_contrasena(longitud):
    caracter = string.ascii_letters + string.digits + string.punctuation
    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(caracter)
    return contrasena

longitud = int(input("Ingrese la longitud de la contraseña deseada: "))
nueva_contrasena = generar_contrasena(longitud)
print("La contraseña generada es: ", nueva_contrasena)