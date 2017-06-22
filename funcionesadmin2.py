def cargarAuto(BD):
    print ("Ingresar la Informacion del Auto")
    continuar = raw_input("Ingresar 'Salir' para terminar, cualquier otra cosa para continuar");
    while continuar != "Salir" and continuar != "salir":
        codigoprod = input("Ingresar el Codigo de Producto: ") 
        marca = raw_input("Ingresar su Marca: ")
        modelo = raw_input("Ingresar Modelo: ") 
        anio  = input("Ingresar anio: ")
        cantidad  = input("Ingresar anio: ")
        precio = input("Ingresar precio: ")
        BD.append((codigoprod,marca,modelo,anio,cantidad,precio)); 
        continuar = raw_input("Ingresar 'Salir' para terminar, cualquier otra cosa para continuar");
    return BD

def cantautdistintos(BD):
    modelo=raw_input ('Ingrese el modelo')
    sumador = 0
    for arc in BD
        if modelo==arc[2]
            sumador = sumador + arc[4]  
    return sumador