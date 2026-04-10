import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

engine = create_engine('postgresql://iot_user:iot_pass@localhost:5432/iot_db')

def load_data(view):
    return pd.read_sql(f"SELECT * FROM {view}", engine)

st.title("Dashboard IoT")

df1 = load_data('avg_temp_por_dispositivo')
st.plotly_chart(px.bar(df1, x='device_id', y='avg_temp'))

df2 = load_data('leituras_por_hora')
st.plotly_chart(px.line(df2, x='hora', y='contagem'))

df3 = load_data('temp_max_min_por_dia')
st.plotly_chart(px.line(df3, x='data', y=['temp_max', 'temp_min']))
