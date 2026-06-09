import streamlit as st
import pandas as pd
import plotly.express as px
# Dados de exemplo
df = pd.DataFrame({
"Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
"Vendas": [120, 145, 98, 200, 175, 230],
"Clientes": [40, 55, 35, 80, 70, 95],
})

# Cabeçalho
st.title("Painel de Vendas" )
st.write("Resumo dos últimos 6 meses" )
# Exibe o dataframe interativa
st.subheader("Dados brutos" )
st.dataframe(df, use_container_width =True)

# Gráfico de barras com Plotly
st.subheader("Vendas por mês" )
fig_bar = px.bar(df, x="Mês", y="Vendas")
st.plotly_chart (fig_bar, use_container_width =True)

# Gráfico de linhas com Plotly
st.subheader("Tendência de clientes" )
fig_line = px.line(df, x="Mês", y="Clientes",
markers=True)
st.plotly_chart(fig_line, use_container_width =True)