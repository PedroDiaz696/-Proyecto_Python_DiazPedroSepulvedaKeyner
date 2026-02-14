#git push origin main "subir los cambios a la nube"


import json

with open("registros_campers_350.json", "r", encoding="utf-8") as archivo: #open = abre el archivo #,"r", para read/leer #"utf-8" = para que no falle con tildes #"as archivo" variable que representa el archivo #with abre el archivo y lo cierra automaticamente
    campers = json.load(archivo) #json.load() sirve para que pase el archivo json a python

print(len(campers))


def menuRegistro():
    print("--------------------------")
    print("------- REGISTRATE -------")
    print("--------------------------")
    print("1. Camper")
    print("2. Trainer")
    print("3. Coordinador")
    opcionRegistro = int(input(": "))
    if opcionRegistro == 1:
        registroCamper()

def registroCamper():
        print("--- Bienvenido Camper ---")
        print("Que quieres hacer? : ")
        print("1. Ver estado de usuario")
        print("2. Solicitar inscribirse")
        print("3. ver lista de campers")
        opcionCamper = int(input(": "))
        if opcionCamper == 3:
             print(campers[0]["nombre"])




menuRegistro()



