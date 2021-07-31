import streamlit as st
import pandas as pd
import csv
import datetime
import base64


st.title('Uber検索順位チェッカー')
st.subheader('・全てのデータを見る')

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

#選択なしの場合の処理
if selected_city == '-':
    use_df = df_prefecture
elif selected_city != '-' and selected_town == '-':
    use_df = df_city
else:
    use_df = df_town

#日付の絞り込み
selected_date = st.sidebar.date_input(
     "日付",
    datetime.date(2021, 7, 29)
    )
use_df['date'] = pd.to_datetime(use_df['date'])
flag4 = use_df['date'].isin([selected_date])
df_date = use_df[flag4]
#カテゴリの絞り込み
categories = ['最も人気の料理', 'ハンバーガー', 'ファストフード']
selected_category = st.sidebar.selectbox('カテゴリーの選択', categories)
flag5 = df_date['category'].isin([selected_category])
df_category = df_date[flag5]

#アウトプット用df作成
ranks = df_category['rank']
rank_list = list(ranks)

urls = df_category['url']
url_list = list(urls)

names = df_category['name']
name_list = list(names)

final_df = pd.DataFrame(index=ranks, columns=[])
final_df['店舗名'] = names
final_df['URL'] = urls

#csvダウンロードメソッド
def filedownload(df):
    csv = df.to_csv(index=True)
    b64 = base64.b64encode(csv.encode('shift jis')).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="ranking.csv">Download CSV File</a>'
    return href

#ランキング
if st.sidebar.button('適用'):
    st.write('住所：'+ selected_prefecture + selected_city + selected_town)
    st.dataframe(final_df, 10000, 200)
    st.markdown(filedownload(final_df), unsafe_allow_html=True)
else:
    st.write('左側で条件を選択し、適用を押してください')
    st.write('ランキングが表示されます(csv出力も可能)')


#店舗の検索
st.subheader('・あなたの店舗と競合を知る')
sort_name =st.text_input(
    label = "店舗名（もしくはキーワード）を入力してください。あなたの店舗の順位がわかります。ex.(うどん)"
)
sort_df = final_df[final_df['店舗名'].str.contains(sort_name, na=False)]
if len(sort_name) > 0:
    st.dataframe(sort_df)
    st.markdown(filedownload(sort_df), unsafe_allow_html=True)

