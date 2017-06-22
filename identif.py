def identificacion():
    salir=0
    print 'Administrador: 1  Cliente: 2'
    i= input ('>')
    if (i==1):
        while salir!=1:
            pw= input ('Ingese su password: ')
            if (pw==123):
                print 'Bienvenido Admin :)'
                salir=1
                '''Aca se van a modificar la BDproductos'''
            else:
                print 'Contrasenia Incorrecta'
    else:
        print 'Bienvenido Cliente'
identificacion()
    
        
        
