# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 10:42:14 2023

@author: Jung
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter, MaxNLocator
from matplotlib.font_manager import FontProperties
from matplotlib import font_manager, rc


'''오전석 조원'''
def get_data(file_path):
    df = pd.read_excel(file_path)
    df.drop(df.index[0:3], inplace=True)
    df = df.rename(columns=df.iloc[0])
    df.drop(df.index[0], inplace=True)
    df = df[df['매출액 점유율'] != 0]
    df = df.reset_index(drop=True)
    df.drop(df.index[-1], inplace=True)
    return df['매출액'].sum(), df['관객수'].sum()

movie_sales_2018, movie_audience_2018 = get_data('.//data//KOBIS_연도별박스오피스_2018.xlsx')
movie_sales_2019, movie_audience_2019 = get_data('.//data//KOBIS_연도별박스오피스_2019.xlsx')
movie_sales_2020, movie_audience_2020 = get_data('.//data//KOBIS_연도별박스오피스_2020.xlsx')
movie_sales_2021, movie_audience_2021 = get_data('.//data//KOBIS_연도별박스오피스_2021.xlsx')
movie_sales_2022, movie_audience_2022 = get_data('.//data//KOBIS_연도별박스오피스_2022.xlsx')
movie_audience = [movie_audience_2018, movie_audience_2019, movie_audience_2020, movie_audience_2021, movie_audience_2022]
movie_sales = [movie_sales_2018, movie_sales_2019, movie_sales_2020, movie_sales_2021, movie_sales_2022]

movie_audience_Korea_2018, movie_sales_Korea_2018 = get_data('.//data//KOBIS_연도별박스오피스_2018_한국.xlsx')
movie_audience_Korea_2019, movie_sales_Korea_2019 = get_data('.//data//KOBIS_연도별박스오피스_2019_한국.xlsx')
movie_audience_Korea_2020, movie_sales_Korea_2020 = get_data('.//data//KOBIS_연도별박스오피스_2020_한국.xlsx')
movie_audience_Korea_2021, movie_sales_Korea_2021 = get_data('.//data//KOBIS_연도별박스오피스_2021_한국.xlsx')
movie_audience_Korea_2022, movie_sales_Korea_2022 = get_data('.//data//KOBIS_연도별박스오피스_2022_한국.xlsx')
movie_audience_Korea = [movie_audience_Korea_2018, movie_audience_Korea_2019, movie_audience_Korea_2020, movie_audience_Korea_2021, movie_audience_Korea_2022]
movie_sales_Korea = [movie_sales_Korea_2018, movie_sales_Korea_2019, movie_sales_Korea_2020, movie_sales_Korea_2021, movie_sales_Korea_2022]

movie_audience_foreign_2018, movie_sales_foreign_2018 = get_data('.//data//KOBIS_연도별박스오피스_2018_외국.xlsx')
movie_audience_foreign_2019, movie_sales_foreign_2019 = get_data('.//data//KOBIS_연도별박스오피스_2019_외국.xlsx')
movie_audience_foreign_2020, movie_sales_foreign_2020 = get_data('.//data//KOBIS_연도별박스오피스_2020_외국.xlsx')
movie_audience_foreign_2021, movie_sales_foreign_2021 = get_data('.//data//KOBIS_연도별박스오피스_2021_외국.xlsx')
movie_audience_foreign_2022, movie_sales_foreign_2022 = get_data('.//data//KOBIS_연도별박스오피스_2022_외국.xlsx')
movie_audience_foreign = [movie_audience_foreign_2018, movie_audience_foreign_2019, movie_audience_foreign_2020, movie_audience_foreign_2021, movie_audience_foreign_2022]
movie_sales_foreign = [movie_sales_foreign_2018, movie_sales_foreign_2019, movie_sales_foreign_2020, movie_sales_foreign_2021, movie_sales_foreign_2022]


def get_data_COVID19_2020(file_path):
    df = pd.read_excel(file_path)
    covid_2020 = df[df['전국 기준일'].str.startswith(('20.', '2020.'))]['전국 추가 확진']
    covid_2020 = pd.DataFrame(covid_2020)
    covid_2020_number = covid_2020['전국 추가 확진'].sum()
    return covid_2020_number

def get_data_COVID19_2021(file_path):
    df = pd.read_excel(file_path)
    covid_2021 = df[df['전국 기준일'].str.startswith(('2021.'))]['전국 추가 확진']
    covid_2021 = pd.DataFrame(covid_2021)
    covid_2021_number = covid_2021['전국 추가 확진'].sum()
    return covid_2021_number

