#Funciones:Uso y ejemplos 

# def suma_print():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(n1+n2)

# # suma_print()   

# def resta(n1,n2):
#     print(n1-n2) 

# num1=int(input("Ingrese un numero: "))
# num2=int(input("Ingrese otro numero: "))
# resta(num1,num2)   

#-------------------------------------------------------------------------------#
#Calculadora

def calculadora():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print("Suma:", n1+n2)
    print("Resta:", n1-n2)
    print("Multiplicación:", n1*n2)
    print("División:", n1/n2)

# calculadora()   

#-------------------------------------------------------------------------------#
#Calculadora2

def suma():
    print(n1+n2)
def resta():
    print(n1-n2)
def multiplicacion():
    print(n1*n2)
def division():
    print(n1/n2)    

# n1=int(input("Ingrese un numero: "))
# n2=int(input("Ingrese otro numero: "))
# suma()
# resta()
# multiplicacion()
# division()

#-------------------------------------------------------------------------------#

def suma_return():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    return (n1+n2)

# veri=(suma_return())
# print(veri)

#-------------------------------------------------------------------------------#

def promedio(x,y,z):
    return (x+y+z)/3

# if promedio(40,70,22) > 40:
#     print("El alumno aprobó")
# else:
#     print("El alumno reprobó")

#-------------------------------------------------------------------------------#

#Crear un programa para calcular un descuento
#Pedir al usuario el precio y el descuento a aplicar
#Mostrar los resultados

def descuentos(precio, porcentaje): 
    return precio*(porcentaje/100)  

# precio=int(input("Ingrese el precio del producto: "))
# porcentaje=int(input("Ingrese el porcentaje del descuento: "))

# print("El descuento es: ",descuentos(precio,porcentaje))
# print("El precio total es: ",precio-descuentos(precio,porcentaje))


def IVA():
    IVA=(precio/100)*19
    print("El IVA de su producto es:",IVA)
    
# print("Ingrese el precio para saber su IVA: ")  
# precio=int(input()) 
# IVA()  

#-------------------------------------------------------------------------------#

# productos=["Zapato"]
# precio=[20000]

list_prod=[
    {"Nombre":"zapato","precio":20000},
    {"Nombre":"pelota","precio":24000}
]

print(list_prod)

# list_prod.insert({"Nombre":"paleta","precio":14000})

# print(list_prod)

while True:
    while True:
        try:
            print('''
        1.- Agregar productos
        2.- Mostrar productos
        3.- Actualizar producto          
        4.- Salir                    
                ''')
            op=int(input())
            break    
        except Exception:
            print("Solo ingresar números enteros")

    match op:
        case 1:
            nom=input("Ingrese el nombre del producto: ")
            pre=int(input("Ingrese el precio: "))
            list_prod.insert({"Nombre":nom,"precio":pre})
        case 2:
            for p in list_prod:
                print(p)
        case 3:
            for n,p in enumerate(list_prod):
                print(n+1,".-",p)
            opc=int(input("Seleccione el producto a actualizar :"))
            print(list_prod[opc-1])
            nn=input("Ingrese nuevo nombre: ")
            np=int(input("Ingrese nuevo precio: "))
            list_prod[opc-1]["Nombre"]=nn
            list_prod[opc-1]["precio"]=np
            print("Artículo actualizado")
        case _:
            print("Opción inválida")

