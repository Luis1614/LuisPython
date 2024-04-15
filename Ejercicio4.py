Edad=int(input("Ingrese su edad: "))
if Edad>=18:
    Ingreso=float(input("Digite su ingreso mensual en soles: ")) 
    if Ingreso>=1000 and Ingreso<=3000:
        print("Usted obtiene una tarjeta clásica")
        if Ingreso>3000:
            print("Usted obtiene una tarjeta Dorada")
    else:
        print("aumente")
else:
    print("mo tiene edad minima")