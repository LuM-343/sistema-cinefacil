# sistema-cinefacil

-Descripción Sistema Cinefacil

El sistema Cine facil es una herramienta que se pone a disposición de todos los cines, para poder controlar las reservas, funciones, horarios, precios y boletos. Ofreciendo lo necesario para que puedan gestionar estos de la mejor manera


-Funciones del Programa
    
    -Comprobacion(dato)

        Función que se encarga de revisar que el dato str que se le da, no este vacio y si por algun motivo esta vacio, pide de nuevo el dato hasta que este sea válido. Devuelve el dato válido


    -Crear_reserva()

        Función encargada de recopilar los datos para crear nueva reserva, agregando los datos a un diccionario para después hacer un append a la base de datos


    -Ver_reservas()

        Función simple que se encarga de, con un for, mostrar todas las reservas ya realizadas de una forma un poco estética.


    -cambiar_precio()

        Función que cambia el nuevo precio y se encarga de revisar que este sea válido


    -ingres_horario()

        Función para agregar un nuevo horario a los ya predefinidos, recopilando hora y fecha, para despues agregarlo con un append

-¿Qué hiciste en la nueva rama y cómo hiciste el merge?

En la nueva rama subi las opciones de cambiar precio de boleto y agregar horario, que se incorporaron después. y el merge lo realicé de la siguiente manera.
-Cambie a la rama principal(master) con (git checkout master)
-Ejecute este comando en la terminal (git merge funciones_extra)
-Subí los cambios a github


-¿Qué aprendiste sobre Git y GitHub?

Antes no sabía nada sobre git y github solo lo había usado muy por encima, ahora he aprendido como funciona el control de versiones, como llevar un mejor control de los cambios y actualizaciones que sufren los códigos, como funcionan las ramas (branch) y además tambien entendi un poco mejor como ya en proyectos reales utilizan estas herramientas.