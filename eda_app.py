import streamlit as st
import pandas as pd
import numpy as np

def run_eda_app():
    df = pd.read_csv('data/NBA_season1718_salary.csv',index_col=0)
    
    st.subheader('NBA 선수들의 연봉을 알아보자')
    menu = ['컬럼 정보','데이터 프레임']
    selected = st.radio('데이터 정보',menu)
    if selected == '컬럼 정보':
        st.text('Player = 선수 이름')
        st.text('Tm = 팀이름')
        st.text('season17_18 = 17-18시즌 연봉')
    else :
        st.dataframe(df)
        
    st.subheader('연봉 범위')
    st.slider('보고싶은 범위를 선택해주세요',min_value=df['season17_18'].min(),max_value=df['season17_18'].max())