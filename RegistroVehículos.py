#Tarea
#Crear gestión de Vehiculos
#Crear programa para un parking de autos
#Se debe ingresar marca, año, patente y tipo
#Marca: Tipo string, debe typear la marca
#Año: Solo de 4 digitos enteros
#Patente: Debe tener 4 letras minusculas y 2 digitos
#Tipo: S=sedan, C=Camioneta, M=Moto
#Se debe validar cada aspecto y debe tener un mantenedor para todo los Vehiculos motorizados

#1.- Ingresar vehiculos
#2.- Mostrar vehiculos
#3.- Actualizar vehiculo
#4.- Borrar vehiculo
#5.- Mostrar estadisticas: ultimo vehiculo ingresado y total en garage
#6.- Salir

#Usar funciones con argumentos para poder validar y para poder llamar las acciones dentro del menú  

va=0
vb=0

def mostrar_vehiculos():
    for key,vehiculo in Vehiculos.items():
        print(key,".-",vehiculo)   
def mostrar_estadisticas():
    VL=list(Vehiculos.keys())[-1]
    print(f'''
        Estadísticas:
        Vehículo agregado recientemente: {VL}
        Cantidad de Vehiculos en garage: {2+(va-vb)} 
            ''')      

Vehiculos={
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

while True:
        while True:
            try:
                print('''
                Ingrese la acción a realizar:
                1.- Ingresar Vehiculos
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
                va+=1
                marca=input("Ingrese la marca: ")
                while True:
                    anio=int(input("Ingrese el año del vehículo"))
                    if len(str(anio))==4:
                        break
                    else:
                        print("El año debe estar en formato de 4 numeros. Ejemplo: 2010") 
                while True:
                    patente=input("Ingrese la patente: ")
                    cont_letras=0
                    cont_numeros=0
                    for l in patente:
                        if l.isalpha():
                            cont_letras+=1
                        elif l.isdigit():
                            cont_numeros+=1    
                    if len(patente)==6 and cont_letras==4 and cont_numeros==2:
                        break
                    else:
                        print("La patente debe estar en formato de 4 letras y 2 números. Ejemplo: PLDE55") 
                while True:             
                    tipo=input("¿Cuál es el tipo del vehículo?(S=sedan, C=Camioneta, M=Moto): ")
                    if tipo.upper()=="S" or tipo.upper()=="C" or tipo.upper()=="M":
                        break
                    else:
                        print("Ingrese una opción válida")
                VehiculosLargo=list(Vehiculos.keys())[-1]
                Vehiculos[VehiculosLargo+1]={
                                            "Marca":marca,
                                            "Año":anio,
                                            "Patente":patente,
                                            "Tipo":tipo
                                            }  
            case 2:
                mostrar_vehiculos() 
            case 3:
                mostrar_vehiculos()
                vh=int(input("Ingrese que vehículo quiere actualizar"))
                while True:
                    print(Vehiculos[vh])
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
                            Vehiculos[vh]["Marca"]=marca
                        case 2:
                            while True:
                                año=int(input("Ingrese el año: "))
                                if len(str(año))==4:
                                    break
                                else:
                                    print("El año debe estar en formato de 4 numeros. Ejemplo: 2010") 
                            Vehiculos[vh]["Año"]=anio
                        case 3:
                            while True:
                                patente=input("Ingrese la patente: ")
                                cont_letras=0
                                cont_numeros=0
                                for l in patente:
                                    if l.isalpha():
                                        cont_letras+=1
                                    elif l.isdigit():
                                        cont_numeros+=1    
                                if len(patente)==6 and cont_letras==4 and cont_numeros==2:
                                    break
                                else:
                                    print("La patente debe estar en formato de 4 letras y 2 números. Ejemplo: PLDE55") 
                            Vehiculos[vh]["Patente"]=patente
                        case 4:
                            while True:             
                                tipo=input("¿Cuál es el tipo del vehículo?(S=sedan, C=Camioneta, M=Moto): ")
                                if tipo.upper()=="S" or tipo.upper()=="C" or tipo.upper()=="M":
                                    break
                                else:
                                    print("Ingrese una opción válida")
                            Vehiculos[vh]["Tipo"]=tipo       
                        case 5:
                            break
                        case _:
                            print("Ingrese una opción válida")
            case 4:
                mostrar_vehiculos()
                delete=int(input("¿Qué vehículo quiere eliminar?"))  
                del Vehiculos[delete]
                vb+=1 
            case 5:
                mostrar_estadisticas()                     
            case 6:
                print("Saliendo...")
                break
            case _:
                print("Ingrese una opción válida")