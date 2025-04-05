import streamlit as st
import pandas as pd

st.write("# Dashboard de Gestão de Dados")

df = pd.read_csv('car_ad.csv', encoding="ISO-8859-1")

car = st.sidebar.selectbox('Marca', df['car'].unique())

df_filtered = df[df['car'] == car]

st.dataframe(df_filtered)