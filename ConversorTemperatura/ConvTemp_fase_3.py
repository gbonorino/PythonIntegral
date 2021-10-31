# Titulo: Conversor de temperatura
# Autor: yo
# Fecha: hoy
# Fase de desarrollo: 3
# Mejoras: Organiza codigo con una funcion principal que gobierna la ejecucion. 
#          Introduce clausula try ... except y usa bucle while para el usuario.
# Descripcion: Convierte temperaturas de Fahrenheit a Celsius y viceversa.
#   Ingresar la escala de origen y los grados cuando lo pida el programa. 
#   Escriba 'salir' para interrumpir la ejecucion.

def opcion_escala(opcion, grad):
    ans = 0

    if opcion == 'celsius':        # Ingresa grados Celsius
        ans = grad * 9.0 / 5.0 + 32.0

    elif opcion == 'fahrenheit':   # Ingresa grados Fahrenheit
        ans = (grad - 32) * 5.0 / 9.0

    return ans

def principal():
    escala = input("Ingrese escala de origen: ")

    while (escala != 'salir'):
        try:
            grados = float(input("Ingrese grados a convertir: "))

            if (escala == 'celsius'):
                print(f"{grados} grados en fahrenheit son {opcion_escala(escala, float(grados))}")

            elif (escala == 'fahrenheit'):
                print(f"{grados} grados en celsius son {opcion_escala(escala, float(grados))}")

            escala = input("Ingrese escala de origen o salir para terminar el programa: ")

            while (escala != 'celsius') and (escala != 'fahrenheit') and (escala != 'salir'):
                escala = input("Input incorrecto. Seleccione entre celsius/fahrenheit: ")

        except:
            print('Ocurrio un error')

    print("Gracias por utilizar nuestro software. Esperamos le haya sido util.")

principal()