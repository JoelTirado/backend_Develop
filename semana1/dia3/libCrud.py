### LIBRERIA DE CRUD ####
############# FUNCIONES ###############
def buscarAlumno(valorBusqueda,listaAlumnos):
    indiceAlumno = -1
    for indice in range(len(listaAlumnos)):
        alumno = listaAlumnos[indice]
        for clave,valor in alumno.items():
            if(clave == "email" and valor == valorBusqueda):
                indiceAlumno = indice
                break
    return indiceAlumno

######################################