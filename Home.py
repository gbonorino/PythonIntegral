# Home page, first one to appear when students click the link
import streamlit as st 
import time
from datetime import datetime
import random
from PIL import Image

image = Image.open('desmos-graph.png')
image = image.resize((750,500))

st.header("Bienvenidos!")
st.subheader("Plataforma de cuestionarios del curso Python Integral")
             
st.write("En este website encontrarán los Cuestionarios del curso organizados de la siguiente manera.\n" 
         + "En el menú de la izquierda se muestran los cuestionarios disponibles. Cada uno en su propia pestaña.\n"
         + "Los cuestionarios están diseñados para optimizar la retención de información. Para ello, puede \n"
         + "retomarlo las veces que desee. Las preguntas son elegidas aleatoriamente de una bolsa de preguntas \n"
         + "que hemos creado para que no se acostumbre al patron de respuestas y mejorar las chances de aprender.\n"
         + "Los cuestionarios son por tiempo y el puntaje mínimo es 0. El puntaje final se calcula en base a la formula\n")

st.latex(r'''\text{score} = 100 \cdot e^{-0.02 \cdot timeElapsed}''')

st.write("La cual aplica una penaliación al tiempo concurrido por pregunta. Aqui está la curva de la ecuación:")
st.image(image, caption="Curva de score. Creado con Desmos.")

st.subheader("Cuestionarios")
st.write("Los cuestionarios estan organizados por modulos en la siguiente manera:")
st.markdown("* Cuestionario 1: Resumen contenido del modulo 1.")
st.markdown("* Cuestionario 3: Resumen contenido del modulo 2.")
st.markdown("* Cuestionario i: Resumen contenido del modulo i.")

