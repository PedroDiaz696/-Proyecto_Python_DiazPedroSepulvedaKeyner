def registrarExamenInicial():
    id_buscar = input("ID del camper: ")

    for camper in campers:
        if camper["id"] == id_buscar:
            teoria = float(input("Nota teorica: "))

            practica = float(input("Nota practica: "))

            promedio = (teoria + practica) / 2

            if promedio >= 60:
                    camper["estado"] = "Aprobado"
                    print("Camper aprobado")
            else:
                    print("Camper no aprobado")
            return
            
            print("Camper no encontrado")