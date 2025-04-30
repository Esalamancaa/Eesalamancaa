import time

#Usuarios
user1="carlos" ; user2="juan" ; user3="jaime"
#Contraseñas
c1=9053 ; c2=6700 ; c3=2965
#Saldo
s1=80000 ; s2=20000 ; s3=50000
#Contador inicial de intentos
intentos=2
#Cajas de billetes
cj1=30 ; cj2=30 ; cj3=30 
#Inicio de programa
user=input("Ingrese su usuario :")

#Validación de datos ingresados
if user.lower()==user1 or user2 or user3:
    if user==user1:
        cc=int(input("Ingrese la contraseña :"))
        saldo=s1
        while cc!=c1 and intentos>0:
            intentos-=1
            print(f"Clave incorrecta, intente nuevamente. Tiene {intentos+1} intentos")
            cc=int(input("Ingrese la contraseña :"))
            if intentos==0:
                print("Numero de intentos excedido, la cuenta se ha bloqueado.")
    elif user==user2:
        cc=int(input("Ingrese la contraseña :"))
        saldo=s2  
        while cc!=c2 and intentos>0:
            intentos-=1
            print(f"Clave incorrecta, intente nuevamente. Tiene {intentos+1} intentos")
            cc=int(input("Ingrese la contraseña :"))
            if intentos==0:
                print("Numero de intentos excedido, la cuenta se ha bloqueado.")
    elif user==user3:
        cc=int(input("Ingrese la contraseña :"))
        saldo=s3
        while cc!=c3 and intentos>0:
            intentos-=1
            print(f"Clave incorrecta, intente nuevamente. Tiene {intentos+1} intentos")
            cc=int(input("Ingrese la contraseña :"))
            if intentos==0:
                print("Numero de intentos excedido, la cuenta se ha bloqueado.")
    else:
            print(f"No existe el usuario {user}")               
             
time.sleep(1)

#Retiro de dinero
print('''
BIENVENIDO      
    ¿Cuanto va a retirar?  
    1.- $5000    2.- $10000
    3.- $20000   4.- Salir 
    ''')                            
op=int(input())

#Validación de elección y disponibilidad de billetes
while op!=4:
    if op==1:
        if cj1>0 and saldo>=5000:
            cj2-=1 ; saldo-=5000
            print(f"Se retirarán $5000 de su saldo. Su saldo disponible es {saldo}")
            op=int(input('''
                ¿Desea realizar otro retiro?  
                1.- $5000    2.- $10000
                3.- $20000   4.- Salir 
                  '''))
        else:
            op=int(input("Este cajero se ha quedado sin billetes de $5000 o no tiene suficiente saldo. Ingrese otra opción :"))
    elif op==2:
        if cj2>0 and saldo>=10000:
            cj2-=1 ; saldo-=10000
            print(f"Se retirarán $10000 de su saldo. Su saldo disponible es {saldo}")
            op=int(input('''
                ¿Desea realizar otro retiro?  
                1.- $5000    2.- $10000
                3.- $20000   4.- Salir 
                  '''))
        else:  
            op=int(input("Este cajero se ha quedado sin billetes de $10000 o no tiene suficiente saldo. Ingrese otra opción :"))  
    elif op==3:
        if cj3>0 and saldo>=20000:
            cj3-=1 ; saldo-=20000
            print(f"Se retirarán $20000 de su saldo. Su saldo disponible es {saldo}")
            op=int(input('''
                ¿Desea realizar otro retiro?  
                1.- $5000    2.- $10000
                3.- $20000   4.- Salir 
                  '''))
        else:
            op=int(input("Este cajero se ha quedado sin billetes de $20000 o no tiene suficiente saldo. Ingrese otra opción :"))            
    elif op==4:
        print("No se ha realizado ninguna operación. saliendo...")   
    else:
        op=int(input("Ingrese una opción válida para continuar :"))    