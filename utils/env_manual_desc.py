# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 01:49:05 2023

@author: Jung
"""

import streamlit as st

def desc():
    st.divider() 
    st.write('''**가상환경을 만들어서 작업하는 이유 : 독립적인 작업환경에서 작업할 수 있기 때문.**''')
    st.write('''- 프로젝트 진행 시 여러 라이브러리를 다운로드 하여 사용하게 되는데 각 라이브러리들끼리 충돌을 일으킬 수 있으며, 
             특정 버전과 호환하는 경우가 생겨 버전을 선택해야 하는 상황이 발생할 수도 있다.
             가상환경은 버전을 별도로 지정할 수 있기에 이러한 문제가 발생하지 않는다.''')
    st.divider() 


    st.write('''1. 아나콘다(https://www.anaconda.com/download)를 로컬(각자의 데스크탑, 노트북 등)에 설치한다.''')    

    st.write('''2. 윈도우 시작 버튼 – Anaconda3 폴더의 Anaconda Powershell Prompt를 실행한다.''')
    st.image('./images/env1.png', use_column_width = True)
    st.write('''#''')
    
    st.write('''3. 처음 빈 화면에 우선 ‘conda env list’를 입력하여 설치된 가상환경 목록과 설치 경로를 확인한다. 
             (설치한 가상환경이 없다면 처음에는 ‘base’만 뜨는 것이 정상이다.)''')
    st.image('./images/env2.png', use_column_width = True)
    st.write('''#''')
    
    st.write('''4. 가상환경을 설치하기 위해 ‘conda create –n test(설정할 가상환경 이름) python=3.9(설치할 파이썬 버전)’을 입력한다. 
             필요에 따라 뒤에 ipython이나 numpy 등의 라이브러리 이름을 입력하여 추가로 설치할 수 있다.''')
    st.image('./images/env3.png', use_column_width = True)
    st.write('''#''')
         
    st.write('''5. 설치가 진행되는 동안 ‘Proceed ([y]/n)?’이란 문구가 뜨면 ‘y’를 입력한다.''')
    st.image('./images/env4.png', use_column_width = True)
    st.write('''#''')
         
    st.write('''6. 최종적으로 설치가 완료된 것을 확인한다.''')
    st.image('./images/env5.png', use_column_width = True)    
    st.write('''#''')
    
    st.write('''7. 설치된 가상환경에 진입하기 위해 ‘conda activate test(새로 설치한 가상환경 이름)’를 입력한다.
             이후 맨 앞 괄호 안의 문구가 가상환경 이름으로 바뀐 것이 확인되면 가상환경에 진입한 것이다.''')
    st.image('./images/env6.png', use_column_width = True)     
    st.write('''#''')
    
    st.write('''8. ‘python’을 입력하면 파이썬 실행 모드로 들어가며, 설치된 파이썬 버전을 확인할 수 있다. 
             가상환경을 설치할 때 입력한 버전과 일치하는 지 확인한다.
             *‘python –version’이라는 명령어를 입력하는 것으로도 버전을 확인할 수 있다.''')
    st.image('./images/env7.png', use_column_width = True)
    st.write('''#''')
    
    st.write('''9. 파이썬 실행 모드에서 ‘import 설치한 라이브러리명’을 입력하여 가상환경을 설치할 때 라이브러리도 제대로 설치 되었는지 확인한다. 
             아무런 문구 없이 넘어간다면 해당 라이브러리가 제대로 설치된 것이고, 
             설치되지 않았다면 ‘ModuleNotFoundError: No module named 라이브러리명’과 같은 오류 메시지가 뜬다.''')
    st.image('./images/env8.png', use_column_width = True)
    st.write('''#''')
    
    st.write('''10. 라이브러리까지 제대로 설치된 것이 확인되면 ‘exit()’를 입력하여 파이썬 실행 모드를 빠져나온다.
             * 추가 라이브러리 설치는 파이썬 실행 모드를 빠져나온 뒤 ‘pip install 라이브러리명’을 입력하면 된다.''')    
    st.image('./images/env9.png', use_column_width = True)
    st.write('''#''')
    
    st.write('''11. 가상환경을 빠져나오려면 ‘conda deactivate’를 입력하면 된다. 이후 맨 앞 괄호 안의 문구가 ‘base’로 변경된 것을 확인할 수 있다. ''')    
    st.image('./images/env10.png', use_column_width = True)
    st.write('''#''')
    
    st.write('''12. 가상환경 삭제는  ‘conda remove --name 삭제할 가상환경 이름 --all’을 입력하면 된다.
             다만 삭제하려는 가상환경에서 빠져나온 상태여야만 삭제가 가능하다.''')
    st.image('./images/env11.png', use_column_width = True)
    st.write('''#''')
    
    st.write('''13. 설치할 때와 마찬가지로 ‘Proceed ([y]/n)?’이란 문구가 뜨면 ‘y’를 입력한다. 이후 가상환경 삭제가 완료된 것을 확인할 수 있다.''')
    st.image('./images/env12.png', use_column_width = True)    
    