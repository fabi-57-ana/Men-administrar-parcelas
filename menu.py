
while True:
    menu = input("""
________________________________________________
|  Hola! Gracias por utilizar el sistema de    |
|              AgroTech Coop.                  |
|_____Seleccione un numero del 1 al 5._________|
|______________________________________________|
[1] Gestionar Parcela
[2] Gestionar Sensores
[3] Registrar Mediciones
[4] Consultar Datos
[5] Salir del Sistema
_______________________________________________
_______HAGA CLICK ABAJO PARA CONTINUAR_________
_______________________________________________
""")
    if menu == '1':
        while True:
            sub_menu = input("""
_______Gestionar Parcela_______
Seleccione un numero del 1 al 5.
_______________________________
[1] Ver Parcela
[2] Agregar Parcela
[3] Modificar Parcela
[4] Eliminar Parcela
[5] Volver a Menu Principal
_______________________________
""")
            if sub_menu == '1':
                print("_________Parcelas Registradas________")
                print("Parcela 1: Campo Norte - Soja (10 ha)")
                print("Parcela 2: Campo Sur - Maíz (7 ha)")
            elif sub_menu == '2':
                print("___________Agregar Parcela___________")
                print("Parcela 3 - Campo Este - Trigo (5 ha)")
            
            elif sub_menu == '3':
                print("___________Modificar Parcela___________")
                print("Cambiar 'Soja' a 'Girasol' en Parcela 1")
            
            elif sub_menu == '4':
                print("__Eliminar Parcela__")
                print("Eliminar 'Parcela 2'")
            elif sub_menu == '5':
                break  
            else:
                print("Opción no válida")
    elif menu == '2':
        while True:
            sub_menu = input("""
____Gestionar Sensores_____
Seleccione un numero del 1 al 3.
___________________________
[1] Ver Sensores
[2] Agregar Sensores
[3] Volver a Menu Principal
___________________________
""")
            if sub_menu == '1':
                print("__________Ver Sensores__________")
                print("Sensor 1: Termómetro - Parcela 1")
                print("Sensor 2: Higrómetro - Parcela 2")
            
            elif sub_menu == '2':
                print("_______Agregar Sensor_________")
                print("Sensor 3 -    PH   - Parcela 1")
            
            elif sub_menu == '3':
                break  
            else:
                print("Opción no válida")
    elif menu == '3':
        while True:
            sub_menu = input("""
____Registrar Mediciones_____
Seleccione un numero del 1 al 2.
___________________________
[1] Registrar Mediciones
[2] Volver a Menu Principal
___________________________
""")
            if sub_menu == '1':
                print("Sensor 1 - 25.5 C - 10/05/2024")
            elif sub_menu == '2':
                break 
            else:
                print("Opción no válida")
    elif menu == '4':
        while True:
            sub_menu = input("""
_______Consultar Datos_________
Seleccione un numero del 1 al 3.
_______________________________
[1] Ver Todas las Mediciones
[2] Ver Mediciones por Sensor
[3] Volver a Menu Principal
_______________________________
""")
            if sub_menu == '1':
                print("____ Todas las Mediciones____")
                print("Sensor 1: 25.5 C - 10/05/2024")
                print("Sensor 2: 60% - 09/05/2024")
            elif sub_menu == '2':
                print("_____Mediciones por Sensor____")
                print("Sensor 1 - 25.5 C (10/05), 26.0 C (11/05)")
            elif sub_menu == '3':
                break 
            else:
                print("Opción no válida")
    elif menu == '5':
        print("Salir del sistema")
        break
    else:
        print("Error: Intente nuevamente.")


