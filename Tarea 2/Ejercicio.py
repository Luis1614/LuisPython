"""
A. Crear un menu iterativo con las siguientes opciones:
    opcion 1: 'Saludar' , pedir datos personales
    opcion 2: Realizar una operacion matematica pedir 2 numeros
    opcion 3: Agregar a lista un diccionario que tenga (nombre ,edad ,correo,cursos). Los cursos sera a su vez una lista de diccionario que tendra las llaves de 
    nombre de curso y listado de notas
    opcion 4: calcular el promedio de las notas y agregar las notas finales a una lista
    opcion 5: mostrar listado de alumnos aprobados
    opcion 6: mostrar listado de alumnos desaprobados
    opcion 7: Generar una funcion rango hasta un numero grande (10^10) con un step y agregar a una lista los numeros que cumplan la condicion de ser
    multiplo de 2 ,  5 y de 7.Finalmente mostrar el tamaño de esa lista.
    opcion 8: llamar a una funcion que devuelva el mayor de 2 numeros ingresados por teclado.
    opcion 9: Salir.
"""

def saludar():
    nombre = input("Ingrese su nombre completo: ")
    edad = int(input("Ingrese su edad: "))
    correo = input("Ingrese su correo electrónico: ")
    print(f"""Hola,{nombre}!. Bienvenido a este menú iterativo
          Para recordarte que tu edad es {edad} años y tu correo es {correo}""")

def realizar_operacion():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación a realizar (+, -, *, /): ")
    if operacion == '+':
        resultado = a + b
    elif operacion == '-':
        resultado = a - b
    elif operacion == '*':
        resultado = a * b
    elif operacion == '/':
        resultado = a / b
    print(f"El resultado de la operación es: {resultado}")

def agregar_alumno(lista_alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    edad = int(input("Ingrese la edad del alumno: "))
    correo = input("Ingrese el correo electrónico del alumno: ")
    cursos = []
    while True:
        curso_nombre = input("Ingrese el nombre del curso o 'fin' para salir : ")
        if curso_nombre.lower() == 'fin':
            break
        notas = []
        while True:
            nota = input(f"Ingrese una nota para el curso '{curso_nombre}' (o 'fin' para terminar): ")
            if nota.lower() == 'fin':
                break
            notas.append(float(nota))
        cursos.append({"nombre": curso_nombre, "notas": notas})
    lista_alumnos.append({"nombre": nombre, "edad": edad, "correo": correo, "cursos": cursos})
    print("Alumno agregado con éxito.")

def calcular_promedio(lista_alumnos, lista_notas_finales):
    for alumno in lista_alumnos:
        for curso in alumno["cursos"]:
            promedio_curso = sum(curso["notas"]) / len(curso["notas"])
            lista_notas_finales.append(promedio_curso)
    print("Promedio de notas calculado y agregado a la lista.")

def mostrar_aprobados(lista_alumnos, lista_notas_finales):
    for i, alumno in enumerate(lista_alumnos):
        if lista_notas_finales[i] >= 10:
            print("Nombre:", alumno["nombre"])
            print("Promedio de notas:", lista_notas_finales[i])
            print("Estado: Aprobado")

def mostrar_desaprobados(lista_alumnos, lista_notas_finales):
    for i, alumno in enumerate(lista_alumnos):
        if lista_notas_finales[i] < 10:
            print("Nombre:", alumno["nombre"])
            print("Promedio de notas:", lista_notas_finales[i])
            print("Estado: Desaprobado")

def generar_lista_multiplos():
    mcm = 2 * 5 * 7  # Mínimo común múltiplo de 2, 5 y 7
    lista_multiplos = []
    for i in range(0, 10**10, mcm):
        lista_multiplos.append(i)
    print("Tamaño de la lista de múltiplos:", len(lista_multiplos))

def obtener_mayor():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    mayor = max(a, b)
    print(f"El número mayor es:{mayor}")

if __name__ == "__main__":
    alumnos = []
    notas_finales = []

    while True:
        print("\nMenú:")
        print("1. Saludar")
        print("2. Realizar operación matemática")
        print("3. Agregar alumno")
        print("4. Calcular promedio de notas")
        print("5. Mostrar listado de alumnos aprobados")
        print("6. Mostrar listado de alumnos desaprobados")
        print("7. Generar lista de múltiplos")
        print("8. Obtener el mayor de dos números")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                saludar()
            case "2":
                realizar_operacion()
            case "3" :
                agregar_alumno(alumnos)
            case "4":
                calcular_promedio(alumnos, notas_finales)
            case "5":
                mostrar_aprobados(alumnos, notas_finales)
            case "6":
                mostrar_desaprobados(alumnos, notas_finales)
            case "7":
                generar_lista_multiplos()
            case "8":
                obtener_mayor()
            case "9":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción del menú.")
