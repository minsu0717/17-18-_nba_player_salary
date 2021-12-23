import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

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
        
    st.subheader('선수 검색 하기')
    player = st.text_input('이름을 적어주세요')
    st.write(df.loc[df['Player'].str.lower().str.contains(player.lower()),])
    
    st.subheader('연봉 상위 10명과 하위 10명')
    menu_2 = ['상위 10명','하위 10명']
    choice =st.radio('선택',menu_2)
    if choice == '상위 10명':
        st.write(df.sort_values('season17_18',ascending=False).head(10))
    else :
        st.write(df.sort_values('season17_18',ascending=False).tail(10))
        
    st.subheader('어떤 팀이 선수와 계약을 많이 했는지 보기')
    fig1=plt.figure(figsize=(15,10))
    sns.countplot(data=df,x='Tm',order=df['Tm'].value_counts().index)
    st.pyplot(fig1)
    st.write(df.groupby('Tm').count().sort_values('Player',ascending=False)['Player'])
    
    st.subheader('어떤 팀이 선수를 비싸게 영입했는지 보기')
    team = df.groupby('Tm')['season17_18'].mean()
    team=team.sort_values(ascending=False)
    fig1=plt.figure(figsize=(15,10))
    plt.bar(team.index,team)
    st.pyplot(fig1)
    st.write(team)
    
    st.subheader('팀 순위 보기')
    menu_3 = ['동부','서부']
    choice_region=st.radio('선택',menu_3)
    if choice_region == '동부':
        st.image('data/nba_2.png')
    else:
        st.image('data/nba_1.png')
        
    st.subheader('분석 결과 선수와 많이 계약을 한 것 보다 돈을 많이 쓰는 팀이\
        좋은 성적을 낸다는 것을 알 수 있다.')