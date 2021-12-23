import streamlit as st

from eda_app import run_eda_app


def main():
    st.title('17-18시즌 NBA 선수들의 연봉')
    
    menu = ['Home','EDA']
    choice = st.sidebar.selectbox('메뉴',menu)
    
    if choice == 'Home':
        st.subheader('이 데이터셋은 Basketball Reference에서 스크랩 했습니다.\
                이 데이터 셋은 플레이어 이름, 팀 및 급여 급액에 대한 정보가 있습니다.')
        st.image('http://jumpball.co.kr/news/data/20180609/p179579935773582_643.jpg')
        
    elif choice == 'EDA':
        run_eda_app()
if __name__ == '__main__':
    main()