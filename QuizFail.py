import streamlit as st 
import time
from datetime import datetime
import random
import math
import pandas as pd
import os, glob
import randomname

TIME_LIMIT = 5 #seconds

class Quiz:
    def __init__(self, num_mod, max_time, empty_node, quiz_questions='default', ans=False):
        self.ans = ans
        self.num_mod = num_mod
        self.max_time = max_time
        self.empty_node = empty_node
        
        csvs = glob.glob('leaderboard_data/*.csv')
        dfs = [pd.read_csv(i, index_col=False) for i in csvs]
        self.df_leaderboard = pd.concat(dfs)
        
        defaultQuest = [
{'question':"What does NDVI stand for?",
                  'options': {
                   "Natural difference vegetation index":False,
                   "Nature dynamic vigour index":False,
                   "Nature dimensionless vigour index":False,
                   "Normalised difference vegetation index":True,
                   }},
                  
{'question':"Deforestation is the ____ largest cause of human-caused climate change?",
                  'options': {
                   "1st":False,
                   "2nd":True,
                   "3rd":False,
                   "4th":False,
                   }},
                  
{'question':"Which of the following does deforestation affect?",
                  'options': {
                   "Harm to the local economies":False,
                   "Uprooting indigenous people":False,
                   "Threaten biodiversity":False,
                   "All of the options":True,
                   }},
                  
{'question':"The rainforest houses incredible biodiversity. Which of these is **not** a real rainforest resident?",
                  'options': {
                   "Thunder Dragon Mantis":True,
                   "Black Howler Monkey":False,
                   "Strawberry Dart Frog":False,
                   "Rhinoceros Hornbill":False,
                   }},
                  
{'question':"How many of the Earth’s plants and animals are found in the tropical rainforests?",
                  'options': {
                   "25%":False,
                   "33%":False,
                   "50%":True,
                   "75%":False,
                   }},

{'question':"How much of the Earth’s surface is covered by oceans? ",
                  'options': {
                   "51%":False,
                   "71%":True,
                   "81%":False,
                   "91%":False,
                   }},
                  
{'question':"True or False. Humans have mapped more of Mars than they have of the Earth’s oceans.", 
                  'options': {
                    'True': True,
                    'False': False,
                    }},
            
{'question':"How deep is the Marianas trench?",
                  'options':{
                   "1 mile":False,
                   "2 miles":False,
                   "7 miles":True,
                   "11 miles":False,
                   }},
                  
{'question':"Which is **not** a cause of major ocean currents?",
                  'options':{
                   "Wind blowing": False,
                   "Volcanoes erupting": True,
                   "Earth rotating": False,
                   "Water density varying": False,
                   }},
                  
{'question':"Which process does not lead to a decrease in water salinity?",
                  'options':{
                   "Run off from the land": False,
                   "Precipitation": False,
                   "Sea ice melting": False,
                   "Evaporation": True,
                  }},

{'question':"Where is the majority of the permafrost in the world?",
                  'options': {
                   "Arctic": True,
                   "Antarctica": False,
                  }},
                  
{'question':"What is the altitude of a geostationary satellite?",
                  'options': {
                   "35,786 km": True,
                   "17,786 km": False,
                   "1,778 km": False,
                   "3,578 km": False,
                  }},
                  
{'question':"What type of satellite has an active sensor?",
                  'options': {
                   "Radar": True,
                   "Hyperspectral": False,
                   "Optical": False,
                   "Thermal": False,
                  }},

{'question':"What percentage of the electromagnetic spectrum are we able to see with our own eyes?",
                  'options': {
                   "0.0035%": True,
                   "0.035%": False,
                   "0.35%": False,
                   "3.5%": False,
                  }},
                  
{'question':"As plants become more stressed, they reflect near infrared wavelengths less strongly.",
                  'options': {
                   "True": True,
                   "False": False,
                  }},
                  
{'question':"Remote sensing techniques make use of the properties of ______________ emitted, reflected or diffracted by the sensed objects?",
                  'options': {
                   "Electromagnetic waves": True,
                   "Sound waves": False,
                   "Wind waves": False,
                   "Electric waves": False,
                  }},
                 
{'question':"Which type of remote sensing uses its own source of electromagnetic energy?",
                  'options': {
                   "Active": True,
                   "Passive": False,
                   "Both": False,
                   "None": False,
                  }},
]
        if quiz_questions == 'default':
            self.quiz_questions = defaultQuest
        
        else:
            self.quiz_questions = quiz_questions
            
        
        st.header("Cuestionario Modulo " + str(self.num_mod))
            
        
    def getNumMod(self):
        return self.num_mod
    
    def getMaxTime(self):
        return self.max_time
    
    def activate(self):
        self.active = True
    
    
    def answer(self):
        self.correct = self.ans
        if self.ans == 'True':
            #motivate quickfire answers with an exponential decay
            score = (1 * math.exp(-0.02*(time.time()-self.time_now)))*100
            self.score = max(1, score)
        else:
            #penalise wrong answers with a negative score
            self.score = -5
            
        #update the score but prevent it from becoming negative
        if self.total_score + self.score > 0:
            self.total_score += self.score
        
        else:
            self.total_score = 0
            self.score = 0
            
        self.total_score = max(0, self.total_score)
        self.time_now = time.time()
        self.count += 1
        
    def get_time_remaining(self, timing):
        time_left = self.max_time - (timing - self.time_now)
        if time_left < self.max_time:
            return 'Only a few seconds left!'
        else:
            return ''
        
    def get_all_leaderboard(self):
        csvs = glob.glob('leaderboard_data/*.csv')
        dfs = [pd.read_csv(i, index_col=False) for i in csvs]
        self.df_leaderboard = pd.concat(dfs)
        return self.df_leaderboard
    
    def runQuiz(self):
        # initialise the session state if keys don't yet exist
        # session state keeps the values of the parameters set during that session
        
        self.correct = None
        self.quiz_active = False
        
        i,j,_ = st.columns([1,1.5,5])
        if i.button("Start quiz", key='start_quiz', disabled=self.quiz_active):
            self.quiz_active = True
            self.total_score = 0
            self.count = 0
            self.time_start = time.time()
            self.time_now = time.time()
            self.score = 0
            self.correct = None
            self.name = " "
            st.experimental_rerun()
            
        if j.button("End quiz and reset", key='reset', disabled=not self.quiz_active):
            self.total_score = 0
            self.count = 0
            self.correct = None
            self.quiz_active = False
            self.time_start = None
            st.experimental_rerun()

        if not self.quiz_active:
            
            st.write(f'\n Bienvenidos al cuestionario numero {self.num_mod}! Tiene {self.max_time} segundos para responder la mayor cantidad de preguntas que pueda.\n'
                    + '\n Puede reintentar las veces que desee, y publicar su puntaje a la tabla de liderazgo gobal para comparar su rendimiento al de alumnos anteriores.\n'
                    + '\n Si no quiere publicar su puntaje simplemente regrese al curso :)')
                        
            
            l, _ = st.columns([6, 1], gap='medium')

            df_leaderboard = self.get_all_leaderboard()

            l.subheader('Tabla de Liderazgo')
            l.table(df_leaderboard.sort_values(by='Puntaje Final', ascending=False).style.set_table_styles(
            [{
                'selector': 'th',
                'props': [
                    ('background-color', '#000000'),
                    ('font-color', 'white')]
            }]))

        # CSS to inject contained in a string
        hide_table_row_index = """
                    <style>
                    tbody th {display:none}
                    .blank {display:none}
                    </style>
                    """

        # Inject CSS with Markdown
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        if self.quiz_active:
            #check for time up upon page update
            if time.time() - self.time_start > self.max_time:
                self.show_leaderboard(show_results=True)
                
            else:
                self.show_questions()
    
    def show_questions(self):
        row = None
        with self.empty_node:
            with st.container():
                # Seleccion aleatoria de archivo questions.py
                row_new = random.choice(self.quiz_questions)
                
                while row_new == row:
                    row_new = random.choice(self.quiz_questions)
                row = row_new
    
                
                st.markdown(f"Question {self.count+1}: {row['question']}")
                a,b,_ = st.columns([2,2,5])

                # options = lista de preguntas en questions.py
                options = list(row['options'].keys())
                
                random.shuffle(options)
                
                # Botones con opciones de respuesta
                if len(options) == 2:
                    st.button(options[0], on_click=self.answer(), args=(str(row['options'][options[0]]),))
                    st.button(options[1], on_click=self.answer(), args=(str(row['options'][options[1]]),))
                elif len(options) == 3:
                    a.button(f"{options[0]}", on_click=self.answer(), args=(str(row['options'][options[0]]),))
                    a.button(f"{options[1]}", on_click=self.answer(), args=(str(row['options'][options[1]]),))
                    b.button(f"{options[2]}", on_click=self.answer(), args=(str(row['options'][options[2]]),))
                else:
                    a.button(f"{options[0]}", on_click=self.answer(), args=(str(row['options'][options[0]]),))
                    a.button(f"{options[1]}", on_click=self.answer(), args=(str(row['options'][options[1]]),))
                    b.button(f"{options[2]}", on_click=self.answer(), args=(str(row['options'][options[2]]),))
                    b.button(f"{options[3]}", on_click=self.answer(), args=(str(row['options'][options[3]]),))
            
            d,e,_ = st.columns([2,2,6])
            with d:
                total_score_empty = st.empty()
                time_left_empty = st.empty()
            with e:
                st.write('')
                answer_empty = st.empty()
                
            if self.correct  == 'True' and self.count > 0:
                answer_empty.success(f"Question {self.count} correct!")
            elif self.correct == 'False' and self.count > 0:
                answer_empty.error(f"Question {self.count} incorrect!")
            
            total_score_empty.metric('Total score', value=f"{self.total_score:.2f}", delta=f"{self.score:.2f}")
            time_left_empty.write(f"{self.get_time_remaining(time.time())}")
                


    def show_leaderboard(self, show_results=False):
        with self.empty_node:
            with st.container():
                if show_results:
                    g, _ = st.columns([6, 1], gap='medium')
                    #st.subheader("Time's up!")
                    g.info(f"Se acabo el tiempo! Obtuviste un puntaje de **{self.total_score:.2f}** \
                        y respondiste **{self.count}** preguntas.")
                    
                    # agregar boton que inicie la condicion para tomar el nombre
                    # y recien mostrar la tabla con el nombre indicado
                    # para evitar que se muestre el ultimo nombre en session_state
                    
                    if st.checkbox("Publicar puntaje en el ranking"):
                    
                        nombre = g.text_input("Como es tu nombre?")
                        if len(nombre) > 0:
                            if not os.path.exists(f'leaderboard_data/{nombre.lower()}.csv'):
                                self.name = nombre
                            else:
                                st.warning("Ya existe el nombre. Proba una variacion.")
                            
                        g.markdown(f'Su nombre en el ranking sera ** {self.name} **.')
                        
                        if not isinstance(self.total_score, float):
                            self.total_score = 0
                        
                        df = pd.DataFrame({'Nombre': self.name,
                                'Puntaje Final': self.total_score,
                                'Preguntas Respondidas': self.count,
                                'Fecha': datetime.today().strftime("%d/%m/%Y")}, index=[0])
                        g.table(df)
                
                        if st.button('Publicar mi score'):
                            with st.spinner('Cargando'):
                                df.to_csv(f'leaderboard_data/{self.name}.csv', index=False)
                                st.success('Su puntaje se cargo con exito!')
                                self.quiz_active = False
                                time.sleep(2)
                                st.experimental_rerun()
                    
                    l, _ = st.columns([6, 1], gap='medium')
                    
                    csvs = glob.glob('leaderboard_data/*.csv')
                    dfs = [pd.read_csv(i, index_col=False) for i in csvs]
                    self.df_leaderboard = pd.concat(dfs)

                    df_leaderboard = self.df_leaderboard
                    
                    l.subheader('Tabla de Liderazgo')
                    l.table(df_leaderboard.sort_values(by='Puntaje Final', ascending=False).style.set_table_styles(
                    [{
                        'selector': 'th',
                        'props': [
                            ('background-color', '#000000'),
                            ('font-color', 'white')]
                    }]))
        
