# Page for Cuestionario 1

import streamlit as st 
import time
from datetime import datetime
import random

from functions import Quiz

qus = [
{'question':"¿Qué es una variable?",
                  'options': {
                   "Un contenedor de valores":False,
                   "Un sitio en la memoria RAM":False,
                   "Un apuntador a un objeto":False,
                   "Todas las anteriores":True,
                   }},
                  
{'question':"El nombre de una variable puede iniciar con:",
                  'options': {
                   "Un número":False,
                   "El caracter '_'":True,
                   "Mayúscula":False,
                   "Ambos 2. y 3.":False,
                   }},
]

quiz1 = Quiz(num_mod=1, max_time=10, empty_node=st.empty(), quiz_questions=qus)

# function in file functions.py
quiz1.show_leaderboard()

quiz1.runQuiz()

        
        
        