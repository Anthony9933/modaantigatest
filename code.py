import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configurar o layout da página
st.set_page_config(layout="wide")

# Sidebar (Menu Lateral)
page = st.sidebar.selectbox("Escolha a Página", ["Visão Geral", "Filtros e Dados"])

def show_overview():
    # Visão Geral do Projeto
    st.header("Visão Geral do Projeto")
    st.write("Bem-vindo ao projeto de Visualização de dados da loja Moda Antiga! Este projeto gira em torno da análise e apresentação "
             "de dados do estoque e de vendas de produtos da loja Moda Antiga. O conjunto de dados contém várias colunas fornecendo insights "
             "sobre os produtos e informações relativas a vendas, incluindo data, produtos mais vendidos, melhores e piores meses de venda.")
    
    # Como Funciona
    st.header("Como Funciona")
    st.write("O projeto utiliza um conjunto de dados com informações sobre as vendas e o estoque da loja. Aqui está uma breve visão "
             "geral dos principais componentes:")
    
    # Objetivo do Projeto
    st.header("Objetivo do Projeto")
    st.write("O principal objetivo deste projeto é obter insights pela análise dos dados e gráficos criados. Isso inclui entender "
             "o que os dados estão nos dizendo, identificar e explorar padrões dos compradores "
             "prevendo e criando estratégias para aumentar as vendas.")
    
    # Como Utilizar
    st.header("Como Utilizar")
    st.write("Para explorar o projeto, você pode navegar por diferentes seções usando a barra lateral. As principais seções incluem:")
      
    st.header("Conclusão")
    st.write("Sinta-se à vontade para analisar o conjunto de dados, obter insights e tirar conclusões significativas a partir "
             "dos dados apresentados. Para análises específicas ou dúvidas, novos recursos podem ser incorporados com base nos "
             "objetivos do seu projeto.")
  
    st.write("Aproveite a exploração do projeto!")

def show_filters_data():
    # Título da aplicação
    st.title('Análise de Dados da Loja de Roupas Femininas')
    # Carregar os dados
    df = pd.read_csv('sua_base_de_dados_ajustada.csv')
    # Mostrar os dados
    st.header('Dados Brutos')
    st.write(df)
    
    # Gráfico de vendas por estação
    st.header('Vendas por Estação')
    vendas_por_estacao = df.groupby('Estacao')['PdVenda'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    plt.bar(vendas_por_estacao['Estacao'], vendas_por_estacao['PdVenda'], color='skyblue')
    plt.title('Total de Vendas por Estação')
    plt.xlabel('Estação')
    plt.ylabel('Total de Vendas')
    st.pyplot(plt)
    
    # Gráfico de quantidade de itens vendidos por tecido
    st.header('Quantidade de Itens Vendidos por Tecido')
    quantidade_por_tecido = df.groupby('Tecido')['Quantidade'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    plt.bar(quantidade_por_tecido['Tecido'], quantidade_por_tecido['Quantidade'], color='lightgreen')
    plt.title('Quantidade de Itens Vendidos por Tecido')
    plt.xlabel('Tecido')
    plt.ylabel('Quantidade Vendida')
    st.pyplot(plt)
    
    # Gráfico de lucro por tecido (PdVenda - PdCusto)
    st.header('Lucro por Tecido')
    df['Lucro'] = df['PdVenda'] - df['PdCusto']
    lucro_por_tecido = df.groupby('Tecido')['Lucro'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    plt.bar(lucro_por_tecido['Tecido'], lucro_por_tecido['Lucro'], color='lightcoral')
    plt.title('Lucro por Tecido')
    plt.xlabel('Tecido')
    plt.ylabel('Lucro Total')
    st.pyplot(plt)
    
    # Gráfico de evolução das vendas ao longo do tempo
    st.header('Evolução das Vendas ao Longo do Tempo')
    # Converter a coluna 'Data' para datetime
    #df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m', errors='coerce')
    #df = df.dropna(subset=['Data'])
    #df['AnoMes'] = df['Data'].dt.to_period('M')
    #vendas_mensais = df.groupby('AnoMes')['PdVenda'].sum().reset_index()
    #vendas_mensais['AnoMes'] = vendas_mensais['AnoMes'].astype(str)
    plt.figure(figsize=(12, 6))
    plt.plot(vendas_mensais['AnoMes'], vendas_mensais['PdVenda'], marker='o', linestyle='-')
    plt.title('Evolução das Vendas ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Total de Vendas')
    plt.xticks(rotation=45)
    plt.grid(True)
    st.pyplot(plt)
    
    # Gráfico de relação entre quantidade e preço de custo
    st.header('Relação entre Quantidade e Preço de Custo')
    plt.figure(figsize=(10, 6))
    plt.scatter(df['PdCusto'], df['Quantidade'], alpha=0.5)
    plt.title('Relação entre Quantidade e Preço de Custo')
    plt.xlabel('Preço de Custo')
    plt.ylabel('Quantidade')
    st.pyplot(plt)

# Página de Visão Geral
if page == "Visão Geral":
    show_overview()

# Página de Filtros e Dados
elif page == "Filtros e Dados":
    show_filters_data()
