# Quiz: DETERMINAR NUMERO ENTERO DE 5 DIGITOS Y DETERMINAR SI ES CAPICUA 

print("-------------------------------------")
print("-------------------------------------")
print("---------- numero_capicua------------")
print("-------------------------------------")
print("-------------------------------------")

#input
N = int(input("Por favor dígite un número de 5 dígitos: "))

#proccesing 

#<>10000
if N >= 100000 or N <= 9999:
    print("")
    print("El numero digitado tiene cuatro digitos_digita otro que tenga 5")

else:
    N1 = int(str(N)[::-1])
    if N1 == N:
        print("el número",N," es un número capicúa")
    else:
        print("el número",N,"no es un número capicúa")














