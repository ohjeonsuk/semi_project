# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 17:03:18 2023

@author: Jung
"""

from utils import module as mo
import streamlit as st

def app():    
    
    covid_2020_number = mo.get_data_COVID19_2020('.//data//코로나19_확진자_발생동향.xlsx')
    covid_2021_number = mo.get_data_COVID19_2021('.//data//코로나19_확진자_발생동향.xlsx')
    covid_2022_number = mo.get_data_COVID19_2022('.//data//코로나19_확진자_발생동향.xlsx')

    covid_number = [covid_2020_number, covid_2021_number, covid_2022_number]
    st.write('연도별 코로나확진자수')
    data5 = {'코로나확진자수': covid_number}
    COVID19_numbers = mo.COVID19_numbers_graph(data5, '국적별 영화관람객수')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(COVID19_numbers)
    
    movie_sales_2018, movie_audience_2018 = mo.get_data('.//data//KOBIS_연도별박스오피스_2018.xlsx')
    movie_sales_2019, movie_audience_2019 = mo.get_data('.//data//KOBIS_연도별박스오피스_2019.xlsx')
    movie_sales_2020, movie_audience_2020 = mo.get_data('.//data//KOBIS_연도별박스오피스_2020.xlsx')
    movie_sales_2021, movie_audience_2021 = mo.get_data('.//data//KOBIS_연도별박스오피스_2021.xlsx')
    movie_sales_2022, movie_audience_2022 = mo.get_data('.//data//KOBIS_연도별박스오피스_2022.xlsx')
    movie_audience = [movie_audience_2018, movie_audience_2019, movie_audience_2020, movie_audience_2021, movie_audience_2022]
    movie_sales = [movie_sales_2018, movie_sales_2019, movie_sales_2020, movie_sales_2021, movie_sales_2022]  
    
    st.write('연도별 영화관람객수/영화매출액')
    data3 = {'영화관람객수': movie_audience}
    data4 =  {'영화매출액': movie_sales}
    year_movie = mo.year_movie_graph(data3, data4, '연도별 영화관람객수 영화매출액')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(year_movie)
    
    
    
    st.write('월별 영화 매출액 및 관객수')
    file_path = './/data//KOBIS_월별박스오피스_18_fh.xlsx'
    sales_18_fh, aud_18_fh = mo.get_data_month(file_path)
    file_path = './/data//KOBIS_월별박스오피스_18_sh.xlsx'
    sales_18_sh, aud_18_sh = mo.get_data_month(file_path)
    
    file_path = './/data//KOBIS_월별박스오피스_19_fh.xlsx'
    sales_19_fh, aud_19_fh = mo.get_data_month(file_path)
    file_path = './/data//KOBIS_월별박스오피스_19_sh.xlsx'
    sales_19_sh, aud_19_sh = mo.get_data_month(file_path)

    file_path = './/data//KOBIS_월별박스오피스_20_fh.xlsx'
    sales_20_fh, aud_20_fh = mo.get_data_month(file_path)
    file_path = './/data//KOBIS_월별박스오피스_20_sh.xlsx'
    sales_20_sh, aud_20_sh = mo.get_data_month(file_path)

    file_path = './/data//KOBIS_월별박스오피스_21_fh.xlsx'
    sales_21_fh, aud_21_fh = mo.get_data_month(file_path)
    file_path = './/data//KOBIS_월별박스오피스_21_sh.xlsx'
    sales_21_sh, aud_21_sh = mo.get_data_month(file_path)

    file_path = './/data//KOBIS_월별박스오피스_22_fh.xlsx'
    sales_22_fh, aud_22_fh = mo.get_data_month(file_path)
    file_path = './/data//KOBIS_월별박스오피스_22_sh.xlsx'
    sales_22_sh, aud_22_sh = mo.get_data_month(file_path)

    
    aud_18 = (aud_18_fh + aud_18_sh)
    sales_18 = (sales_18_fh + sales_18_sh)

    aud_19 = (aud_19_fh + aud_19_sh)
    sales_19 = (sales_19_fh + sales_19_sh)
    
    aud_20 = (aud_20_fh + aud_20_sh)
    sales_20 = (sales_20_fh + sales_20_sh)
    
    aud_21 = (aud_21_fh + aud_21_sh)
    sales_21 = (sales_21_fh + sales_21_sh)

    aud_22 = (aud_22_fh + aud_22_sh)
    sales_22 = (sales_22_fh + sales_22_sh)
    
    fig_bc, _  = mo.create_combined_graph(sales_18, aud_18, '2018년 월별 매출액/관객수', sales_19, aud_19, '2019년 월별 매출액/관객수')
    st.pyplot(fig_bc)
    
    fig_ac, _  = mo.create_combined_graph(sales_20, aud_20, '2020년 월별 매출액/관객수', sales_21, aud_21, '2021년 월별 매출액/관객수')
    st.pyplot(fig_ac)
    
    fig2022, _ = mo.create_combined_graph(sales_22, aud_22, '2022년 월별 매출액/관객수')
    st.pyplot(fig2022)


def app2():
    
    movie_audience_Korea_2018, movie_sales_Korea_2018 = mo.get_data('.//data//KOBIS_연도별박스오피스_2018_한국.xlsx')
    movie_audience_Korea_2019, movie_sales_Korea_2019 = mo.get_data('.//data//KOBIS_연도별박스오피스_2019_한국.xlsx')
    movie_audience_Korea_2020, movie_sales_Korea_2020 = mo.get_data('.//data//KOBIS_연도별박스오피스_2020_한국.xlsx')
    movie_audience_Korea_2021, movie_sales_Korea_2021 = mo.get_data('.//data//KOBIS_연도별박스오피스_2021_한국.xlsx')
    movie_audience_Korea_2022, movie_sales_Korea_2022 = mo.get_data('.//data//KOBIS_연도별박스오피스_2022_한국.xlsx')
    movie_audience_Korea = [movie_audience_Korea_2018, movie_audience_Korea_2019, movie_audience_Korea_2020, movie_audience_Korea_2021, movie_audience_Korea_2022]
    movie_sales_Korea = [movie_sales_Korea_2018, movie_sales_Korea_2019, movie_sales_Korea_2020, movie_sales_Korea_2021, movie_sales_Korea_2022]

    movie_audience_foreign_2018, movie_sales_foreign_2018 = mo.get_data('.//data//KOBIS_연도별박스오피스_2018_외국.xlsx')
    movie_audience_foreign_2019, movie_sales_foreign_2019 = mo.get_data('.//data//KOBIS_연도별박스오피스_2019_외국.xlsx')
    movie_audience_foreign_2020, movie_sales_foreign_2020 = mo.get_data('.//data//KOBIS_연도별박스오피스_2020_외국.xlsx')
    movie_audience_foreign_2021, movie_sales_foreign_2021 = mo.get_data('.//data//KOBIS_연도별박스오피스_2021_외국.xlsx')
    movie_audience_foreign_2022, movie_sales_foreign_2022 = mo.get_data('.//data//KOBIS_연도별박스오피스_2022_외국.xlsx')
    movie_audience_foreign = [movie_audience_foreign_2018, movie_audience_foreign_2019, movie_audience_foreign_2020, movie_audience_foreign_2021, movie_audience_foreign_2022]
    movie_sales_foreign = [movie_sales_foreign_2018, movie_sales_foreign_2019, movie_sales_foreign_2020, movie_sales_foreign_2021, movie_sales_foreign_2022]

    
    st.write('국적별 영화 매출액 및 관객수')
    
    data2 = {'한국영화매출액': movie_sales_Korea, '외국영화매출액' : movie_sales_foreign}
    nationality_movie_sales = mo.nationality_movie_sales_graph(data2, '국적별 영화매출액')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(nationality_movie_sales)


    data = {'한국영화관람객수': movie_audience_Korea, '외국영화관람객수' : movie_audience_foreign}
    nationality_movie_numbers = mo.nationality_movie_numbers_graph(data, '국적별 영화관람객수')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(nationality_movie_numbers)


    st.write('최근 5년간 일반/독립 영화 매출액 및 관객수')

    data_sales_ind = dict(zip(mo.year, mo.sales_ind))
    data_sales_com = dict(zip(mo.year, mo.sales_com))
    fig_sales, _ = mo.create_sales_graph(data_sales_com, data_sales_ind, '최근 5년 간 일반/독립 영화 매출액(단위:억)')
    st.pyplot(fig_sales)

    data_aud_ind = dict(zip(mo.year, mo.aud_ind))
    data_aud_com = dict(zip(mo.year, mo.aud_com))
    fig_aud, _ = mo.create_aud_graph(data_aud_com, data_aud_ind, '최근 5년 간 일반/독립 영화 관객수(단위:백만)')
    st.pyplot(fig_aud)
    
    