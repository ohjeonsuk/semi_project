# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 01:51:09 2023

@author: Jung
"""

import streamlit as st
from utils import env_manual_desc as env


def app():
	st.write('''
		### 가상환경 구축 매뉴얼
		'''
		)

	env.desc()