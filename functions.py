import streamlit as st 
import time
from datetime import datetime
import random
import math
import pandas as pd
import os, glob
import randomname

TIME_LIMIT = 5 #seconds


def answer(ans):
    st.session_state['correct'] = ans
    if ans == 'True':
        #motivate quickfire answers with an exponential decay
        score = (1 * math.exp(-0.02*(time.time()-st.session_state['time_now'])))*100
        st.session_state['score'] = max(1, score)
    else:
        #penalise wrong answers with a negative score
        st.session_state['score'] = -5
        
    #update the score but prevent it from becoming negative
    if st.session_state['total_score'] + st.session_state['score'] > 0:
        st.session_state['total_score'] += st.session_state['score']
    
    else:
        st.session_state['total_score'] = 0
        st.session_state['score'] = 0
        
    st.session_state['total_score'] = max(0, st.session_state['total_score'])
    st.session_state['time_now'] = time.time()
    st.session_state['count'] += 1
    
def get_time_remaining(timing):
    time_left = TIME_LIMIT - (timing - st.session_state['time_now'])
    if time_left < 20:
        return 'Only a few seconds left!'
    else:
        return ''
    
def get_all_leaderboard():
    csvs = glob.glob('leaderboard_data/*.csv')
    dfs = [pd.read_csv(i, index_col=False) for i in csvs]
    return pd.concat(dfs)

def show_leaderboard(empty_node, show_results=False):
    with empty_node:
        with st.container():
            if show_results:
                g, _ = st.columns([6, 1], gap='medium')
                #st.subheader("Time's up!")
                g.info(f"Se acabo el tiempo! Obtuviste un puntaje de **{st.session_state['total_score']:.2f}** \
                    y respondiste **{st.session_state['count']}** preguntas.")
                
                # agregar boton que inicie la condicion para tomar el nombre
                # y recien mostrar la tabla con el nombre indicado
                # para evitar que se muestre el ultimo nombre en session_state
                
                if st.checkbox("Publicar puntaje en el ranking"):
                
                    nombre = g.text_input("Como es tu nombre?")
                    if len(nombre) > 0:
                        if not os.path.exists(f'leaderboard_data/{nombre.lower()}.csv'):
                            st.session_state["name"] = nombre
                        else:
                            st.warning("Ya existe el nombre. Proba una variacion.")
                        
                    g.markdown(f'Su nombre en el ranking sera ** {st.session_state["name"]} **.')
                    
                    if not isinstance(st.session_state['total_score'], float):
                        st.session_state['total_score'] = 0
                    
                    df = pd.DataFrame({'Nombre': st.session_state["name"],
                            'Puntaje Final': st.session_state['total_score'],
                            'Preguntas Respondidas': st.session_state['count'],
                            'Fecha': datetime.today().strftime("%d/%m/%Y")}, index=[0])
                    g.table(df)
               
                    if st.button('Submit my score'):
                        with st.spinner('Cargando'):
                            df.to_csv(f'leaderboard_data/{st.session_state["name"]}.csv', index=False)
                            st.success('Su puntaje se cargo con exito!')
                            st.session_state['quiz_active'] = False
                            time.sleep(2)
                            st.experimental_rerun()
                
                l, _ = st.columns([6, 1], gap='medium')

                df_leaderboard = get_all_leaderboard()
                
                l.subheader('Tabla de Liderazgo')
                l.table(df_leaderboard.sort_values(by='Puntaje Final', ascending=False).style.set_table_styles(
                [{
                    'selector': 'th',
                    'props': [
                        ('background-color', '#000000'),
                        ('font-color', 'white')]
                }]))
    
