import streamlit as st
import pandas as pd
import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.sidebar.header('Dashboard `version 2`')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('Data 1', 'Data 2'))

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

st.sidebar.markdown('''
---
Tugas Besar Mata Kuliah Cloud Computing
''')

st.title('Cloud Computing Kelompok 3')
data = pd.read_csv('./data/diskon.csv', on_bad_lines='warn')

fashion = ['baju', 'celana', 'fashion','leather','jeans']
kosmetik = ['liptint','lipstick','kosmetik','lipstick','makeup','make up']
tiket= ['tiket', 'kendaraan', 'pesawat','bis','bus']
makanan = ['kue','enak','lezat','sehat','madu','gofood','shopeefood']

selection = ['Fashion', 'Kosmetik', 'Tiket', 'Makanan', 'Lainnya']

filter = st.multiselect('Filter', selection)

def detect_jenis_diskon(text):
    if any(keyword in text for keyword in fashion):
        return 'Fashion'
    elif any(keyword in text for keyword in kosmetik):
        return 'Kosmetik'
    elif any(keyword in text for keyword in makanan):
        return 'Makanan'
    elif any(keyword in text for keyword in tiket):
        return 'Tiket'
    else:
        return 'Lainnya'

data['jenis_diskon'] = data['full_text'].str.lower().apply(detect_jenis_diskon)

filtered_data = data[data['jenis_diskon'].isin(filter)]
count = filtered_data[filtered_data.columns[0]].count()

st.write(f'{filtered_data[filtered_data.columns[0]].count()} Result')
st.dataframe(filtered_data[['full_text', 'tweet_url','username']])
