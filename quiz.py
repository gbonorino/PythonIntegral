import streamlit as st 
import time
from datetime import datetime
import random

from functions import *
from questions import quiz_questions


row = None

    
#initialise the session state if keys don't yet exist
if 'correct' not in st.session_state.keys():
    st.session_state['correct'] = None
if "quiz_active" not in st.session_state.keys():
    st.session_state["quiz_active"] = False

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

i,j,_ = st.columns([1,1,5])
if i.button("Start quiz", key='start_quiz', disabled=st.session_state['quiz_active']):
    st.session_state['quiz_active'] = True
    st.session_state['total_score'] = 0
    st.session_state['count'] = 0
    st.session_state['time_start'] = time.time()
    st.session_state['time_now'] = time.time()
    st.session_state['score'] = 0
    st.session_state['correct'] = None
    st.experimental_rerun()
if j.button("End quiz and reset", key='reset', disabled=not st.session_state['quiz_active']):
    st.session_state['total_score'] = 0
    st.session_state['count'] = 0
    st.session_state['correct'] = None
    st.session_state['quiz_active'] = False
    st.session_state['time_start'] = None
    st.experimental_rerun()

if not st.session_state['quiz_active']:
    st.write(f'\\n Welcome to the quiz! You have {TIME_LIMIT} seconds to answer as many questions as you can.')
                
    
question_empty = st.empty()

d,e,_ = st.columns([2,2,6])
with d:
    total_score_empty = st.empty()
    time_left_empty = st.empty()
with e:
    st.write('')
    answer_empty = st.empty()
    
st.markdown('---')

# function in file functions.py
show_leaderboard(question_empty)

if st.session_state['quiz_active']:
    #check for time up upon page update
    if time.time() - st.session_state['time_start'] > TIME_LIMIT:
        show_leaderboard(question_empty, show_results=True)
        
    else:
        with question_empty:
            with st.container():
                #get a newly generated question with answer options
                row_new = random.choice(quiz_questions)
                
                while row_new == row:
                    row_new = random.choice(quiz_questions)
                row = row_new
                
                st.markdown(f"Question {st.session_state['count']+1}: {row['question']}")
                a,b,_ = st.columns([1,1,6])

                options = list(row['options'].keys())
                random.shuffle(options)

                #construct the answer buttons, and pass in whether the answer is correct or not in the args
                if len(options) == 2:
                    st.button(options[0], on_click=answer, args=(str(row['options'][options[0]]),))
                    st.button(options[1], on_click=answer, args=(str(row['options'][options[1]]),))
                elif len(options) == 3:
                    a.button(f"{options[0]}", on_click=answer, args=(str(row['options'][options[0]]),))
                    a.button(f"{options[1]}", on_click=answer, args=(str(row['options'][options[1]]),))
                    b.button(f"{options[2]}", on_click=answer, args=(str(row['options'][options[2]]),))
                else:
                    a.button(f"{options[0]}", on_click=answer, args=(str(row['options'][options[0]]),))
                    a.button(f"{options[1]}", on_click=answer, args=(str(row['options'][options[1]]),))
                    b.button(f"{options[2]}", on_click=answer, args=(str(row['options'][options[2]]),))
                    b.button(f"{options[3]}", on_click=answer, args=(str(row['options'][options[3]]),))
                
                if st.session_state['correct']  == 'True' and st.session_state['count'] > 0:
                    answer_empty.success(f"Question {st.session_state['count']} correct!")
                elif st.session_state['correct'] == 'False' and st.session_state['count'] > 0:
                    answer_empty.error(f"Question {st.session_state['count']} incorrect!")
                
                total_score_empty.metric('Total score', value=f"{st.session_state['total_score']:.2f}", delta=f"{st.session_state['score']:.2f}")
                time_left_empty.write(f"{get_time_remaining(time.time())}")