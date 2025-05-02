#Poner listado de 3 productos por categoria, las cat son 1,2 y 3
#Clasificar segun categoria y precio
#Cat 1 +200, cat 2 +400, cat 3 +600
#Precios: 1000 y menos, 3%; entre 1001 y 5000, 5% ; 5001 y más, 6%
#Agregar los impuestos segun la categoria  
#Luego aplicar descuento al total de la boleta según el monto

import time
pct=0


print('''
      Bienvenido(a), elija una categoría :"
      1.- Conservas
      2.- Granos envasados
      3.- Jugos
      4.- Salir    
      ''')
op=int(input())


if op==1:
    print('''
        Conservas
        1.- Jurel en lata $1800
        2.- Duraznos en almíbar $1500
        3.- Champiñones laminados $2000   
        0.- Salir     
          ''')
    op2=int(input())
    while op2!=0:
        if op2==1:
            print("Ha elegido jurel en Lata")
            pct+=(1800+200)*0.95
        elif op2==2:
            print("Ha elegido duraznos en almíbar")
            pct+=(1500+200)*0.95
        elif op2==3:
            print("Ha elegido champiñones laminados")
            pct+=(2000+200)*0.95 
        elif op2==0:
            print("Saliendo...")    
        else:
            op2=int("Elija una opción válida")
        op2=int(input())
elif op==2:
    print('''
        Granos envasados
        1.- 1kg de arroz $2000
        2.- 1kg de lentejas $2600
        3.- 1kg de porotos blancos $3000
        0.- Salir     
          ''')
    op2=int(input())
    while op2!=0:
        if op2==1:
            print("Ha elegido 1kg de arroz")
            pct+=(2000+400)*0.95
        elif op2==2:
            print("Ha elegido 1kg de lentejas")
            pct+=(2600+400)*0.95
        elif op2==3:
            print("Ha elegido 1kg de porotos blancos")
            pct+=(3000+400)*0.95 
        else:
            op2=int(print("Elija una opción válida"))
        op2=int(input())
elif op==3:
    print('''
        Granos envasados
        1.- 2u caja de jugo $550
        2.- 1lt botella jugo de naranja $1900
        3.- 1lt jugo natural orgánico $7300
        0.- Salir     
          ''')
    op=int(input())
    while op2!=0:
        if op2==1:
            print("Ha elegido 2u caja de jugo")
            pct+=(550+600)*0.95
        elif op2==2:
            print("Ha elegido 1lt botella jugo de naranja")
            pct+=(1900+400)*0.95
        elif op2==3:
            print("Ha elegido 1lt jugo natural orgánico")
            pct+=(7300+400)*0.95 
        else:
            op2=int(print("Elija una opción válida"))
        op2=int(input())
elif op==4:
    print("Saliendo de la selección")
time.sleep(1)

print("El total de su compra es: ", pct)
print("El total + IVA es de: ", pct*1.19)