def get_data_COVID19_2022(file_path):
    df = pd.read_excel(file_path)
    covid_2022 = df[df['전국 기준일'].str.startswith(('2022.'))]['전국 추가 확진']
    covid_2022 = pd.DataFrame(covid_2022)
    covid_2022_number = covid_2022['전국 추가 확진'].sum()
    return covid_2022_number

covid_2020_number = get_data_COVID19_2020('.//data//코로나19_확진자_발생동향.xlsx')
covid_2021_number = get_data_COVID19_2021('.//data//코로나19_확진자_발생동향.xlsx')
covid_2022_number = get_data_COVID19_2022('.//data//코로나19_확진자_발생동향.xlsx')

covid_number = [covid_2020_number, covid_2021_number, covid_2022_number]


def year_movie_graph(data1, data2, title):
    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)

    index = [2018, 2019, 2020, 2021, 2022]
    data1 = {'영화관람객수': movie_audience}
    df1 = pd.DataFrame(data1, index=index)
    
    data2 = {'영화매출액': movie_sales}
    df2 = pd.DataFrame(data2, index=index)
    
    fig = plt.figure(figsize=(10,8)) ## Figure 생성
    fig.set_facecolor('white') ## Figure 배경색 지정
    ax1 = fig.add_subplot() ## axes 생성
    colors = sns.color_palette('autumn', len(index)) ## 바 차트 색상
    xtick_label_position = list(range(len(index))) ## x축 눈금 라벨이 표시될 x좌표
    ax1.set_xticks(xtick_label_position) ## x축 눈금
    ax1.set_xticklabels(index, fontsize=15) ## x축 눈금 라벨
    ax1.bar(xtick_label_position, df1['영화관람객수'], color=colors) ## 바차트 출력
    ax1.set_xlabel('년도', fontsize=15)
    ax1.set_ylabel('영화관람객수\n(단위 : 억명)', fontsize=15)
    color = 'blue'
    ax2 = ax1.twinx() ## 새로운 axis 생성
    ax2.plot(xtick_label_position, df2['영화매출액'], color=color, linestyle='--', marker='o') ## 선 그래프
    ax2.tick_params(axis='y', labelcolor=color) ## 눈금 라벨 색상 지정
    ax2.set_ylabel('영화매출액\n(단위 : 조)', fontsize=15, rotation = 270, color = 'blue', labelpad=40)
    plt.title('연도별 영화관람객수/영화매출액', fontsize=20)
    plt.show()

def nationality_movie_numbers_graph(data, title):
    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)
    
    data = {'한국영화관람객수': movie_audience_Korea, '외국영화관람객수' : movie_audience_foreign}
    index = [2018, 2019, 2020, 2021, 2022]
    df = pd.DataFrame(data, index=index)
    
    width = 0.35  # 막대 너비
    plt.figure(figsize=(10, 8))

    plt.bar([i - width/2 for i in df.index], df['한국영화관람객수'], width, label='한국영화관람객수')
    plt.bar([i + width/2 for i in df.index], df['외국영화관람객수'], width, label='외국영화관람객수')
    plt.xlabel('년도', fontsize=13)
    plt.ylabel('국적별영화관람객수\n(단위 : 억명)', fontsize=13)
    plt.title('국적별 영화관람객수', fontsize=20)
    plt.legend()
    plt.show()
    
def nationality_movie_sales_graph(data, title):
    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)
        
    data = {'한국영화매출액': movie_sales_Korea, '외국영화매출액' : movie_sales_foreign}
    index = [2018, 2019, 2020, 2021, 2022]
    df = pd.DataFrame(data, index=index)
    
    width = 0.35  # 막대 너비
    plt.figure(figsize=(10, 8))
    
    plt.bar([i - width/2 for i in df.index], df['한국영화매출액'], width,  label='한국영화매출액')
    plt.bar([i + width/2 for i in df.index], df['외국영화매출액'], width,  label='외국영화매출액')
    plt.xlabel('년도', fontsize=13)
    plt.ylabel('국적별영화매출액\n(단위 : 천억)', fontsize=13)
    plt.title('국적별 영화매출액', fontsize=20)
    plt.legend()
    plt.show()

def COVID19_numbers_graph(data, title):
    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)
    
    data = {'코로나확진자수': covid_number}
    index = [2020, 2021, 2022]
    df = pd.DataFrame(data, index=index)


    plt.plot(df.index, df['코로나확진자수'], marker='o')  # marker 옵션으로 데이터 포인트를 표시할 수 있음


    plt.title('코로나 확진자수', fontsize=20)
    plt.xlabel('년도', fontsize=13)
    plt.ylabel('코로나 확진자수\n(단위 : 천만명)', fontsize=13)
    plt.xticks(index, fontsize=15) 

    plt.show()


'''정은주 조장'''

