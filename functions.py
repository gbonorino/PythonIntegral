import streamlit as st 
import time
from datetime import datetime
import random
import math
import pandas as pd
import os, glob
import randomname

TIME_LIMIT = 20 #seconds


def get_name():
    loop = True
    while loop:
        name = randomname.get_name()
        if not os.path.exists(f'{name}.csv'):
            loop = False
    return 

def gen_question():
    #randomly choose two numbers in a range, alongside an operator
    operators = ['+','-','//','*']
    a,b = random.randint(1,10), random.randint(1,10)
    op = random.choice(operators)
    
    #construct the question text and evaluate the calculation
    ques = f"What is {a} {op} {b}?"
    ans = eval(f"{a}{op}{b}")

    #we create some purposely incorrect answer options
    option2 = eval(f"{b}{op}{a}")
    option3 = eval(f"{b-2}{op}{a+5}")
    option4 = eval(f"{b}{op}{a}-{a}")
    #we want to avoid duplicate answer options, so use this inelegant solution
    while option2 == ans:
       option2 += 1
    while option3 == ans or option3 == option2:
       option3 += 1
    while option4 == ans or option4 == option2 or option4 == option3:
       option4 += 1
    
    return {'question': ques,
            'options': {
            ans: True,
            option2: False,
            option3: False,
            option4: False
            }
            }
    
def answer(ans):
    st.session_state['correct'] = ans
    if ans == 'True':
        #motivate quickfire answers with an exponential decay
        score = (1 * math.exp(-0.05*(time.time()-st.session_state['time_now'])))*10
        st.session_state['score'] = max(1, score)
    else:
        #penalise wrong answers with a negative score
        st.session_state['score'] = -10
        
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
                g,h,i = st.columns([6,3,6])
                #st.subheader("Time's up!")
                g.info(f"Time's up! You scored a total of **{st.session_state['total_score']:.2f}** \
                    and answered **{st.session_state['count']}** questions.")
                h.text('\n'); h.text('\n'); h.text('\n'); h.text('\n'); h.text('\n'); h.text('\n')
                if h.button('Give me a different name'):
                    st.session_state['name'] = st.text_input("Como es tu nombre?")
                if 'name' not in st.session_state.keys():
                    st.session_state['name'] = st.text_input("Como es tu nombre?")
                g.markdown(f'Do you want to submit your score to the leaderboard? \n \
                Your name on the leader board will be **{st.session_state["name"]}**.')
            else:
                _,_, i = st.columns([6,6,6])

            df_leaderboard = get_all_leaderboard()
            i.subheader('Leaderboard')
            i.table(df_leaderboard.sort_values(by='Final score', ascending=False).style.set_table_styles(
            [{
                'selector': 'th',
                'props': [
                    ('background-color', '#D3D3D3'),
                    ('font-color', 'gray')]
            }]))
            
            if show_results:
                if not isinstance(st.session_state['total_score'] , float):
                    st.session_state['total_score'] = 0
                df = pd.DataFrame({'Name': st.session_state["name"], 'Final score': st.session_state['total_score'], 'Questions answered': st.session_state['count'], 'Date': datetime.today().strftime("%d/%m/%Y")}, index=[0])
                g.table(df)
                if st.button('Submit my score'):
                    with st.spinner(''):
                        df.to_csv(f'leaderboard_data/{st.session_state["name"]}.csv', mode='a', index=False)
                        st.success('Your score has been submitted!')
                        st.session_state['quiz_active'] = False
                        time.sleep(2)
                        st.experimental_rerun()
            #st.markdown('---')
            
