# lea un numero entero de 5 digitos y determinar si es capicua 

print("------------------------------------")
print("---NUMERO ENTERO Y DE CINCO DIGITOS ")
print("------------------------------------")

# input

x = int(input("Digite el valor del numero: "))

#   Processing 

if 9999 < x < 100000:
    msj = (" El numero digitado tiene cinco digitos")
else:
    msj = (" El numero digitado no tiene cinco digitos ")

n1 = x / 10
n2 = x / 1000
n3 = x / 10000

if (10 == 10000):
    msj = (" El numero es capicuan ")

if ( 100 == 1000):
    msj = (" El numero es capicuan ")


# output

print("El numero es " + str(x) + msj )














