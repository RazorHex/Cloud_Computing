import streamlit as st
import pandas as pd

st.title('Hello world')
data = pd.read_csv('./data/diskon.csv', on_bad_lines='warn')

input = st.text_input('Keyword')

checks = [input in text for text in data['full_text']]

# [st.write(data['full_text'][i]) for i, x in enumerate(checks) if x == True]

for i, x in enumerate(checks):
  if x == True:
    st.write(data['full_text'][i])
    st.divider()


st.dataframe(data)
