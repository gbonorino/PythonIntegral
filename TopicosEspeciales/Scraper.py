## Scraper para extraer data sobre acciones de yahoo finance y manipularla en un dataframe de pandas
### Luego, pondremos la data en una base de datos SQL para guardarla

import pandas as pd
import bs4 as soup
import requests


## copiar link de la pagina a analizar
url = 'https://finance.yahoo.com/u/yahoo-finance/watchlists/the-berkshire-hathaway-portfolio?.tsrc=fin-srch'

## descargar codigo html del link
info = requests.get(url) 
data = soup.BeautifulSoup(info.text, 'lxml')

## primero inspeccionamos el html en el buscador
## una vez encontrado la ubicacion de la data de interes la usamos par popular una lista
stocks = []

for i in data.findAll('td'):
    stocks.append(i.text)

## este es un paso extra para eliminar la data sobre los indices
parsedStocks = stocks[10:]

# ## a continuacion, para que sea mas facil manipular la data, ubicamos la informacion de cada accion por separado
# ## en el loop que veran estamos dividiendo nuestra primera lista (que tiene data de todas las acciones) en 9
# ## de esta forma tenemos 20 listas (con informacion unica de cada accion) dentro de una gran lista
x=0
y=len(parsedStocks)

listStocks = []
for i in range(x,y,9):
    x=i
    listStocks.append(parsedStocks[x:x+9])


## titulos para las columnas de nuestra data frame
headers = ['Ticker', 'Empresa', 'Ultimo Precio', 'Cambio $', 'Cambio %',
            'Tiempo', 'Volumen', 'Volumen Promedio (3 meses)', 'Valor de Mercado']

df = pd.DataFrame(columns=headers)


## populamos la pandas dataframe con la informacion que sacamos de yahoo finance
for row in listStocks:
    length = len(df)
    df.loc[length] = row

## asignamos un nombre mas representativo a nuestra tabla de datos
BHportfolio = df


## ahora estamos listos para manipular nuestra table de datos... yay!
### sacar hashtag para ver dataframe


## ahora vamos a crear una base de datos con SQL e importar nuestra data
import sqlite3

baseDeDatos = sqlite3.connect('CursoDB1.db') ## pongan el nombre que quieran
c = baseDeDatos.cursor()

## Creamos una tabla llamada "STOCKS1" con las columnas correspondientes
## la syntax es diferente porque corresponde al lenguaje SQL que es utilizado para manejo de base de datos
## Este tema sera trabajado en mas profundidad en nuestro curso de python para Data Science.

c.execute('CREATE TABLE STOCKS1 (Ticker, Empresa, UltPrecio, Cpesos, Cporcentual, Tiempo, Volumen, Volpromedio, ValorMercado)')
baseDeDatos.commit()

BHportfolio.to_sql('STOCKS1', baseDeDatos, if_exists = 'replace', index=False)

## ahora podemos acceder a nuestra nueva base de datos de SQL

c.execute('''
SELECT * FROM STOCKS1
          ''')

for row in c.fetchall():
    print(row)

