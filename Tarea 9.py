# Programación Avanzada - Tarea No. 9
# Luis Manuel Velásquez González 1502325

#Cine Fácil
precio=20
reservas=[]
horario=[
    {"Fecha":"31/07/2025", "Hora": "14:00"},
    {"Fecha":"31/07/2025", "Hora": "18:00"},
    {"Fecha":"01/08/2025", "Hora": "12:00"},
    {"Fecha":"01/08/2025", "Hora": "19:00"},
]

def comprobacion(dato):
    while dato=="":
        print("Dato no válido")
        dato=input("Ingresa el dato de nuevo: ").strip().lower()
    return(dato)

def crear_reserva():
    nombre=input("Ingresa tu nombre: ").strip().lower()
    nombre=comprobacion(nombre)

    pelicula=input("Ingresa que película deseas ver: ").strip().lower()
    pelicula=comprobacion(pelicula)

    boletos=int(input("Ingresa la cantidad de boletos a comprar: "))
    while boletos <=0:
        print("Número de boletos no válido")
        boletos=int(input("Ingrese de nuevo: "))

    print("Selecciona una de las funciones disponibles")
    i=1
    for funciones in horario:
        print(f"{i}. Función a las {funciones["Hora"]} horas, del {funciones["Fecha"]}")
        i+=1
    seleccion=int(input("Ingresa la opcion: "))
    while seleccion>len(horario)+1 or seleccion<0:
        print("Función no válida")
        seleccion=int(input("Ingresa de nuevo: "))
    tiempo=horario[seleccion-1]

    reserva={
        "nombre":nombre,
        "pelicula":pelicula,
        "boletos":boletos,
        "tiempo":tiempo
    }
    reservas.append(reserva)

    print("-\nReserva Guardada-")
    print(f"{reserva['nombre'].title()} compró {reserva['boletos']} para la película de {reserva['pelicula'].title()}")
    print(f"para el {reserva['tiempo']["Fecha"]} a las {reserva['tiempo']["Hora"]}")
    print(f"Dejando un total de Q{reserva['boletos']*precio}")

def ver_reservas():
    i=1
    for r in reservas:
        print(); print(f"{1}. Nombre: {r["nombre"].title()} | Boletos comprados: {r["boletos"]} | Película: {r["pelicula"].title()}")
        print(f"   Fecha: {r['tiempo']["Fecha"]} | Hora: {r['tiempo']["Hora"]} | Total: Q{r["boletos"]*precio}")
        i+=1

def cambiar_precio():
    precio=int(input("Ingresa el nuevo precio: "))
    while precio<0:
        print("Precio no válido")
        precio=int(input("Ingresa el nuevo precio: "))

def ingreso_horario():
    fecha=input("Ingresa la fecha en formato dd/mm/aa:").strip().lower()
    fecha=comprobacion(fecha)
    hora=input("Ingresa la hora en formato hh/mm (24 horas): ").strip().lower()
    hora=comprobacion(hora)
    nuevo_horario={
        "Fecha":fecha,
        "Hora":hora
    }
    horario.append(nuevo_horario)
    print("Horario Agregado de forma exitosa")

while True:
    print("\nBienvenido a CineFácil")
    print("1. Crear una reserva")
    print("2. Ver reservas hechas")
    print("3. Cambiar precio de boletos")
    print("4. Agregar nuevo horario")
    print("5. Salir")
    opcion=input("Ingresa una opción: ")

    if opcion=="1":
        print("\nBienvenido, crearemos unar reserva")
        crear_reserva()
    elif opcion=="2":
        print("\nBienvenido, estas son las reservas")
        ver_reservas()
    elif opcion=="3":
        print("\nCambio de precio de boleto")       #Funciones extra
        cambiar_precio()
    elif opcion=="4":
        print("\nIngresa un nuevo horario")         #Funciones extra
        ingreso_horario()
    elif opcion=="5":
        print("\nGracias por preferi Cine Fácil, el mejor cine")
        break
    else:
        print("\nOpción equivocada")