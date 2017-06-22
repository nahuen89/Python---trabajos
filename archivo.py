# -*- coding: utf-8 -*-
'''
Implementacion de la funcionalidad básica para la gestion de lista de archivos.
cargarInicial() => retorna una lista de tuplas, donde cada tupla contiene informacion de archivo
visualizarListaArchivo(LA)
cargarArchivo(LA)
eliminarArchivo(ListaArchivo , claveArchivo)
modificaArchivo(LA,claveArchivo) 
calcularSumaTamanio(LA) => retorna la suma de los tamnios de los archivos de la lista
calcularSumaTamanioExtension(LA, extension) => retorna la suma de los tamnios de los archivos con extension 
archivoPorExtension(LA, extension) => retorna una nueva lista
pruebaMetodos()
'''


'''
Metodo que crea una lista de tuplas, donde cada tupla contiene informacion de archivos (nombre,extension,tamanio,nombreAutor)
'''
def cargarInicial():
    LA=[]
    a1 = ("archivo1", "xls", 3,"autor1")
    LA.append(a1)
    a2 = ("archivo2", "doc", 13,"autor2")
    LA.append(a2)
    a3 = ("archivo3", "dot", 99,"autor3") 
    LA.append(a3)
    a4 = ("archivo4", "doc", 45,"autor4")
    LA.append(a4)
    a5 = ("archivo5", "dot", 6,"autor5") 
    LA.append(a5)
    return LA

'''
Metodo que recorre la lista LA que recibe por parametro y visualiza cada uno de sus elementos
'''
def visualizarListaArchivo(LA):
    for unArchivo in LA:
        print("--------------------------------------") 
        print("Nombre: ",unArchivo[0]) 
        print("Extension: ",unArchivo[1])
        print("Tamanio ",unArchivo[2]) 
        print("Autor: ",unArchivo[3])
        print("--------------------------------------")
        
        
'''
Metodo que permite incorporar archivos a la lista LA que se recibe por parametro
'''        
def cargarArchivo(LA):
    print ("Ingresar la Informacion de los Archivos")
    continuar = raw_input("Ingresar 'Salir' para terminar, cualquier otra cosa para continuar");
    while continuar != "Salir" and continuar != "salir":
        nombre = raw_input("Ingresar su Nombre: ") 
        extension = raw_input("Ingresar su extension: ")
        tamanio = input("Ingresar tamanio ") 
        autor  = raw_input("Ingresar su autor: ")
        LA.append((nombre,extension,tamanio,autor)); 
        continuar = raw_input("Ingresar 'Salir' para terminar, cualquier otra cosa para continuar");
    return LA
'''
Metodo que permite eliminar un archivo de la lista ListaArchivo cuyo nombre coincide con el valor de la variable claveArchivo
'''

def eliminarArchivo(ListaArchivo , claveArchivo):
    indice = 0
    band =True
    while (indice < len(ListaArchivo) and band ):
        unArchivo = ListaArchivo[indice]
        if(unArchivo[0] == claveArchivo):
            ListaArchivo.remove(unArchivo)
            band = False
        indice = indice + 1 
'''
Metodo que permite mdificar un archivo de la lista LA cuyo nombre coincide con el valor de la variable claveArchivo. 

'''
def modificaArchivo(LA,claveArchivo):
 
    indice = 0
    band = True
    while (indice < len(LA) and band ):
        unArchivo = LA[indice]
        if(unArchivo[0] == claveArchivo):
            respuesta = raw_input("Ingrese 1 si desea modificar la extension: ")
            if(respuesta=="1"):
                extension = raw_input("Ingresar la nueva extension: ")
            else:
                extension =unArchivo[1]
            respuesta = raw_input("Ingrese 1 si desea modificar el tamanio: ")
            if(respuesta=="1"):
                tamanio = input("Ingresar tamanio ")
            else:
                tamanio =unArchivo[2]
            respuesta = raw_input("Ingrese 1 si desea modificar el autor: ") 
            if(respuesta=="1"):
                autor  = raw_input("Ingresar su autor: ")
            else:
                autor =unArchivo[3]
            archModificado = (claveArchivo,extension,tamanio,autor)    
            eliminarArchivo(LA,claveArchivo)
            LA.append(archModificado)
            band = False
        indice = indice + 1 
'''
Metodo que permite calcular la suma de los tamanios de los archivos contenidos en la lista LA
'''
def calcularSumaTamanio(LA):
    sumador = 0;
    for unArchivo in LA:
        sumador = sumador + unArchivo[2];    
        
    return sumador

'''
Metodo que permite calcular la suma de los tamanios de los archivos contenidos en la lista LA, cuya extension es igual al valor de la variable extension
'''
def calcularSumaTamanioExtension(LA, extension):
    sumador = 0;
    for unArchivo in LA:
        if(unArchivo[1] == extension):
            sumador = sumador + unArchivo[2];    
        
    return sumador

'''
Metodo que recorre la lista y retorna una nueva lista donde sus archivos tienen como extension el valor contenido en la variable extension
'''
def archivoPorExtension(LA, extension):
    nuevaLista = []
    for unArchivo in LA:
        if(unArchivo[1]==extension):
            nuevaLista.append(unArchivo)            
    return nuevaLista


'''
Metodo que permite probar la funcionalidad implementada
'''
def pruebaMetodos():
        listaInicial =cargarInicial()
        visualizarListaArchivo(listaInicial)
        #A continuacion se prueba cada uno de los métodos implementados, descomentar segun desee

        print("La suma de los tamanios de los archivos es: ",calcularSumaTamanio(listaInicial))
        print("La suma de los tamanios de los archivos .dot es: ",calcularSumaTamanioExtension(listaInicial,"dot"))
       
        
        listaArchivosDoc =  archivoPorExtension(listaInicial,"dot")
        print("A continuacion se listan los archivos .dot: ")
        visualizarListaArchivo(listaArchivosDoc)
        
        eliminarArchivo(listaInicial , "archivo4")
        print("A continuacion se listan los archivos sin el archivo  'archivo4' : ")
        visualizarListaArchivo(listaInicial)
        
        modificaArchivo(listaInicial , "archivo5")
        print("A continuacion se listan los archivos sin el archivo  'archivo5' : ")
        visualizarListaArchivo(listaInicial)

pruebaMetodos()