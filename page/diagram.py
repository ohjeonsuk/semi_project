# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 17:12:02 2023

@author: Jung
"""

import streamlit as st
from utils import diagram_desc as dgm

def app():
	st.write('''
		### 프로젝트 diagram
		''')

	dgm.desc()