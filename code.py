import streamlit as st
import pandas as pd 
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

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
    st.header("Filtros e Dados")
    
    # Carregar dados
    data = '''<dados.csv>'''
    df = pd.read_csv(pd.compat.StringIO(data))
    
    # Preprocessamento de dados
    df['Total_Venda'] = df['Quantidade'] * df['Preço_Venda']
    
    # Sidebar para filtro por estação
    estacao = st.sidebar.selectbox('Selecionar Estação', df['Estacao'].unique())
    
    # Filtrar dados pela estação selecionada
    df_filtered = df[df['Estacao'] == estacao]
    
    # Gráfico de linha de vendas mensais
    st.title(f'Vendas Mensais - {estacao}')
    fig, ax = plt.subplots()
    df_filtered.groupby('Mes').sum()['Total_Venda'].plot(kind='line', ax=ax)
    ax.set_ylabel('Total de Vendas')
    st.pyplot(fig)
    
    # Gráfico de barras de vendas por categoria
    st.title('Vendas por Categoria')
    fig, ax = plt.subplots()
    df_filtered.groupby('Categoria').sum()['Total_Venda'].plot(kind='bar', ax=ax)
    ax.set_ylabel('Total de Vendas')
    st.pyplot(fig)
    
    # Gráfico de pizza de vendas por estação
    st.title('Proporção de Vendas por Estação')
    fig, ax = plt.subplots()
    df.groupby('Estacao').sum()['Total_Venda'].plot(kind='pie', ax=ax, autopct='%1.1f%%')
    ax.set_ylabel('')
    st.pyplot(fig)
    
    # Boxplot de preços por categoria
    st.title('Distribuição de Preços por Categoria')
    fig, ax = plt.subplots()
    sns.boxplot(x='Categoria', y='Preço_Venda', data=df_filtered, ax=ax)
    ax.set_ylabel('Preço de Venda')
    st.pyplot(fig)
    
    # Mapa de calor de vendas
    st.title('Mapa de Calor de Vendas')
    df_pivot = df.pivot_table(index='Mes', columns='Produto', values='Total_Venda', aggfunc='sum')
    fig, ax = plt.subplots()
    sns.heatmap(df_pivot, ax=ax)
    st.pyplot(fig)

   
# Página de Visão Geral
if page == "Visão Geral":
    show_overview()


elif page == "Filtros e Dados":
    show_filters_data()
    
# Página de Filtros de acidentes
#elif page == "Gráficos de Acidentes e Casualidades ao Longo do Tempo":
    #show_graphs()

#elif page == "Número de Acidentes por Hora do Dia":
    #show_accidents_by_hour()
