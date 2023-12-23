"""
#Veririficar si un numero es o impar
numero = int(input('Ingrese un número: '))
if numero % 2 == 0:
    print("el número es par")
else:
    print("el numero es impar")


#Clasificar a una persona en una categoría de edad

edad = int(input("Ingresa su edad: "))
if edad <= 10:
    print("Eres un niño")
elif edad >=11 and edad <=17:
    print("Eres un adolescente")
elif edad >=18:
    print("Eres un adulto")

    #Evaluar la nota de un alumno e indicar que tipo de letra tiene

nota = int(input("¿Cuál es tu calificación?: "))
if nota == 20:
    print("Tu sacaste A")
elif nota <20 and nota >15:
    print("Tu nota es de B")
elif nota <14 and nota >10:
    print("Tu no es C")
elif nota < 9:
    print("Tu nota es D")

       
#Calcular el descuento de una tienda si el monto supera los 100$ aplicar el 10% de descuento

precio = int(input("¿Cuánto cuesta el producto: ?"))

if precio >= 100:
    descuento = precio *0.10
    total = precio - descuento
    print(f"El monto final será de {total} " )

#Determinar el tipo de triángulo en base a sus lados Equilatero, Isosceles y Escaleno
lado1 = int(input("Ingrese el primer lado: "))
lado2= int(input("Ingrese el segundo lado: "))
lado3 = int(input("Ingrese el tercer lado: "))

if lado1 == lado2 and lado2 == lado3:
    print("El triángulo es equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("El triángulo es Isosceles")
else:
    print("El triángulo es Escaleno")

"""

#Convertir un valor de dolores a bs y viceversa

print("¿Qué desea hacer?")
decision = int(input("Convertir monto en dólares - ingrese 1 \nConvertir monto en bs - ingrese 2 \nIngresa el valor: "))

match decision:
    case 1:
        monto = float(input("Ingrese el monto en bolivares para saber cuantos dólares son: "))
        dolares = monto / 35.78
        print(f"{monto} bs en dólares es igual a {dolares} $")
    case 2:
        monto = float(input("Ingrese el monto en dólares para saber cuantos bolívares son: "))
        bolivares = monto * 35.78
        print(f"{monto} $ en bolivares es igual a {bolivares} bs")