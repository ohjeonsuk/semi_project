# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 16:28:02 2023

@author: Jung
"""

import streamlit as st
from page import env_manual as pg1
from page import streamlit_manual as pg2
from page import diagram as pg3
from page import data_analyze as pg4

st.title('코로나19 전후 영화 특성에 따른 영화 소비 패턴의 변화 (6조)')

item = st.sidebar.selectbox('항목', ['가상환경 구축 매뉴얼', 'streamlit 매뉴얼', '프로젝트 diagram', '처리 및 분석한 내용'])




if item == '가상환경 구축 매뉴얼':
    pg1.app()
    
elif item == 'streamlit 매뉴얼':
    pg2.app()

elif item == '프로젝트 diagram':
    pg3.app()
    
elif item == '처리 및 분석한 내용':
    pg4.app()
    pg4.app2()
    
