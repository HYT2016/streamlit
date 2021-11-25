import time

import streamlit as st

import numpy as np
import pandas as pd

st.title('DEMO')

# # @st.cache
# def load_data(nrows):
#     data = pd.read_csv("tryexcel.csv", nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     return data


# # Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Loading data...')
# # Load 5 rows of data into the dataframe.
# data = load_data(5)
# # Notify the reader that the data was successfully loaded.
# data_load_state.text("Done! ")




# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)


import time

import streamlit as st

import numpy as np
import pandas as pd



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

if st.checkbox('show map'):
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [22.7, 120.3],
        columns=['lat', 'lon'])
    st.map(map_data)