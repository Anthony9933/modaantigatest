import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
df = pd.read_csv('dados.csv')

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
    
    # Mostrar os dados
    st.header('Dados Brutos')
    st.write(df)
    
    # Gráfico de vendas por estação
    st.header('Vendas por Estação')
    fig1 = px.bar(df, x='Estacao', y='PdVenda', title='Total de Vendas por Estação', labels={'PdVenda': 'Total de Vendas', 'Estacao': 'Estação'}, text_auto=True)
    st.plotly_chart(fig1)
    
    # Gráfico de quantidade de itens vendidos por tecido
    st.header('Quantidade de Itens Vendidos por Tecido')
    fig2 = px.bar(df, x='Tecido', y='Quantidade', title='Quantidade de Itens Vendidos por Tecido', labels={'Quantidade': 'Quantidade Vendida', 'Tecido': 'Tecido'}, text_auto=True)
    st.plotly_chart(fig2)
    
    # Gráfico de lucro por tecido (PdVenda - PdCusto)
    st.header('Lucro por Tecido')
    df['Lucro'] = df['PdVenda'] - df['PdCusto']
    fig3 = px.bar(df, x='Tecido', y='Lucro', title='Lucro por Tecido', labels={'Lucro': 'Lucro Total', 'Tecido': 'Tecido'}, text_auto=True)
    st.plotly_chart(fig3)
    
    # Gráfico de evolução das vendas ao longo do tempo
    st.header('Evolução das Vendas ao Longo do Tempo')
    # Converter a coluna 'Data' para datetime
    df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m')
    # Agrupar por ano e mês
    vendas_mensais = df.groupby(df['Data'].dt.to_period('M')).sum().reset_index()
    fig4 = px.line(vendas_mensais, x='Data', y='PdVenda', title='Evolução das Vendas ao Longo do Tempo', labels={'Data': 'Data', 'PdVenda': 'Total de Vendas'})
    st.plotly_chart(fig4)
    
    # Gráfico de relação entre quantidade e preço de custo
    st.header('Relação entre Quantidade e Preço de Custo')
    # Verificar se PdCusto e Quantidade são numéricos
    df = df[pd.to_numeric(df['PdCusto'], errors='coerce').notnull()]
    df = df[pd.to_numeric(df['Quantidade'], errors='coerce').notnull()]
    fig5 = px.scatter(df, x='PdCusto', y='Quantidade', title='Relação entre Quantidade e Preço de Custo', labels={'PdCusto': 'Preço de Custo', 'Quantidade': 'Quantidade'})
    st.plotly_chart(fig5)

# Página de Visão Geral
if page == "Visão Geral":
    show_overview()

# Página de Filtros e Dados
elif page == "Filtros e Dados":
    show_filters_data()