def get_data_month(file_path):
    df = pd.read_excel(file_path)
    df.drop(df.index[0:5], inplace=True)
    df = df.rename(columns=df.iloc[0])
    df.drop(df.index[0], inplace=True)
    df = df[df['매출액 점유율'] != 0]
    df = df.reset_index(drop=True)
    idx = df[df['순위'] == '합계']
    
    df_month = []
    for i in range(len(idx) - 1):
        start_idx = idx.index[i] + 5
        end_idx = idx.index[i + 1]
        df_month.append(df[start_idx:end_idx])
    
    start_idx = 0
    end_idx = idx.index[0]
    df_month.insert(0, df[start_idx:end_idx])
    df_month.reverse()
    
    sales = []
    aud = []
    for df_m in df_month:
        sales_sum = df_m['매출액 '].sum()
        aud_sum = df_m['관객수 '].sum()
        sales.append(sales_sum)
        aud.append(aud_sum)
    
    return sales, aud



def create_combined_graph(sales_data_1, aud_data_1, title_1, sales_data_2=None, aud_data_2=None, title_2=None):
    font_name = './NanumGothic.ttf'
    fontprop = font_manager.FontProperties(fname=font_name, size=20)
    month = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']

    fig, axes = plt.subplots(1, 2, figsize=(16, 8))  # 1 행 2 열의 서브플롯 생성
    fig.set_facecolor('white')

    colors = sns.color_palette('summer', len(month))
    xtick_label_position = list(range(len(month)))

    # 첫 번째 그래프 그리기
    ax = axes[0]
    ax.bar(xtick_label_position, sales_data_1, color=colors)
    ax.set_xticks(xtick_label_position)
    ax.set_xticklabels(month)
    ax.set_ylabel('매출액(단위:천억)', color='black', fontsize=12, fontproperties=fontprop)

    ax2 = ax.twinx()
    ax2.plot(xtick_label_position, aud_data_1, color='blue', linestyle='--', marker='o')
    ax2.tick_params(axis='y', labelcolor='blue')
    ax2.set_ylabel('관객수(단위:천만)', color='blue', fontsize=12, fontproperties=fontprop)

    ax.set_title(title_1, fontproperties=fontprop)

    # 두 번째 그래프가 있는 경우에만 그리기
    if sales_data_2 is not None and aud_data_2 is not None and title_2 is not None:
        ax = axes[1]
        ax.bar(xtick_label_position, sales_data_2, color=colors)
        ax.set_xticks(xtick_label_position)
        ax.set_xticklabels(month)
        ax.set_ylabel('매출액(단위:천억)', color='black', fontsize=12, fontproperties=fontprop)

        ax2 = ax.twinx()
        ax2.plot(xtick_label_position, aud_data_2, color='blue', linestyle='--', marker='o')
        ax2.tick_params(axis='y', labelcolor='blue')
        ax2.set_ylabel('관객수(단위:천만)', color='blue', fontsize=12, fontproperties=fontprop)

        ax.set_title(title_2, fontproperties=fontprop)
    else:
        # 두 번째 그래프가 필요 없을 때는 해당 서브플롯을 비활성화
        axes[1].axis('off')
        
    plt.tight_layout()
    return fig, (ax)



def get_data_ci(file_path):
    df = pd.read_excel(file_path)
    df.drop(df.index[0:3], inplace=True)
    df = df.rename(columns=df.iloc[0])
    df.drop(df.index[0], inplace=True)
    df = df[df['매출액 점유율'] != 0]
    df = df.reset_index(drop=True)
    df.drop(df.index[-1], inplace=True)
    return df['매출액'].sum(), df['관객수'].sum()

sales_ind_18, aud_ind_18 = get_data_ci('.//data//KOBIS_연도별박스오피스_독립_18.xlsx')
sales_com_18, aud_com_18 = get_data_ci('.//data//KOBIS_연도별박스오피스_일반_18.xlsx')

sales_ind_19, aud_ind_19 = get_data_ci('.//data//KOBIS_연도별박스오피스_독립_19.xlsx')
sales_com_19, aud_com_19 = get_data_ci('.//data//KOBIS_연도별박스오피스_일반_19.xlsx')

sales_ind_20, aud_ind_20 = get_data_ci('.//data//KOBIS_연도별박스오피스_독립_20.xlsx')
sales_com_20, aud_com_20 = get_data_ci('.//data//KOBIS_연도별박스오피스_일반_20.xlsx')

sales_ind_21, aud_ind_21 = get_data_ci('.//data//KOBIS_연도별박스오피스_독립_21.xlsx')
sales_com_21, aud_com_21 = get_data_ci('.//data//KOBIS_연도별박스오피스_일반_21.xlsx')

