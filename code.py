import streamlit as st
import pandas as pd
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
    #st.header("Filtros e Dados")
    
    # Carregar dados
    df = pd.read_csv('dados.csv')
    
    # Configurar o layout da página
    st.set_page_config(layout="wide")
    
    # Título da aplicação
    st.title('Análise de Dados da Loja de Roupas Femininas')
    
    # Mostrar os dados
    st.header('Dados Brutos')
    st.write(df)
    
    # Gráfico de vendas por estação
    st.header('Vendas por Estação')
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Estacao', y='PdVenda', data=df, estimator=sum, ax=ax1)
    ax1.set_title('Total de Vendas por Estação')
    ax1.set_xlabel('Estação')
    ax1.set_ylabel('Total de Vendas')
    st.pyplot(fig1)
    
    # Gráfico de quantidade de itens vendidos por tecido
    st.header('Quantidade de Itens Vendidos por Tecido')
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Tecido', y='Quantidade', data=df, estimator=sum, ax=ax2)
    ax2.set_title('Quantidade de Itens Vendidos por Tecido')
    ax2.set_xlabel('Tecido')
    ax2.set_ylabel('Quantidade Vendida')
    st.pyplot(fig2)
    
    # Gráfico de lucro por tecido (PdVenda - PdCusto)
    st.header('Lucro por Tecido')
    df['Lucro'] = df['PdVenda'] - df['PdCusto']
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Tecido', y='Lucro', data=df, estimator=sum, ax=ax3)
    ax3.set_title('Lucro por Tecido')
    ax3.set_xlabel('Tecido')
    ax3.set_ylabel('Lucro Total')
    st.pyplot(fig3)
    
    # Gráfico de evolução das vendas ao longo do tempo
    st.header('Evolução das Vendas ao Longo do Tempo')
    df['Data'] = pd.to_datetime(df['Data'])
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    df.groupby(df['Data'].dt.to_period('M')).sum()['PdVenda'].plot(ax=ax4)
    ax4.set_title('Evolução das Vendas ao Longo do Tempo')
    ax4.set_xlabel('Data')
    ax4.set_ylabel('Total de Vendas')
    st.pyplot(fig4)
    
    # Gráfico de relação entre quantidade e preço de custo
    st.header('Relação entre Quantidade e Preço de Custo')
    fig5, ax5 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='PdCusto', y='Quantidade', data=df, ax=ax5)
    ax5.set_title('Relação entre Quantidade e Preço de Custo')
    ax5.set_xlabel('Preço de Custo')
    ax5.set_ylabel('Quantidade')
    st.pyplot(fig5)

   
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
