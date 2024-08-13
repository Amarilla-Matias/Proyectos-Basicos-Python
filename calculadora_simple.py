def suma(a, b):
    return a + b
def resta(a, b):
    return a - b 
def multiplicacion(a, b):
    return a * b
def division(a, b):
    return a / b

#Preguntar al usuario la operacion que desea realizar
while True:
        try:
            operacion = int(input("Seleccione la operacion que desea realizar:"
                "\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n"))
            if (operacion <= 4 and operacion > 0):
                break
        except:
            print("Ingrese un entero Valido!")

#Pedir al usuario los numeros a operar
num1 = float(input("Ingrese el primer Numero: "))
num2 = float(input("Ingrese el segundo Numero: "))

#Realizar la operacion seleccoionda por el usuario

if operacion == 1:
    resultado = suma(num1, num2)
elif operacion == 2:
    resultado = resta(num1, num2)
elif operacion == 3:
    resultado = multiplicacion( num1, num2)
elif operacion == 4:
    resultado = division(num1, num2)
else:
    resultado = "Operacion no Valida!"
    print("Operacion no Valida")

print(f"Resultado: {resultado}")