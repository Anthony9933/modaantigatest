import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


df = pd.read_csv('sua_base_de_dados_ajustada.csv')
# Converter a coluna 'Data' para datetime
df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
df = df.dropna(subset=['Data'])  # Eliminar linhas com 'Data' nula

# Verificar se ainda existem datas nulas
st.write("Existem datas nulas:", df['Data'].isnull().any())

df['AnoMes'] = df['Data'].dt.to_period('M').dt.to_timestamp()  # Converter para o primeiro dia do mês
vendas_mensais = df.groupby('AnoMes').agg({'PdVenda': 'sum'}).reset_index()

plt.figure(figsize=(12, 6))
plt.plot(vendas_mensais['AnoMes'], vendas_mensais['PdVenda'], marker='o', linestyle='-')
plt.title('Evolução das Vendas ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)
plt.grid(True)
st.pyplot(plt)
