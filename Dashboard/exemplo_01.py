import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_KEY")

# Criar conexão
engine = create_engine(DATABASE_URL)
df = pd.read_sql("SELECT * FROM bitcoin_dados ORDER BY timestamp DESC", con=engine)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Configurações da página
st.set_page_config(page_title="Dashboard Bitcoin", layout="wide")

# Título
st.title("🪙 Painel de Monitoramento - Bitcoin em Tempo Real")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("💰 Valor Atual (USD)", f"${df.iloc[0]['valor']:.2f}")
col2.metric("🕒 Última Atualização", df.iloc[0]['timestamp'].strftime("%d/%m/%Y %H:%M:%S"))
col3.metric("📊 Total de Registros", len(df))

st.markdown("---")

# Gráfico de linha
st.subheader("📈 Evolução do Valor do Bitcoin")
df_ordenado = df.sort_values("timestamp")
st.line_chart(df_ordenado.set_index("timestamp")["valor"])

# Gráfico de pizza (quantidade por moeda)
st.subheader("📊 Distribuição de Moedas (Base x Currency)")
moeda_counts = df['moeda'].value_counts()
st.pyplot(
    moeda_counts.plot.pie(autopct='%1.1f%%', figsize=(5, 5), ylabel='', title='Moeda Final').get_figure()
)

# Tabela dos últimos registros
st.subheader("📋 Registros Recentes")
st.dataframe(df.head(10), use_container_width=True)
