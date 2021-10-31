from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd

def fahr_celsius(gradFahr):
    return (gradFahr - 32) * 5.0 / 9.0

def datos(temp_csv):
    for i in range(0, len(temp_csv)):
        l=len(temp_csv)
        s = temp_csv['TempAire'][i]
        gradCelsius.append(fahr_celsius(s))
    plt.plot(gradCelsius)
    plt.show()

gradCelsius = []
archent = "TempAireArticoCelsius.csv"
temp_csv = pd.read_csv(archent)

root = Tk()
root.title('Conversion de temperaturas')
root.geometry('400x200')

boton = Button(root, text='Graficar', command = lambda arg1=temp_csv: datos(arg1))
boton.pack(pady=10)
root.mainloop()
