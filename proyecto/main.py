#Proyecto Final
#1. Escribir un programa principal (main) que tenga una funcion que muestre un menu de opciones
#2. Cada opcion debe ser importada desde otro modulo.
#3. Previamente a ingresar a las opciones pedira nombre de usuario y password en caso no tenga se podra registrar en una bd.
#3. Opcion 1 : Generar un proceso automatico que ingrese un archivo a una base de datos.  
#4. Opcion 2 : Generar un reporte de las ventas totales(filtrar data por fecha o ventas mayor a tal monto o  tipo de productos etc).
#5. Opcion 3 : Generar un grafico de las ultimas ventas agrupados por mes o categoria o etc.
#6. Opcion 4 : Genear  una bitacora con las acciones realizadas.
#7. Opcion 5 : SALIR

from servicios.functions import *
from monitoreo.logger import *

log=logger()

def showOpcions():
    msg="""
    Bienvenido Luis, Are you ready?
    ==> Elige una opcion
1. Cargar Data
2. Generar un reporte
3. Mostar gráfico
4. Salir
"""
    print(msg)
    opcion=input("Ingrese la opción: ")
    return opcion

def getFunction(opcion):
        #hacer el bucle

        if opcion=="1":
            print("Ingrese aquí")
            log.message(f"Realizo la carga de archivo")
            loadData()
        elif opcion =="2":
             log.message(f"Realizo el reporte")
             #poner log
             generateReport()
        elif opcion =="3":
            log.message(f"Realizo el grafico")
            showData()
        elif opcion =="4":
            print("¡Hasta luego! Regresa pronto")
            return True
        else:
             print("Ingresa una opcion valida por favor")
"""while True:
    showOpcions()
    opcion = input("Ingrese la opción: ")
    if opcion=="4":
        break
    getFunction(opcion)"""

if __name__=='__main__':
    while True:
        opcion=showOpcions()
        if getFunction(opcion)==True:
             break
        #getFunction(opcion)