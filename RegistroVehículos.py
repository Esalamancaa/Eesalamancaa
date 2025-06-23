#Tarea
#Crear gestión de vehículos
#Crear programa para un parking de autos
#Se debe ingresar marca, año, patente y tipo
#Marca: Tipo string, debe typear la marca
#Año: Solo de 4 digitos enteros
#Patente: Debe tener 4 letras minusculas y 2 digitos
#Tipo: S=sedan, C=Camioneta, M=Moto
#Se debe validar cada aspecto y debe tener un mantenedor para todo los vehículos motorizados

#1.- Ingresar vehiculos
#2.- Mostrar vehiculos
#3.- Actualizar vehiculo
#4.- Borrar vehiculo
#5.- Mostrar estadisticas: ultimo vehiculo ingresado y total en garage
#6.- Salir

#Usar funciones con argumentos para poder validar y para poder llamar las acciones dentro del menú  


 
def mostrar_vehiculos():
    for key,vehiculo in Vehículos.items():
        print(key,".-",vehiculo)
def ingresar_vehiculos():
    marca=input("Ingrese la marca: ")
    while True:
        año=int(input("Ingrese el año: "))
        laño=str(año)
        if len(laño)==4:
            break
        else:
            print("El año debe estar en formato de 4 numeros. Ejemplo: 2010") 
    while True:
        patente=input("Ingrese la patente: ")
        if len(patente)==6:
            break
        else:
            print("La patente debe estar en formato de 4 letras y 2 números. Ejemplo: PLDE55") 
    while True:             
        tipo=input("¿Cuál es el tipo del vehículo?(S=sedan, C=Camioneta, M=Moto): ")
        if tipo.upper()=="S" or tipo.upper()=="C" or tipo.upper()=="M":
            break
        else:
            print("Ingrese una opción válida")
    VehículosLargo=list(Vehículos.keys())[-1]
    Vehículos[VehículosLargo+1]={
                                "Marca":marca,
                                "Año":año,
                                "Patente":patente,
                                "Tipo":tipo
                                }  
def actualizar_vehiculos():
    mostrar_vehiculos()
    vh=int(input("Ingrese que vehículo quiere actualizar"))
    while True:
        print(Vehículos[vh])
        print('''
            1.- Marca
            2.- Año
            3.- Patente 
            4.- Tipo      
            5.- Salir  
            ''')
        op2=int(input("Ingrese qué cambio quiere realizar: "))    
        match op2:
            case 1:
                marca=input("Ingrese la marca: ") 
                Vehículos[vh]["Marca"]=marca
            case 2:
                while True:
                    año=int(input("Ingrese el año: "))
                    laño=str(año)
                    if len(laño)==4:
                        break
                    else:
                        print("El año debe estar en formato de 4 numeros. Ejemplo: 2010") 
                Vehículos[vh]["Año"]=año
            case 3:
                while True:
                    patente=input("Ingrese la patente: ")
                    if len(patente)==6 and patente.isalnum()==True:
                        break
                    else:
                        print("La patente debe estar en formato de 4 letras y 2 números. Ejemplo: PLDE55") 
                Vehículos[vh]["Patente"]=patente
            case 4:
                while True:             
                    tipo=input("¿Cuál es el tipo del vehículo?(S=sedan, C=Camioneta, M=Moto): ")
                    if tipo.upper()=="S" or tipo.upper()=="C" or tipo.upper()=="M":
                        break
                    else:
                        print("Ingrese una opción válida")
                Vehículos[vh]["Tipo"]=tipo       
            case 5:
                break
            case _:
                print("Ingrese una opción válida") 
def borrar_vehiculos():
    borrados=int(0)
    mostrar_vehiculos()
    delete=int(input("¿Qué vehículo quiere eliminar?"))  
    del Vehículos[delete]
def mostrar_estadisticas():
    VL=list(Vehículos.keys())[-1]
    print(f'''
        Estadísticas:
        Vehículo agregado recientemente: 
        Cantidad de vehículos en garage: {VL} 
            ''')      
def menu_de_registro():
    while True:
        while True:
            try:
                print('''
    Ingrese la acción a realizar:
    1.- Ingresar vehículos
    2.- Mostrar vehiculos
    3.- Actualizar vehiculo
    4.- Borrar vehiculo
    5.- Mostrar estadisticas: ultimo vehiculo ingresado y total en garage
    6.- Salir
    ''')
                op=int(input())
                break
            except Exception as e:
                print(e)    
        match op:
            case 1:
                ingresar_vehiculos() 
            case 2:
                mostrar_vehiculos()
            case 3:
                actualizar_vehiculos()
            case 4:
                borrar_vehiculos()
            case 5:
                mostrar_estadisticas()                       
            case 6:
                print("Saliendo...")
                break
            case _:
                print("Ingrese una opción válida")
Vehículos={
    1:{
    "Marca":"Chevrolet",
    "Año":2020,
    "Patente":"JHPO80",
    "Tipo":"C"
    },
    2:{
    "Marca":"Suzuki",
    "Año":2023,
    "Patente":"DLUP22",
    "Tipo":"S" 
    }
}

menu_de_registro()