import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

st.set_page_config(page_title="Dashboard IoT", layout="wide")

engine = create_engine('postgresql://iot_user:iot_pass@postgres:5432/iot_db')

def load_data(view):
    try:
        return pd.read_sql(f"SELECT * FROM {view}", engine)
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()

st.title(" Dashboard de Temperaturas IoT")

# Gráfico 1
st.subheader("Média de Temperatura por Dispositivo")
df1 = load_data('avg_temp_por_dispositivo')
if not df1.empty:
    st.plotly_chart(px.bar(df1, x='device_id', y='avg_temp'))

# Gráfico 2
st.subheader("Leituras por Hora")
df2 = load_data('leituras_por_hora')
if not df2.empty:
    st.plotly_chart(px.line(df2, x='hora', y='contagem'))

# Gráfico 3
st.subheader("Temperatura por Dia")
df3 = load_data('temp_max_min_por_dia')
if not df3.empty:
    st.plotly_chart(px.line(df3, x='data', y=['temp_max', 'temp_min']))