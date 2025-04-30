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
print("Ingrese su usuario :")
user=input()

#Validación de datos ingresados
if user.lower()==user1 or user2 or user3:
    if user==user1:
        saldo=s1 ; cr=c1
    elif user==user2:
        saldo=s2 ; cr=c2
    elif user==user3:
        saldo=s3 ; cr=c3
    else:
        user=int(input("Ingrese un usuario válido :"))   
cc=int(input("Ingrese la contraseña :"))
while cc!=cr and intentos>0:
    intentos-=1
    print(f"Clave incorrecta, intente nuevamente. Tiene {intentos+1} intentos")
    cc=int(input("Ingrese la contraseña :"))
    if intentos==0:
        print("Numero de intentos excedido, la cuenta se ha bloqueado.")
             
time.sleep(1)

#Retiro de dinero
op=int(input('''
BIENVENIDO      
    ¿Cuanto va a retirar?  
    1.- $5000    2.- $10000
    3.- $20000   4.- Salir 
    '''))                            

#Validación de elección y disponibilidad de billetes

if op==1:
    cj=cj1
    retiro=5000
elif op==2:
    cj=cj2
    retiro=10000
elif op==3:
    cj=cj3
    retiro=20000
elif op==4:
    print("Saliendo...")   
else:
    op=int(input("Ingrese una opción válida para continuar :")) 
while op!=4:
    if cj>0 and saldo>=20000:
        cj-=1
        saldo-=retiro
        print(f"Se retirarán $20000 de su saldo. Su saldo disponible es {saldo}")
        op=int(input('''
    ¿Desea realizar otro retiro?  
    1.- $5000    2.- $10000
    3.- $20000   4.- Salir 
    '''))
    else:
        op=int(input("Este cajero se ha quedado sin billetes de $20000 o no tiene suficiente saldo. Ingrese otra opción :"))           