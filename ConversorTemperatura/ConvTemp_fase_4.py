# Titulo: Conversor de temperatura
# Autor: yo
# Fecha: hoy
# Fase de desarrollo: 4
# Mejoras: Lee los datos de disco.
# Descripcion: Convierte temperaturas de Fahrenheit a Celsius y viceversa.
#   Ingresar la escala de origen y los grados cuando lo pida el programa. 
#   Escriba 'salir' para interrumpir la ejecucion.

import csv
import os

os.chdir('c:\\udemy_nuevo')
def fahr_celsius(gradFahr):
    return (gradFahr - 32) * 5.0 / 9.0

def celsius_fahr(gradCels):
    return gradCels * 9.0 / 5.0 + 32

def selecciona_archivos():
    escala = input('En que escala quiere los grados? celsius/fahrenheit ')
    if escala == 'celsius':
        archent = "TempAireArticoFahrenheit.csv"
        archsal = "TempAireArticoCelsius_sal.csv"
    else:
        archent = "TempAireArticoCelsius.csv"
        archsal = "TempAireArticoFahrenheit_sal.csv"
    return (archent, archsal, escala)

archent, archsal, escala = selecciona_archivos()

with open(archent,'r') as arch_1: 
    with open(archsal, 'w', newline='') as arch_2:
        temp_ent = csv.reader(arch_1)
        temp_sal = csv.writer(arch_2)
        contador = 0
        for fila in temp_ent:
            if contador == 0:
                temp_sal.writerow([fila[0]+"   "+fila[1]])
                contador = 1
            else:
                if escala == 'celsius':
                    conversion = float(fila[1])
                    grad_celsius = fahr_celsius(conversion)
                    temp_sal.writerow([fila[0] +"  "+ str(grad_celsius)])
                else:
                    conversion = float(fila[1])
                    grad_fahr = celsius_fahr(conversion)
                    temp_sal.writerow([fila[0] +"  "+ str(grad_fahr)])
