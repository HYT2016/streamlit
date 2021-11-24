import time

import streamlit as st

import numpy as np
import pandas as pd

st.title('hi~~~')
st.write("嘗試創建**表格**：")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
df

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [22.7, 120.3],
    columns=['lat', 'lon'])
st.map(map_data)

if st.checkbox('顯示地圖圖表'):
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [22.7, 120.3],
        columns=['lat', 'lon'])
    st.map(map_data)

    option = st.selectbox(
    '你喜歡哪種動物？',
    ['狗', '貓', '鸚鵡', '天竺鼠'])
'你的答案：', option