sales_ind_22, aud_ind_22 = get_data_ci('.//data//KOBIS_연도별박스오피스_독립_22.xlsx')
sales_com_22, aud_com_22 = get_data_ci('.//data//KOBIS_연도별박스오피스_일반_22.xlsx')


sales_ind = [sales_ind_18, sales_ind_19, sales_ind_20, sales_ind_21, sales_ind_22]
aud_ind = [aud_ind_18, aud_ind_19, aud_ind_20, aud_ind_21, aud_ind_22]

sales_com = [sales_com_18, sales_com_19, sales_com_20, sales_com_21, sales_com_22]
aud_com = [aud_com_18, aud_com_19, aud_com_20, aud_com_21, aud_com_22]

year = [2018, 2019, 2020, 2021, 2022]




def create_sales_graph(data, data2, title):
    font_name = './NanumGothic.ttf'
    fontprop = FontProperties(fname=font_name, size=20)

    width = 0.35
    sns.set_theme(style="white", context="talk")
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True,figsize=(10,8))
    fig.subplots_adjust(hspace=0.1)  
    
    ax1.bar([i - width/2 for i, _ in enumerate(data.keys())], data.values(), width)
    ax1.bar([i + width/2 for i, _ in enumerate(data2.keys())], data2.values(), width)

    ax1.set_ylim(400000000000, 1900000000000)
    ax2.set_ylim(0, 70000000000)

    ax2.bar([i - width/2 for i, _ in enumerate(data.keys())], data.values(), width, label='일반영화매출액')
    ax2.bar([i + width/2 for i, _ in enumerate(data2.keys())], data2.values(), width, label='독립영화매출액')

    ax1.spines['bottom'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax1.tick_params(labeltop=False)
    ax2.xaxis.tick_bottom()

    ax2.set_xticks([i for i, _ in enumerate(data.keys())]) 
    ax2.set_xticklabels(data.keys()) # xtick 연도로 변경

    def y_tick_formatter(x, pos):
        return f'{int(x/100000000):,}'  # 천 단위 콤마 표시

    ax1.yaxis.set_major_formatter(FuncFormatter(y_tick_formatter))
    ax2.yaxis.set_major_formatter(FuncFormatter(y_tick_formatter))

    ax1.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=4)) # ax1의 ytick 개수 설정


    kwargs = dict(marker=[(-1, -0.5), (1, 0.5)], markersize=12,
                  linestyle="none", color='k', mec='k', mew=1, clip_on=False)
    ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
    ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

    plt.suptitle(title, fontproperties = fontprop)

    fontprop2 = font_manager.FontProperties(fname = font_name, size=13)
    plt.legend(loc=(0.75, 1.8), prop=fontprop2)
    return fig, (ax1, ax2)


def create_aud_graph(data, data2, title):
    font_name = './NanumGothic.ttf'
    fontprop = FontProperties(fname=font_name, size=20)

    width = 0.35
    sns.set_theme(style="white", context="talk")
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True,figsize=(10,8))
    fig.subplots_adjust(hspace=0.1)  
    
    ax1.bar([i - width/2 for i, _ in enumerate(data.keys())], data.values(), width)
    ax1.bar([i + width/2 for i, _ in enumerate(data2.keys())], data2.values(), width)

    ax1.set_ylim(40000000, 250000000)
    ax2.set_ylim(0, 9000000)

    ax2.bar([i - width/2 for i, _ in enumerate(data.keys())], data.values(), width, label='일반영화관객수')
    ax2.bar([i + width/2 for i, _ in enumerate(data2.keys())], data2.values(), width, label='독립영화관객수')

    ax1.spines['bottom'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax1.tick_params(labeltop=False)
    ax2.xaxis.tick_bottom()

    ax2.set_xticks([i for i, _ in enumerate(data.keys())]) 
    ax2.set_xticklabels(data.keys()) # xtick 연도로 변경

    def y_tick_formatter(x, pos):
        return f'{int(x/1000000):,}'  # 천 단위 콤마 표시

    ax1.yaxis.set_major_formatter(FuncFormatter(y_tick_formatter))
    ax2.yaxis.set_major_formatter(FuncFormatter(y_tick_formatter))

    ax1.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=4)) # ax1의 ytick 개수 설정


    kwargs = dict(marker=[(-1, -0.5), (1, 0.5)], markersize=12,
                  linestyle="none", color='k', mec='k', mew=1, clip_on=False)
    ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
    ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

    plt.suptitle(title, fontproperties = fontprop)

    fontprop2 = font_manager.FontProperties(fname = font_name, size=13)
    plt.legend(loc=(0.75, 1.8), prop=fontprop2)
    return fig, (ax1, ax2)




