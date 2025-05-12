#Funciones

# def suma():
#     n1=int(input("Ingrese un número :"))
#     n2=int(input("Ingrese otro número :"))
#     print("La suma es ", n1+n2)

# suma()    

#------------------------------------------------------#

# op=int(input("Seleccione una opción :"))

# while True:
#     op=int(input("Seleccione una opción :"))
#     match op:
#         case 1:
#             print("Opción 1")
#         case 2:
#             print("Opción 2")
#         case 3:
#             print("Opción 3")
#         case 4:
#             print("Saliendo")
#             break   
#         case _:
#             print("Opción inválida")

#------------------------------------------------------#
def suma():
    n1=int(input("Ingrese el primer número :"))
    n2=int(input("Ingrese el segundo número :"))
    print("El resultado de la suma es", n1+n2)

def resta():
    n1=int(input("Ingrese el primer número :"))
    n2=int(input("Ingrese el segundo número :"))
    print("El resultado de la suma es", n1-n2) 

def multiplicación():
    n1=int(input("Ingrese el primer número :"))
    n2=int(input("Ingrese el segundo número :"))
    print("El resultado de la suma es", n1*n2)       

def división():
    n1=int(input("Ingrese el primer número :"))
    n2=int(input("Ingrese el segundo número :"))
    try:
        print("El resultado de la división es", n1/n2) 
    except ZeroDivisionError:    
        print("La división por cero no está permitida")    


def calcu():
    while True: 
        print('''
        ¿Que operación desea realizar? 
        1.- Sumar             2.- Restar
        3.- Multiplicación    4.- División
        5.- Salir
        ''')
        op=int(input())
        match op:
            case 1: 
                suma()
            case 2:
                resta()
            case 3:
                multiplicación()
            case 4:
                división()
            case 5:
                print("Saliendo")
                break                

calcu()

#------------------------------------------------------#

#Tarea
#Realizar un programa que incluya "match" y llame a otras 3 funciones.
#Estas funciones deben incluir if, else, for y/o while.
#El programa debe ser recursivo.