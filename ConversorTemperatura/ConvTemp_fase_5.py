# Titulo: Conversor de temperatura
# Autor: yo
# Fecha: hoy
# Fase de desarrollo: 4
# Descripcion: 
#   Trabaja con clases.
#   Convierte temperaturas de Fahrenheit a Celsius y viceversa.
#   Opera indefinidamente. Gestiona errores de ingreso de datos.
#   Ingresar la escala de origen y los grados.

class Temperatura:
    def __init__(self, temp):
        self.temp = temp           # Variable de instancia

    def celsius_fahr(self):
        resultado = float((9 * self.temp) / 5 + 32)
        return resultado

    def fahr_celsius(self):
        resultado = float((self.temp - 32) * 5 / 9)
        return resultado

while True:
    try:
        escala = input("Ingrese escala de origen (celsius, fahrenheit): ")
        grados = float(input("Ingrese grados a convertir: "))

        if (escala != 'celsius') and (escala != 'fahrenheit'):
            print('Revise la escala')
            continue

        if escala == 'celsius':
            temp1 = Temperatura(grados)     # Instanciacion de objeto
            print(temp1.celsius_fahr())
        else:
            temp1 = Temperatura(grados)
            print(temp1.fahr_celsius())
    except:
        print('Algo no anduvo bien!')
    finally:
        res = input("Si desea continuar escriba si: ")
        if res != "si":
            break