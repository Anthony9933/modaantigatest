import streamlit as st
import pandas as pd
import plotly.express as px

# Função para carregar os dados
@st.cache
def load_data():
    # Substitua 'seu_arquivo.csv' pelo caminho para o seu arquivo de dados
    df = pd.read_csv('sua_base_de_dados_ajustada.csv')
    df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d')
    return df

# Carregar os dados
df = load_data()

# Processar os dados para obter vendas anuais e mensais
df['Ano'] = df['Data'].dt.year
df['Mes'] = df['Data'].dt.month
df['VendaTotal'] = df['Quantidade'] * df['PdVenda']

# Agrupar por ano e mês e somar as vendas
vendas_mensais = df.groupby(['Ano', 'Mes'])['VendaTotal'].sum().reset_index()

# Criar uma coluna de data fictícia para plotar
vendas_mensais['AnoMes'] = pd.to_datetime(vendas_mensais[['Ano', 'Mes']].assign(DIA=1))

# Configurar o título da aplicação
st.title('Evolução das Vendas ao Longo dos Anos e Meses')

# Criar o gráfico de evolução das vendas
fig = px.line(vendas_mensais, x='AnoMes', y='VendaTotal', title='Evolução das Vendas Mensais', labels={'AnoMes': 'Ano e Mês', 'VendaTotal': 'Vendas Totais'})

# Mostrar o gráfico no Streamlit
st.plotly_chart(fig)
