import time

#Usuarios
user1="carlos"
user2="juan"
user3="jaime"
#Contraseñas
c1=9053
c2=6700
c3=2965
#Saldo
s1=80000
s2=20000
s3=50000
#Contador inicial de intentos
intentos=2
#Cajas de billetes
cj1=30 #$5000
cj2=30 #10000
cj3=30 #20000
#Inicio de programa
print("Ingrese su usuario :")
user=input()

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
        if cj1>0:
            print("Se retirarán $5000 de su saldo")
            cj2-=1
            saldo-=5000
            print(f"Su saldo disponible es {saldo}")
            print('''
                ¿Cuanto más va a retirar?  
                1.- $5000    2.- $10000
                3.- $20000   4.- Salir 
                  ''')
            op=int(input())
        else:
            print("Este cajero se ha quedado sin billetes de $10000") 
    elif op==2:
        if cj2>0:
            print("Se retirarán $10000 de su saldo")
            cj2-=1
            saldo-=10000
            print(f"Su saldo disponible es {saldo}")
            print('''
                ¿Cuanto más va a retirar?  
                1.- $5000    2.- $10000
                3.- $20000   4.- Salir 
                  ''')
            op=int(input())
        else:
            print("Este cajero se ha quedado sin billetes de $10000")    
    elif op==3:
        if cj3>0:
            print("Se retirarán $20000 de su saldo")
            cj3-=1
            saldo-=s3
            print(f"Su saldo disponible es {saldo}")
            print('''
                ¿Cuanto más va a retirar?  
                1.- $5000    2.- $10000
                3.- $20000   4.- Salir 
                  ''')
            op=int(input())
        else:
            print("Este cajero se ha quedado sin billetes de $10000")               
    elif op==4:
        print("No se ha realizado ninguna operación. saliendo...")   
 