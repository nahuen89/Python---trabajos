# -*- coding: utf-8 -*-


def menu(informacion):
    opcion =input("Ingresar \n\t 0 - Para Salir \n "+
                    "\t 1 - Cargar Información de los Alumnos "+
                    "\n \t  2 - Calcular Edad Promedio "+
                    " \n \t  3 - Cantidad de Personas de un Sexo "+
                    " \n \t  4 - Determinar la Calificación mas alta del Curso "+
                    " \n \t  5 - Mostrar la información del alumno con la calificacion mas alta "+
                    "\n ");
    if(opcion == 1):
        informacion = cargarInformacion(informacion);
        print len(informacion);
    elif opcion == 2:
        print("La edad promedio es ", calcularEdadPromedio(informacion));
    
    elif opcion == 4:
        print("La Nota mas alta es:", determinarNotaMasAlta(informacion));
    elif opcion == 5:
        mostratInfoNotaMasAlta(informacion);
    elif opcion == 3:
        genero = raw_input("Ingresar el Genero a contar");
        print("La cantidad de Personas con genero ", genero, "es: ",cantidadPersonasGenero(genero,informacion));
    else :
        print("Gracias por Usar nuestros servicios");
    return opcion;
 
def cargarInformacion(informacion):
    print "Ingresar la Informacion de los Alumnos"
    continuar = raw_input("Ingresar 'Salir' para terminar, cualquier otra cosa para continuar");
    while continuar != "Salir" and continuar != "salir":
        nombre = raw_input("Ingresar su Nombre: ") 
        edad = input("Ingresar su Edad: ") 
        genero = raw_input("Ingresar su Genero: ")
        notaPromedio = input("Ingresar su Promedio: ") 
        informacion.append((nombre,edad,genero,notaPromedio)); 
        continuar = raw_input("Ingresar 'Salir' para terminar, cualquier otra cosa para continuar");
    return informacion

def calcularEdadPromedio(informacion):
    print "Vamos a calcular la edad Promedio del curso";
    sumador = 0;
    for dato in informacion:
        
        sumador = sumador + dato[1];    
        
    return sumador/len(informacion)


def determinarNotaMasAlta(informacion):
    mayor = 0;
    for dato in informacion:
        if(mayor < dato[3]):
            mayor = dato[3];
        
    return mayor

def mostratInfoNotaMasAlta(informacion):
    mayor = determinarNotaMasAlta(informacion);
    for dato in informacion:
        if(mayor == dato[3]):
            print "El alumno",dato[0]," tiene la nota mas alta.";
        
    

def cantidadPersonasGenero(elgenero,lainformacion):
    print "Vamos a contar la cantidad de personas con genero ",elgenero," del curso.";
    sumador = 0;
    for dato in lainformacion:
        if(dato[2] == elgenero):
            sumador = sumador + 1;    
        
    return sumador

def login():
    verifica = False;
    salir = False;
    while not verifica and not salir:
        print("Ingresar 'Salir' para terminar");
        usuario = raw_input("Ingresar el usuario: ");
        if usuario == "Salir" or usuario == "salir":
            verifica = False;
            salir = True;
        else : 
            contrasenia = raw_input("Ingresar la contraseña: ");
            if usuario == "malapi" and contrasenia == "1234":
                verifica = True;
            elif usuario == "vivi" and contrasenia == "1234":
                verifica = True;
            elif usuario == "luis" and contrasenia == "1234":
                verifica = True;
            else :
                verifica = False;
                print("Vuelva a intentarlo, el usuario y contraseña no se puedieron verificar");
                
    return verifica;

def principal():
    if(login()):
        print("Ahora podemos mostrarle el menu");
        opcion = -1;
        informacion = [];
        while opcion != 0:
            opcion = menu(informacion);
            
    else :
        print("Uds. no es un usuario valido");
        
principal();
