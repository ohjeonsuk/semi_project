# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:45:54 2023

@author: Jung
"""

import streamlit as st
from utils import streamlit_manual_desc as stm


def app():
	st.write('''
		### stramlit 매뉴얼
		''')

	stm.desc()