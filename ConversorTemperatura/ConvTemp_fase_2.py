# Titulo: Conversor de temperatura
# Autor: yo
# Fecha: hoy
# Fase de desarrollo: 2
# Mejora: Ingreso de datos por teclado. Funciones de conversión anidadas. 
#         Opción condicional.
# Descripcion: Convierte temperaturas de Fahrenheit a Celsius y viceversa.
#              Ingresar la escala de origen y los grados, separados por espacio.

def opcion_escala(opcion, grad):
    if opcion == 'celsius':        # Ingresa grados Celsius
        def celsius_fahr(grados):
            return grados * 9.0 / 5.0 + 32.0

        print(celsius_fahr(grad))
    elif opcion == 'fahrenheit':   # Ingresa grados Fahrenheit
        def fahr_celsius(grados):
            return (grados - 32) * 5.0 / 9.0

        print(fahr_celsius(grad))
    else:
        print('Algo anduvo mal')
        
escala, grados = input("Ingrese escala y grados. Separar con espacio. ").split()
opcion_escala(escala, float(grados))

