def BDproductos():
    BD=[]
    a1=(001,"renault","clio",2011,22,62000)
    BD.append(a1)
    a2=(002,"renault","megane",2002,16,80000)
    BD.append(a2)
    a3=(003,"peugeot","206",2000,19,40000)
    BD.append(a3)
    a4=(004,"peugeot","307",2011,20,75000)
    BD.append(a4)
    a5=(005,"citroen","c4",2011,12,120000)
    BD.append(a5)
    a6=(006,"ford","mustang",1998,15,77000)
    BD.append(a6)
    return BD
def identificacion():
    BD=BDproductos()
    salir=0
    print 'Administrador: 1  Cliente: 2'
    i= input ('>')
    if (i==1):
        while salir!=1:
            pw= input ('Ingese su password: ')
            if (pw==123):
                print 'Bienvenido Admin :)'
                menuadmin(BD)
                salir=1
                '''Aca se van a modificar la BDproductos'''
            else:
                print 'Contrasenia Incorrecta'
    else:
        print 'Bienvenido Cliente'
        LS=[]
        menuclient(LS,BD)
def menuadmin(BD):
    print '1: Agregar un vehiculo'
    print '2: Obtener cantidad de vehiculos dependiendo de la marca'
    print '3: Obtener un listado de autos con anio determinado'
    print '4: Obtener un listado de autos cuyo modelo contiene una palabra determinada'
    print '5: Obtener un listado de autos'
    print '6: Remover un auto'
    print '7: Modificar auto'
    print '8: Modificar stock(incremento)'
    print '9: Modificar stock(decremento)'
    print '10: Obtener stock de un auto'
    print '11: Obtener cantidad de autos registrados en BD'
    opcion= input ('Que desea hacer?')
    if(opcion == 1):
        cargarAuto(BD)
    elif(opcion == 2):
        a=cantautdistintos(BD)
        print a
    elif(opcion==3):
        a=autosanio(BD)
        print a
    elif(opcion==4):
        a=palabradeter(BD)
    elif(opcion==5):
        a=listautos(BD)
    elif(opcion==6):
        a=eliminarauto(BD)
    elif(opcion==7):
        a=modificauto(BD)
    elif(opcion==8):
        a=agregarincrementar(BD)
    elif(opcion==9):
        a=restardecrementar(BD)
    elif(opcion==10):
        a=ostock(BD)
    elif(opcion==11):
        a=cantautos(BD)
def cargarAuto(BD):
    print ("Ingresar la Informacion del Auto")
    continuar = ""
    while continuar != "Salir":
        codigoprod = input("Ingresar el Codigo de Producto: ") 
        marca = raw_input("Ingresar su Marca: ")
        modelo = raw_input("Ingresar Modelo: ") 
        anio  = input("Ingresar anio: ")
        cantidad  = input("Ingresar cantidad: ")
        precio = input("Ingresar precio: ")
        BD.append((codigoprod,marca,modelo,anio,cantidad,precio)); 
        continuar = raw_input("Ingresar 'Salir' para terminar, cualquier otra cosa para continuar")
        if (continuar=="salir"):
            menuadmin(BD)
            
    return BD
def cantautdistintos(BD):
    marca=raw_input ('Ingrese la marca: ')
    acum=0
    for i in BD:
        if i[1]==marca:
            acum+=1
    print "hay :",acum,"modelos de",marca,"."
          
    menuadmin(BD)
def autosanio(BD):
    anio=input ('Ingrese el anio: ')
    for i in BD:
        if i[3]==anio:
            print i
        
    menuadmin(BD)
def palabradeter(BD):
    palabra=raw_input ('Ingrese una letra: ')
    for i in BD:
        if palabra in i[2]:
            print i
    menuadmin(BD)
def listautos(BD):
    for i in BD:
        print i[1],"|",i[2],"|",i[3]
    menuadmin(BD)
