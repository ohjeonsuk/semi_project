# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 10:31:21 2023

@author: Jung
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def desc():
    st.divider() 
    st.write('''**Streamlit이란?**
             파이썬을 이용하여 간단하게 웹 애플리케이션을 만들 수 있는 라이브러리. 
             Streamlit을 사용하면 파이썬 스크립트로 간단하게 데이터 시각화, 차트, 그래프, 표, 이미지 등을 웹 페이지로 변환하고, 
             사용자와 상호작용할 수 있는 기능을 추가할 수 있다.''')
    st.divider()          
        
    st.write('''**stramlit 설치 방법**''')
    st.write('''1. 터미널을 통해 설치하려는 환경에 진입한 후 ‘pip install streamlit’을 입력하여 설치를 진행한다.''')
    st.image('./images/sl1.png', use_column_width = True)
    st.write('''#''')
    
    st.write('''2. ‘Successfully installed-’ 라는 문구가 뜨면 설치가 완료됐음을 확인한다.
             *중간에 winerr 225 에러가 뜨면 실행중인 백신을 끄고 설치를 다시 진행한다.''')
    st.image('./images/sl2.png', use_column_width = True)
    st.write('''#''')
             
    st.write('''3. 설치 완료 후 python 실행 모드로 진입, ‘import streamlit’을 입력하여 streamlit 설치 유무를 확인한다. 
             아무것도 뜨지 않는다면 설치가 제대로 된 것이다.''')
    st.image('./images/sl3.png', use_column_width = True)
    st.write('''#''')

    st.divider()     

    st.write('''**streamlit을 사용한 웹서버 작동법**''')
    st.write(''''1. streamlit 이 설치된 가상환경으로 진입한다.''')
    st.image('./images/sl4.png', use_column_width = True)
    st.write('''#''')

    st.write('''2. 작성한 파일(ex. app.py)이 있는 폴더로 이동한다.''')
    st.image('./images/sl5.png', use_column_width = True)
    st.write('''#''')
    
    st.write('''3. ‘streamlit run 파일명(app.py)’ 를 입력하여 웹서버를 작동시킨다.
             (웹 브라우저에서 ‘http://localhost:8501’ 주소로도 접속 가능하다.)''')
    st.image('./images/sl6.png', use_column_width = True)
    st.write('''#''')
    
    st.write('''**streamlit 웹서버 종료 방법**''')
    st.write('''streamlit을 실행시킨 터미널(콘솔, powershell prompt)에서 crtl + c 버튼을 누른다.''')
    st.image('./images/sl7.png', use_column_width = True)
    st.write('''#''')
    
    st.divider()     
    
    st.write('''**streamlit 주요 기능 소개**''')
    st.write('''- 제목 및 텍스트 추가''')
    code1 = '''
    import streamlit as st 
    st.title('제목에 들어갈 내용') 
    st.header('헤더에 들어갈 내용') 
    st.write('텍스트 추가')
    '''
    st.code(code1, language='python')
    st.title('제목에 들어갈 내용') 
    st.header('헤더에 들어갈 내용') 
    st.write('텍스트 추가')
    
    st.write('''#''')
    st.write('''- 이미지 및 캡션 삽입''')    
    code2 = '''
    import streamlit as st 
    st.image('이미지 URL 또는 파일 경로', caption='이미지 캡션', use_column_width=True)
    '''
    st.code(code2, language='python')    
    st.write('''*use_column_width=True : 현재 창을 기준으로 크기 조정''')
    
    st.write('''#''')
    st.write('''- 그래프와 차트 추가''')
    code3 = '''
    import streamlit as st 
    data = [10, 20, 30, 40, 50]
    st.line_chart(data)
    '''
    st.code(code3, language='python')    
    data = [10, 20, 30, 40, 50]
    st.line_chart(data)
    
    st.write('''#''')
    st.write('''- 위젯 추가''')
    code4 = '''
    import streamlit as st 
    user_input = st.text_input('사용자 입력:')
    st.checkbox('체크박스')
    button_clicked = st.button('버튼')
    if button_clicked:
        st.write('버튼이 클릭되었습니다.')
    '''
    st.code(code4, language='python')    
    user_input = st.text_input('사용자 입력:')
    st.checkbox('체크박스')
    button_clicked = st.button('버튼')
    if button_clicked:
        st.write('버튼이 클릭되었습니다.')
    
    st.write('''#''')
    st.write('''- Pandas 데이터 프레임 추가''')
    code5 = '''
    import streamlit as st 
    import pandas as pd
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    st.dataframe(df)
    '''
    st.code(code5, language='python')        
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    st.dataframe(df)
    
    st.write('''#''')
    st.write('''- Matplotlib 그래프 추가''')
    code6 = '''
    import streamlit as st 
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3])
    st.pyplot(plt)
    '''
    st.code(code6, language='python')    
    plt.plot([1, 2, 3])
    st.pyplot(plt)
    
    st.write('''#''')
    st.write('''- 칼럼으로 레이아웃 분할''')
    code7 = '''
    import streamlit as st
    col1, col2 = st.columns([2,3])

    with col1 :
      st.title('첫번째 칼럼')
      st.write('첫번째 칼럼에 들어가는 내용입니다.')
    with col2 :
      st.title('두번째 칼럼')
      st.write('두번째 칼럼에 들어가는 내용입니다.')
    '''
    st.code(code7, language='python') 
    col1, col2 = st.columns([2,3])

    with col1 :
      st.title('첫번째 칼럼')
      st.write('첫번째 칼럼에 들어가는 내용입니다.')
    with col2 :
      st.title('두번째 칼럼')
      st.write('두번째 칼럼에 들어가는 내용입니다.')
    
    st.write('''#''')
    st.write('''- 사이드바 설정''')
    code8 = '''
    import streamlit as st
    item = st.sidebar.selectbox('항목', ['선택1', '선택2'])

    if item == '선택1':
        st.write('1번이 선택되었습니다.')
    elif item == '선택2':
        st.write('2번이 선택되었습니다.')
    '''
    st.code(code8, language='python')
    st.image('./images/sl8.png', use_column_width = True)
    st.image('./images/sl9.png', use_column_width = True)
    
    st.write('''#''')
    st.write('''- 파일 업로드 및 처리''')
    code9 = '''
    import streamlit as st
    import pandas as pd

    uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.dataframe(data)
    '''
    st.code(code9, language='python')
    uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.dataframe(data)
    st.write('''*위 예시에서는 사용자가 CSV 파일을 업로드하면 업로드된 파일이 DataFrame으로 변환되어 표 형태로 시각화 되며, 
             파일 유형 및 처리 방식은 원하는 대로 조정 가능하다.''')
    
    st.write('''#''')
    st.write('''- 파일 다운로드 링크 생성''')
    code10 = '''
    import streamlit as st
    st.download_button(label="다운로드 버튼", data="데이터 또는 파일 내용", file_name="다운로드할 파일 이름", key="download-button")
    '''
    st.code(code10, language='python')
    data = "다운로드할 파일의 내용입니다."
    file_name = "sample.txt"
    st.download_button("파일 다운로드", data=data, file_name=file_name, key="download-button")
    
    st.divider()
    st.write('''**이외 기능 및 사용법은 'https://docs.streamlit.io/' 참조**''')

    
    