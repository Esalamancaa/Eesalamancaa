personas=[
    {"nombre": "Diego Robles",
     "numero": 79823432,
     "Casado": True
    },
    {"nombre": "John Snow",
     "numero": 74825552,
     "Casado": True
    },
    {"nombre": "Pedro Pascual",
     "numero": 29007582,
     "Casado": False
    }
    ]
    
print(personas[2]["numero"])

for key, value in personas.items():
    print(key, value)

print(personas["nombre"])   

#------------------------------------------------------------------#

text=input("Ingrese un texto: ")

pala=input("Ingrese la palabra que quiere buscar")