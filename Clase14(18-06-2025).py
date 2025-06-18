#Maslistas

# productos=["Zapato"]
# precio=[20000]

prod_sports=[
    {"Nombre":"zapato","precio":20000},
    {"Nombre":"pelota","precio":24000}
]

print(prod_sports)

# prod_sports.insert({"Nombre":"paleta","precio":14000})

# print(prod_sports)

def mostrar_articulos(lista):
    for n,p in enumerate(lista):
        print(n+1,".-",p["Nombre"], "$", p["precio"])

def insertar(lista):
    nom=input("Ingrese el nombre del producto: ")
    pre=int(input("Ingrese el precio: "))
    lista.insert(0,{"Nombre":nom,"precio":pre})   

def actualizar(lista):
    mostrar_articulos(prod_sports)
    opc=int(input("Seleccione el producto a actualizar :"))
    print(prod_sports[opc-1])
    nn=input("Ingrese nuevo nombre: ")
    np=int(input("Ingrese nuevo precio: "))
    lista[opc-1]["Nombre"]=nn
    lista[opc-1]["precio"]=np
    print("Artículo actualizado")    

def borrar(lista):
    mostrar_articulos(prod_sports)
    opc=int(input("Seleccione el producto a borrar :"))
    prod_sports.pop(opc-1)                  

def menu(lista):

    while True:
        while True:
            try:
                print('''
            1.- Agregar productos
            2.- Mostrar productos
            3.- Actualizar producto      
            4.- Borrar producto              
            5.- Salir                    
                    ''')
                op=int(input())
                break    
            except Exception:
                print("Solo ingresar números enteros")
        match op:
            case 1:
                insertar(lista)
            case 2:
                mostrar_articulos(lista)
            case 3:
                actualizar(lista)
            case 4:
                borrar(lista)
            case 5:
                break    
            case _:
                print("Opción inválida")

# menu(prod_sports)         

#-----------------------------------------------------------------------#

#Crear programa CRUD del siguiente diccionario.

personas={
    1:{"Nombre":"Diego Rivera",
       "Numero": [7565434,9783423],
       "Estado civil": "casado",
       "Trabajando":True,
       "Edad": 64},
    2:{"Nombre":"Alberto Paredes",
       "Numero": [5230583,3896452],
       "Estado civil": "soltero",
       "Trabajando":True,
       "Edad": 30},
    3:{"Nombre":"Camila Araneda",
       "Numero": [5088234,1856340],
       "Estado civil": "casado",
       "Trabajando":True,
       "Edad": 28}

}

while True:
    while True:
        try:
            print('''
            Sistema...
            1.- Ingresar persona
            2.- Mostrar listado
            3.- Actualizar persona
            4.- Borrar persona     
            5.- Salir                         
                ''')
            op=int(input())
            break
        except Exception as e:
            print("El error es:",e)
    match op:
        case 1:
            nombre=input("Ingrese el nombre")
            numero=int(input("Ingrese el numero de telefono"))
            est=int(input("Estado civil 1.-Casado, 2.-Soltero"))
            if est==1:
                estCivil="Casado"
            else:
                estCivil="Soltero"
            edad=int(input("Ingrese la edad"))    
            nextkey=len(personas)
            personas[nextkey+1]={"Nombre":nombre,
            "Numero": [numero],
            "Estado civil": estCivil,
            "Trabajando":True,
            "Edad": edad}
        case 2:
            for persona, val in personas.items():
                print(persona,".-",val) 
        case 3:
            print("¿Cuál persona va a actualizar?")
            for persona,val in personas.items():
                print(persona,".-",val) 
            per=int(input()) 
            #Falta por completar esta sección
        case 4:
            print("¿Cuál persona va a borrar?")
            for persona,val in personas.items():
                print(persona,".-",val) 
            per=int(input())               
            personas.pop(per-1)    
        case 5:
            print("Saliendo...")
            break
        case _:
            print("Ingrese una opción válida")
