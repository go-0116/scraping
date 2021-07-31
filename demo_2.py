from os import terminal_size
import streamlit as st
import pandas as pd
import csv
import datetime
import base64
import altair as alt

st.title('Uber検索順位チェッカー')
st.subheader('・順位の推移を知る')

df = pd.read_csv('base.csv', encoding="shift_jis")
prefectures = df['prefecture']
prefecture_list = list(set(prefectures))

st.sidebar.header('条件選択')
selected_prefecture = st.sidebar.selectbox('都道府県', prefecture_list)
#都道府県で絞り込み
flag = df['prefecture'].isin([selected_prefecture])
df_prefecture = df[flag]
cities = df_prefecture['city']
city_list = list(set(cities))
city_list.append('-')
selected_city = st.sidebar.selectbox('市区', city_list)
#市で絞り込み
flag2 = df_prefecture['city'].isin([selected_city])
df_city = df_prefecture[flag2]
towns = df_city['town']
town_list = list(set(towns))
town_list.append('-')
selected_town = st.sidebar.selectbox('町村', town_list)
#町で絞り込み
flag3 = df_city['town'].isin([selected_town])
df_town = df_city[flag3]

use_df = df_town
#日付で絞り込み
selected_date_1 = st.sidebar.date_input(
     "日付（前）",
    datetime.date(2021, 7, 1)
    )

selected_date_2 = st.sidebar.date_input(
     "日付（後）",
    datetime.date(2021, 7, 29)
    )

use_df['date'] = pd.to_datetime(use_df['date'])
df_date = use_df[(use_df['date'] >= pd.Timestamp(selected_date_1)) & (use_df['date'] < pd.Timestamp(selected_date_2))]

#カテゴリで絞り込み
categories = ['最も人気の料理', 'ハンバーガー', 'ファストフード']
selected_category = st.sidebar.selectbox('カテゴリーの選択', categories)
flag5 = df_date['category'].isin([selected_category])
df_category = df_date[flag5]

#レストラン名で絞り込み
restaurants = list(set(df_category['name']))
selected_restaurant = st.sidebar.selectbox('レストランの選択', restaurants)
flag6 = df_category['name'].isin([selected_restaurant])
df_restaurant = df_category[flag6]
df_restaurant_1 = df_restaurant.sort_values('date')

#アウトプット用df作成
dates = df_restaurant_1['date']
date_list = list(dates)

ranks = df_restaurant_1['rank']
rank_list = list(ranks)

final_df = pd.DataFrame(index=[], columns=[])
final_df['日付'] = date_list
final_df['ランク'] = rank_list

#折れ線グラフ作成
line_chart = alt.Chart(final_df).mark_line(color='steelblue').encode(
    x=alt.X('日付'),
    y=alt.Y('ランク')
    ).properties(
    width=800,
    height=400
    ).interactive()


if st.sidebar.button('適用'):
    st.altair_chart(line_chart)
else:
    st.write('左側で条件を選択し、適用を押してください')
    st.write('期間内の順位が表示されます')







