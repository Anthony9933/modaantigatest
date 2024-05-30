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

# Processar os dados para obter vendas anuais
df['Ano'] = df['Data'].dt.year
df['VendaTotal'] = df['Quantidade'] * df['PdVenda']
vendas_anuais = df.groupby('Ano')['VendaTotal'].sum().reset_index()

# Configurar o título da aplicação
st.title('Evolução das Vendas ao Longo dos Anos')

# Criar o gráfico de evolução das vendas
fig = px.line(vendas_anuais, x='Ano', y='VendaTotal', title='Evolução das Vendas Anuais')

# Mostrar o gráfico no Streamlit
st.plotly_chart(fig)

