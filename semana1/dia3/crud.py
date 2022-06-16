
import os
import time
from tabulate import tabulate
from libCrud import *

""" APLICACIÓN CRUD
C - CREATE
R - READ
U - UPDATE
D - DELETE
PARA ESTE CASO USAREMOS ALUMNOS
[
    {'nombre':'','email':'','celular':''},
    {'nombre':'','email':'','celular':''}
]
"""
alumnos = [
    {'nombre':'cesar mayta',
    'email':'cesarmayta@gmail.com',
    'celular':'956290589'}
    ]



opcion = "0"
while(opcion != "5"):
    if(opcion != "0"):
        time.sleep(1)
        os.system("clear")
    menu()
    opcion = input("INGRESE LA OPCIÓN A EJECUTAR : ")
    os.system("clear")
    if(opcion == "1"):
        print(
        """
        ============================
        [1] REGISTRO DE NUEVO ALUMNO
        ============================
        """)
        insertarAlumno(alumnos)
        print(
        """
        ================================
            ALUMNO REGISTRADO !!!
        ================================
        """)
    elif(opcion == "2"):
        columnas = ["nombre","email","celular"]
        tablaAlumnos = [alumno.values() for alumno in alumnos]
        print(tabulate(tablaAlumnos,headers=columnas,tablefmt="grid"))

        input("presione Enter para continuar ...")
        
    elif(opcion == "3"):
        print(
        """
        ========================
        [3]  ACTUALIZAR UN ALUMNO
        ========================
        """)
        valorBusqueda = input("ingrese el email del alumno a actualizar : ")
        
        indiceAlumno = buscarAlumno(valorBusqueda,alumnos)
        
        if(indiceAlumno == -1):
            print("No se encontro el alumno")
        else:
            actualizarAlumno(indiceAlumno,alumnos)
            print("ALUMNO ACTUALIZADO!!!")
    elif(opcion == "4"):
        print(
        """
        ========================
        [4]  ELIMINAR ALUMNO
        ========================
        """)
        valorBusqueda = input("ingrese el email del alumno a eliminar : ")
        
        indiceAlumno = buscarAlumno(valorBusqueda,alumnos)

        if(indiceAlumno == -1):
            print("No se encontro el alumno")
        else:
            alumnos.pop(indiceAlumno)
            print("ALUMNO ELIMINADO !!!")
    elif(opcion == "5"):
        print(
        """
        ===========================
        EL SISTEMA SE ESTA CERRANDO
        ===========================
        """)
    else:
        print(
        """
        ===========================
            OPCIÓN INCORRECTA!!!
        ===========================
        """)