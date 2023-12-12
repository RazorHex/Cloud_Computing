import streamlit as st
import pandas as pd

st.title('Cloud Computing Kelompok 3')
data = pd.read_csv('./data/diskon.csv', on_bad_lines='warn')

fashion = ['baju', 'celana', 'fashion','leather','jeans','gofood','shopeefood']
kosmetik = ['liptint','lipstick','kosmetik','lipstick','makeup','make up']
tiket= ['tiket', 'kendaraan', 'pesawat','bis','bus']
makanan = ['kue','enak','lezat','sehat','madu']

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
st.dataframe(filtered_data[['full_text', 'tweet_url']])
