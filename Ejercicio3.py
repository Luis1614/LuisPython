numero = int(input("Ingrese la cantidad de números a sumar: "))
suma = 0
for i in range(1, numero + 1):
    suma += i
print(f"La suma de los números hasta {numero} es: {suma}")