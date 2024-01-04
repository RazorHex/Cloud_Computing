import streamlit as st
import pandas as pd
import numpy as np
import plost
import altair as alt

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.sidebar.header('Dashboard `Cloud Computing`')

# st.sidebar.subheader('Heat map parameter')
# time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

# st.sidebar.subheader('Donut chart parameter')
# donut_theta = st.sidebar.selectbox('Select data', ('Data 1', 'Data 2'))

st.sidebar.subheader('Pilih Data Yang Diinginkan')
plot_data = st.sidebar.multiselect('Select data', ['Data 1', 'Data 2'], ['Data 2', 'Data 1'])
plot_height = st.sidebar.slider('Banyak Data Yang Ingin Ditampilkan', 50, 500, 50)

st.sidebar.markdown('''
---
Tugas Besar Mata Kuliah Cloud Computing
''')
st.sidebar.write("Ahda Akmalul Ilmi <br> Fabiano Abbey Karo Sekali <br> Danny Aulia", unsafe_allow_html=True)




st.title('Cloud Computing Kelompok 3')
data = pd.read_csv('./data/diskon.csv', on_bad_lines='warn')
data2 = pd.read_csv('./data/diskon2.csv', on_bad_lines='warn')

fashion = ['baju', 'celana', 'fashion','leather','jeans']
kosmetik = ['liptint','lipstick','kosmetik','lipstick','makeup','make up']
tiket= ['tiket', 'kendaraan', 'pesawat','bis','bus']
makanan = ['kue','enak','lezat','sehat','madu','gofood','shopeefood']

selection = ['Fashion', 'Kosmetik', 'Tiket', 'Makanan', 'Lainnya']
# selection_fashion = ['Fashion']
# selection_kosmetik = ['Kosmetik']
# selection_Tiket = ['Tiket']
# selection_Makanan = ['Makanan']
# selection_Lainnya = ['Lainnya']

filter = st.multiselect('Filter', selection)
if filter and not plot_data:
    st.warning("Pilih opsi multiselect di Bagian Dashboard.")
    st.warning("Icon Dashboard berada di Ujung kiri atas [>]")

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

def process_data(data, filter, limit):
    filtered_data = data[data['jenis_diskon'].isin(filter)]
    return filtered_data[['full_text', 'tweet_url', 'username']].head(limit)

if 'Data 1' in plot_data:
    data['jenis_diskon'] = data['full_text'].str.lower().apply(detect_jenis_diskon)

#Data 1
    filtered_data = process_data(data, filter, plot_height)
    count = filtered_data[filtered_data.columns[0]].count()

    c1,c2 = st.columns((8.5,1.5))
    with c1 :
        st.write(f'{filtered_data[filtered_data.columns[0]].count()} Hasil')
        st.table(filtered_data[['full_text', 'tweet_url','username']].head(plot_height))
    with c2 :
        st.write('Total Keseluruhan Data 1')
        jumlah_data_per_kategori = data[data['jenis_diskon'].isin(selection)]['jenis_diskon'].value_counts()
        st.write(jumlah_data_per_kategori)

    st.write("*Bar Chart Data 1*")
    data_source = pd.DataFrame({
        "Jumlah": [jumlah_data_per_kategori[2], jumlah_data_per_kategori[4], jumlah_data_per_kategori[1],jumlah_data_per_kategori[3]],
        "Opsi": ['Fashion', 'Kosmetik', 'Tiket', 'Makanan']
    })


    bar_chart = alt.Chart(data_source).mark_bar().encode(
        x=alt.X("Opsi:N", title="Kategori Diskon"),
        y=alt.Y("sum(Jumlah):Q", title="Total Jumlah"),
        color="Opsi:N"
    )
    st.altair_chart(bar_chart, use_container_width=True)

#Data 2
if 'Data 2' in plot_data:
    data2['jenis_diskon'] = data2['full_text'].str.lower().apply(detect_jenis_diskon)

    filtered_data2 = process_data(data2, filter, plot_height)
    count2 = filtered_data2[filtered_data2.columns[0]].count()

    c1,c2 = st.columns((8.5,1.5))
    with c1 :
        st.write(f'{filtered_data2[filtered_data2.columns[0]].count()} Hasil')
        st.table(filtered_data2[['full_text', 'tweet_url','username']].head(plot_height))
    with c2 :
        st.write('Total Keseluruhan Data 2')
        jumlah_data_per_kategori2 = data2[data2['jenis_diskon'].isin(selection)]['jenis_diskon'].value_counts()
        st.write(jumlah_data_per_kategori2)

    st.write("*Bar Chart Data 2*")
    data_source2 = pd.DataFrame({
        "Jumlah": [jumlah_data_per_kategori2[2], jumlah_data_per_kategori2[4], jumlah_data_per_kategori2[1],jumlah_data_per_kategori2[3]],
        "Opsi": ['Fashion', 'Kosmetik', 'Tiket', 'Makanan']
    })

    bar_chart2= alt.Chart(data_source2).mark_bar().encode(
        x=alt.X("Opsi:N", title="Kategori Diskon"),
        y=alt.Y("sum(Jumlah):Q", title="Total Jumlah"),
        color="Opsi:N"
    )
    st.altair_chart(bar_chart2, use_container_width=True)