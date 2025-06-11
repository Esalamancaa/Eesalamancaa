# #Listas 
# #Una lista es conjunto de datos

# #Uso y ejemplos de listas

# #index(-)-6,-5,-4,-3,-2,-1
# numeros=[ 2, 5, 8, 77,6, 7.9]
# #index(+) 0, 1, 2, 3, 4, 5

#---------------------------------------------------------------------------#

# print (round(numeros[3]))

# # for numero in numeros:
# #     print("Numero x 2", numero*2)

#---------------------------------------------------------------------------#
    
# nombres=["Felipe", "Curly", "Larry", "Moe"]

# print(nombres)

# nombres.append("Luthien")

# print(nombres)

#---------------------------------------------------------------------------#

# #Programa de ingreso datos a listas

# import os

# while True:
#     print('''
#     1.-Ingresar nombre
#     2.- Salir
#           ''')
#     op=int(input())
#     os.system('cls')
#     match op:
#         case 1:
#             print("Ingrese el nombre")     
#             n1=input()
#             os.system('cls')
#             nombres=[]
#             nombres.append(n1)
#         case 2:
#             print(nombres)
#             break    
#         case _:
#             print("No es una opción válida")

#---------------------------------------------------------------------------#

# #VerProfe
# nombres=["Christopher", "Edward", "John", "Hanz"]
# apellidos=["Nolan", "Norton", "Williams", "Zimmer"]

# while True:
#     print('''
#         1.- Ingresar nombre y apellidos
#         2.- Mostrar nombres y apellidos
#         3.- Buscar nombre
#         4.- Salir   
#         ''')
#     op=int(input())
#     match op:
#         case 1:
#             nom=input("Ingrese un nombre: ")
#             nombres.append(nom)
#             ap=input("Ingrese un apellido: ")
#             apellidos.append(ap)  
#         case 2:
#             for i in nombres:
#                 c=0
#                 print(nombres[c],apellidos[c])
#                 c+=1
#         case 3:
#             busca=input("Indique qué nombre buscará: ")
#             if busca in nombres:
#                 print(f"El nombre {busca} está en la lista")
#             else: 
#                 print(f"El nombre {busca} no está en la lista")
#         case 4:
#             break
#         case _:
#             print("Opción inválida")    

#---------------------------------------------------------------------------#

#Carrito de compras con listas

#Seleccionar una opción
#1. Agregar productos(Nombre producto y precio)
#2. Comprar(Submenú mostrando productos y precios)
#3. Crear boleta
#4. Salir
productos=[]
precio=[]
carrito=[]
total=0

while True:
    print("Sistema de supermercado")
    print('''
    Ingrese una opción:
    1.- Agregar productos
    2.- Comprar 
    3.- Crear boleta
    4.- Salir
        ''')
    op=int(input())
    match op:
        case 1:
            print("Ingrese el producto y el precio")
            pro=input("Ingrese el producto: ")
            productos.append(pro)
            pre=int(input("Ingrese el precio: "))
            precio.append(pre)
        case 2:
            p=0
            n=1
            print("¿Qué producto va a comprar?")   
            for i in range(len(productos)):
                  #len es para el largo de la lista
                  print(f"{n}.-{productos[p]} ${precio[p]}")
                  p+=1
                  n+=1
            print("0.Salir")      
            op=int(input())
            carrito.append(op-1)
            print("Los productos que lleva son")
            for i in carrito:
                print(productos[i])
        case 3:
            print(f"Su total es de ${total}")
            print(f"Su total + IVA es de ${total*1.19}")    
        case 4:
            print("Saliendo del sistema...")
            break