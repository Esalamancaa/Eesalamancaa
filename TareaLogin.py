#Hacer un sistema de login
#Debe verificar si el usuario existe.De existir, le pregunta la contraseña
#Solo 3 oportunidades para acertar
#El diccionario debe estar previamente escrito antes de iniciar el sistema

import time
import os
intentos=3
usuarios={"Edgar":6700,
     "Alfredo":8540
    }  

print("Sistema de login")
time.sleep(2)
enter=input("Ingrese enter para continuar")
os.system('cls')

while True:
    print("Ingrese su nombre de usuario")
    user=input()
    os.system("cls")
    if user in usuarios:
        while True:
            try:
                print("Ingrese su contraseña")
                passwd=int(input())
                os.system('cls')
                if usuarios[user] == passwd:
                    print(f"Bienvenido al sistema, {user}")
                    break
                else:
                    intentos-=1
                    print(f"No es la contraseña, intente de nuevo.{intentos} Intento(s) restante(s)")
                    passwd=int(input())
                    if intentos==0:
                        print("Se han acabado los intentos")
                        break
            except Exception:
                print("Solo puede ingresar numeros enteros")
        break        
    else:
        print("El usuario es incorrecto o no existe, vuelva a intentar")             
       
