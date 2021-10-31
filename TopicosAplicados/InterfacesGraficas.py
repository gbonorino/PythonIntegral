## ejercicio de Interfaces Graficas (GUI) con tkinter
## vamos a crear un GUI conectado a una API de google que dado el nombre de una cancion,
## nos devuelve la letra de esa cancion

## Tkinter documentacion --> https://docs.python.org/3/library/tkinter.html
## link para crear search engine --> https://cse.google.com/cse/create/new

'''
https://genius.com/
http://www.lyricsted.com/
http://www.lyricsbell.com/
https://www.glamsham.com/
http://www.lyricsoff.com/
http://www.lyricsmint.com/
'''

## link para crear API key --> https://developers.google.com/custom-search/v1/overview

from tkinter import *
from lyrics_extractor import SongLyrics

apiKey = 'AIzaSyBPmr54bR_DxLqz-VEKuPzMQs3vikThqb0'
engineID = 'bee5bfe9d6edac213'


## definimos algunas funciones para modularizar el proyecto 
def get_lyrics():

	extract_lyrics = SongLyrics(apiKey, engineID)

	temp = extract_lyrics.get_lyrics(str(e.get()))
	res = temp['lyrics']
	result.set(res)


## objecto de tkinter
## especificamos el color de fondo de nuestra interfaz
master = Tk()
master.configure(bg='white')

# variable clases en tkinter
result = StringVar()

# creamos un clase label
# creamos un widget
Label(master, text="Enter Song name : ",
	bg="light grey").grid(row=0, sticky=W)

Label(master, text="Result :",
	bg="light grey").grid(row=3, sticky=W)


# creamos nueva label para segunda clase
# creamos un metodo Entry
Label(master, text="", textvariable=result,
	bg="light grey").grid(row=3, column=1, sticky=W)

e = Entry(master, width=50)
e.grid(row=0, column=1)

# creamos un boton usando el metodo Button
b = Button(master, text="Buscar",
		command=get_lyrics, bg="Light Blue")

b.grid(row=0, column=2, columnspan=2,
	rowspan=2, padx=5, pady=5,)

mainloop()

