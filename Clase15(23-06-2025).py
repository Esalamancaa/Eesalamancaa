# #Repaso pre prueba


# #Validaciones

# #Validar si un texto tiene por lo menos 3 numeros

# texto="DarkLink128"
# can_num=0

# for p in texto:
#     if p.isdigit():
#         print("Es digito")
#         can_num+=1
# if can_num>=3:
#     print("La palabra cumple con el parametro")        

#--------------------------------------------------------------------#

# anio=1985

# print(len(str(anio)))

# if len(str(anio))==4:
#     print("Tiene largo de 4")

#--------------------------------------------------------------------#    

# #Creación de contraseñas
# #Debe tener tres mayusculas, una minuscula y 3 numeros

# cont_mayus=0
# cont_minus=0
# cont_digit=0

# while True:
#     pw=input("Ingrese una contraseña. Debe contener 3 mayusculas, 1 minuscula y 3 numeros :")
#     for p in pw:
#         if p.isupper():
#             cont_mayus+=1
#         elif p.islower():
#             cont_minus+=1
#         elif p.isdigit():
#             cont_digit+=1
#     if cont_mayus==3 and cont_minus==1 and cont_digit==3:
#         print("La contraseña cumple con los parametros")
#         break
#     elif cont_mayus>=3 or cont_minus>=1 or cont_digit>=3:
#         print(f"Sobra(n){cont_mayus-3} mayuscula(s),{cont_minus-3} minuscula(s) y {cont_digit-3} numero(s)")
#     else:
#         print(f"Falta(n){3-cont_mayus} mayuscula(s),{1-cont_minus} minuscula(s) y {3-cont_digit} numero(s)")    

#--------------------------------------------------------------------#    

# #Creación de contraseñas - VerProfe

def valida_pass(password):
        cont_mayus=0
        cont_minus=0
        cont_digit=0
        cont_gato=False
        password=input("Ingrese su contraseña")

        for l in password:
            if l.isupper():
                cont_mayus+=1
            if l.islower():
                cont_minus+=1
            if l.isdigit():
                cont_digit+=1        
            if l=="#":
                cont_gato=True
        if cont_mayus<3:
            print("Debe tener al menos 3 letras en mayusculas")
        elif cont_minus<1:
            print("Debe tener al menos 1 letra en minuscula")
        elif cont_digit<3:
            print("Debe tener al menos 3 numeros")
        elif cont_gato==False:
            print("Debe tener incluir un '#'")        
        else:
            print("Contraseña creada")
            return True
pp=False        
while pp!=True:
    clave=input("Ingrese su contraseña")

    pp=valida_pass(clave)

#--------------------------------------------------------------------#    

#IngresoDeProductos

#Diccionario de productos
#Valida ('AAii2020')
#code debe tener 2 mayusculas, 2 minusculas y 4 numeros
#Nombre debe tener 2 palabras
#Precio debe tener entre 8000 y 10000

prods={
    1:{"nombre":"Zelda TOTK",
        "precio":80000,
        "code":"ZZkk1985"
    },
    2:{"nombre":"Elden Ring",
        "precio":45000,
        "code":"EErr2021"  
    }

}

