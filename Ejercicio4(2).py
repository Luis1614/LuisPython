Edad=int(input("Ingrese su edad: "))
if Edad>=18:
    Ingreso=float(input("Digite su ingreso mensual en soles: "))
    if Ingreso>=1000:
        print("¡Felicidades! Usted aplica para una tarjeta de credito")
        if Ingreso<=3000:
            print("Con este ingreso usted aplica para una tarjeta clásica")
        else:
            print("Con este ingreso usted Usted aplica para una tarjeta dorada")
    else:
        print("Su ingreso mensual es insuficiente")
else:
    print("No cumple con la edad mínima, debe tener 18 años")