def eliminarauto(BD):
    auto=raw_input ('Ingrese el vehiculo: ')
    for i in BD:
        if i[2]==auto:
            BD.remove(i)
    for j in BD:
        print j[0],"|",j[1],"|",j[2],"|",j[3],"|",j[4],"|",j[5],"|"
    menuadmin(BD)
def modificauto(BD):
    codigo=input ('Ingrese el codigo del vehiculo:')
    for i in BD:
        if i[0]==codigo:
            print i
            BD.remove(i)
            llamarfunc=menumodificauto(BD,codigo)
            print llamarfunc
    menuadmin(BD)
def menumodificauto(BD,codigo):
    x=()
    print ("Ingresar la Informacion del Auto Nuevo")
    codigoprod = codigo
    marca = raw_input("Ingresar su Marca: ")
    modelo = raw_input("Ingresar Modelo: ") 
    anio  = input("Ingresar anio: ")
    cantidad  = input("Ingresar cantidad: ")
    precio = input("Ingresar precio: ")
    BD.append((codigoprod,marca,modelo,anio,cantidad,precio))
    modificauto(BD)
        
    return x
    menuadmin()
def agregarincrementar(BD):
    codigo=input ('Ingrese el codigo del vehiculo:')
    for i in BD:
        if i[0]==codigo:
            codigoprod = i[0]
            marca = i[1]
            modelo = i[2]
            anio  = i[3]
            x= input("Ingresar cantidad: ")
            cantidad  = i[4]+x
            precio = i[5]
            BD.insert(codigo,(codigoprod,marca,modelo,anio,cantidad,precio))
            BD.remove(i)
            print BD
    menuadmin(BD)
def restardecrementar(BD):
    codigo=input ('Ingrese el codigo del vehiculo:')
    for i in BD:
        if i[0]==codigo:
            codigoprod = i[0]
            marca = i[1]
            modelo = i[2]
            anio  = i[3]
            x= input("Ingresar cantidad a restar: ")
            cantidad  = i[4]-x
            precio = i[5]
            BD.insert(codigo,(codigoprod,marca,modelo,anio,cantidad,precio))
            BD.remove(i)
            print BD
    menuadmin(BD)
def ostock(BD):
    codigo=input ('Ingrese el codigo del vehiculo:')
    for i in BD:
        if i[0]==codigo:
            print i[4]
    menuadmin(BD)
def cantautos(BD):
    contador=0
    for i in BD:
        contador+=i[4]
    print contador
    menuadmin(BD)
#----------------------------------------------------------#
def menuclient(LS,BD):
    print '1: Autos Disponibles por marca'
    print '2: Autos Disponibles de la marca por modelo'
    print '3: Agregar a su lista de productos'
    print '4: Presupuesto'
    print '5: Remover autos'
    opcion= input ('Que desea hacer?')
    if(opcion == 1):
        dispauto(LS,BD)
    elif(opcion == 2):
        marcmodel(LS,BD)
    elif(opcion == 3):
        agregarchango(LS,BD)
    
def dispauto(LS,BD):
    marca= raw_input('Ingrese la marca: ')
    for i in BD:
        if marca==i[1]:
            if i[4]>0:
                print i[2]
    menuclient(LS,BD)
def marcmodel(LS,BD):
    marca= raw_input('Ingrese la marca: ')
    for i in BD:
        if marca==i[1]:
            if i[4]>0:
                print i[2],":",i[4]
def agregarchango(LS,BD):
    model=raw_input('Ingrese el modelo del auto: ')
    cant=input('Ingrese la cantidad que desea comprar: ')
    for i in BD:
        if model==i[2]:
            if cant<=i[4]:
                
                codigoprod = i[0]
                marca = i[1]
                modelo = i[2]
                anio  = i[3]
                cantidad  = i[4]
                precio = i[5]
                BD.insert((codigoprod,marca,modelo,anio,cantidad,precio))
            
identificacion()
        
        
        
        

