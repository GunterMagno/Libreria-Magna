def par(numero) -> bool:
    if numero % 2 == 0:
        return True
    elif numero % 2 == 1:
        return False


def comprobar_negativo(numero:str) -> str:
    if numero.startswith("-"):
        print("El numero es negativo intenta de nuevo: ")
        return None


def comprobar_negativo(numero:str) -> str:
    if numero.startswith("-"):
        numero = numero[1:]
        return numero
    

def comprobar_numero(numero) -> bool:
    try:
        float(numero)
    except ValueError:
        print("*Error*, intenta de nuevo.")
        return False
    return True
    

def elegir_opcion_menu() -> int:
    
    opcion = None

    while opcion is None:
        mostrar_menu()

        try:
            opcion = int(pedir_numero_usuario("Elije => "))
            comprobar_opcion(opcion)
        except ValueError:
            mostrar_error("Opción incorrecta, intentalo de nuevo.")
            opcion = None


        limpiar_consola()
    return opcion

def mostrar_error(msj :str):
    print(f"**ERROR**, {msj}")
    pausa(2)


def mostrar_menu(): 
    print("1. hola.")
    print("2. hola.")
    print("3. Salir.\n")


def comprobar_opcion(opcion :int):    
    if not (opcion >= 1 and opcion <= 3):
        raise ValueError

def pedir_numero_usuario(mensaje :str) -> str:
    numero = input(f"{mensaje}")
    return numero


def preguntar_salir() -> bool:
    respuesta = input("\nEstas seguro que quieres salir? -> ")
    if respuesta == "s" or respuesta == "si":
        return True
    elif respuesta == "n" or respuesta == "no":
        return False


def pausa(tiempo :int, tecla_enter :bool):
    """
    Importa el paquete time y pausa la ejecucion del programa

    Args:

        tiempo (int) = tiempo que va a estar pausada la ejecucion

        tecla_enter (bool) = si es True va a estar pausada hasta que se haga un input en la consola
    """
    import time
    if tiempo != 0:
        time.sleep(tiempo)
    if tecla_enter == True:
        input("\nPresione ENTER para continuar...")


def limpiar_consola():
    """
    Importa el paquete os y limpia la pantalla
    """
    import os
    os.system("cls")


def main():
    """
    
    """
    limpiar_consola()
    salir = None

    while not salir:
        opcion = elegir_opcion_menu()
        if opcion == 1:
            numero = pedir_numero_usuario("\nDame un numero: ")
            print(f"\n hola hola: {funcion(numero)} \n")
            pausa(0, False)
            limpiar_consola()

        elif opcion == 2:
            numero = pedir_numero_usuario("\nDame un numero: ")
            print(f"\n hola hola: {funcion(numero)} \n")
            pausa(0, False)
            limpiar_consola()

        elif opcion == 3:
            pregunta = preguntar_salir()
            if pregunta == True:
                salir = True
            elif pregunta == False:
                salir = False
                limpiar_consola()


    pausa(3, False)
    limpiar_consola()


if __name__=="__main__":
    main()

