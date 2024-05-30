import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da barra lateral
page = st.sidebar.selectbox("Escolha a Página", ["Visão Geral", "Filtros e Dados"])

# Função para carregar os dados
@st.cache
def load_data():
    # Substitua 'sua_base_de_dados_ajustada.csv' pelo caminho para o seu arquivo de dados
    #df = pd.read_csv('sua_base_de_dados_ajustada.csv')
    df = pd.read_csv('adjusted_data.csv')
    df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d')
    return df

# Função para mostrar a visão geral
def show_overview():
    st.header("Visão Geral do Projeto")
    st.write("""
        Bem-vindo ao projeto de Visualização de dados da loja Moda Antiga! Este projeto gira em torno da análise e apresentação 
        de dados do estoque e de vendas de produtos da loja Moda Antiga. O conjunto de dados contém várias colunas fornecendo insights 
        sobre os produtos e informações relativas a vendas, incluindo data, produtos mais vendidos, melhores e piores meses de venda.
    """)

    st.header("Como Funciona")
    st.write("""
        O projeto utiliza um conjunto de dados com informações sobre as vendas e o estoque da loja. Aqui está uma breve visão 
        geral dos principais componentes:
    """)

    st.header("Objetivo do Projeto")
    st.write("""
        O principal objetivo deste projeto é obter insights pela análise dos dados e gráficos criados. Isso inclui entender 
        o que os dados estão nos dizendo, identificar e explorar padrões dos compradores 
        prevendo e criando estratégias para aumentar as vendas.
    """)

    st.header("Como Utilizar")
    st.write("""
        Para explorar o projeto, você pode navegar por diferentes seções usando a barra lateral. As principais seções incluem:
    """)

    st.header("Conclusão")
    st.write("""
        Sinta-se à vontade para analisar o conjunto de dados, obter insights e tirar conclusões significativas a partir 
        dos dados apresentados. Para análises específicas ou dúvidas, novos recursos podem ser incorporados com base nos 
        objetivos do seu projeto.
    """)

    st.write("Aproveite a exploração do projeto!")

# Função para mostrar filtros e dados
def show_filters_data():
    # Carregar os dados
    df = load_data()

    # Processar os dados para obter vendas anuais e mensais
    df['Ano'] = df['Data'].dt.year
    df['Mes'] = df['Data'].dt.month
    df['VendaTotal'] = df['Quantidade'] * df['PdVenda']

    # Agrupar por ano e mês e somar as vendas
    vendas_mensais = df.groupby(['Ano', 'Mes'])['VendaTotal'].sum().reset_index()

    # Criar uma coluna de data fictícia para plotar
    vendas_mensais['AnoMes'] = vendas_mensais.apply(lambda row: f"{row['Ano']}-{row['Mes']:02d}-01", axis=1)
    vendas_mensais['AnoMes'] = pd.to_datetime(vendas_mensais['AnoMes'])

    # Configurar o título da aplicação
    st.title('Evolução das Vendas ao Longo dos Anos e Meses')

    # Criar o gráfico de evolução das vendas
    fig = px.line(vendas_mensais, x='AnoMes', y='VendaTotal', title='Evolução das Vendas Mensais', labels={'AnoMes': 'Ano e Mês', 'VendaTotal': 'Vendas Totais'})

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig)

# Multiselect para escolher tecidos
    tecidos = ['Flanela', 'Tactel', 'Cetim', 'Jeans', 'Seda', 'Algodão', 'Viscose', 'Poliéster', 'Sarja', 'Tricô', 'Lã', 'Couro', 'Moletom', 'Malha', 'Chiffon', 'Linho']
    selected_tecidos = st.multiselect("Selecione os Tecidos", tecidos, default=tecidos)

    # Multiselect para escolher estações
    estacoes = ['Verão', 'Outono', 'Inverno', 'Primavera']
    selected_estacoes = st.multiselect("Selecione as Estações", estacoes, default=estacoes)

    # Filtrar os dados com base na seleção
    df_filtered_tecido = df[df['Tecido'].isin(selected_tecidos)]
    df_filtered_estacao = df[df['Estacao'].isin(selected_estacoes)]

    # Agrupar por ano, mês e tecido
    vendas_por_tecido = df_filtered_tecido.groupby(['Ano', 'Mes', 'Tecido'])['VendaTotal'].sum().reset_index()

    # Agrupar por ano e estação
    vendas_por_estacao = df_filtered_estacao.groupby(['Ano', 'Estacao'])['VendaTotal'].sum().reset_index()

    # Criar colunas de data fictícia para plotar
    vendas_por_tecido['AnoMes'] = vendas_por_tecido.apply(lambda row: f"{row['Ano']}-{row['Mes']:02d}-01", axis=1)
    vendas_por_tecido['AnoMes'] = pd.to_datetime(vendas_por_tecido['AnoMes'])

    # Gráfico de evolução das vendas por tecido
    fig_tecido = px.line(vendas_por_tecido, x='AnoMes', y='VendaTotal', color='Tecido', title='Evolução das Vendas por Tecido',
                         labels={'AnoMes': 'Ano e Mês', 'VendaTotal': 'Vendas Totais', 'Tecido': 'Tecido'})

    # Gráfico de vendas por estação
    fig_estacao = px.line(vendas_por_estacao, x='Ano', y='VendaTotal', color='Estacao', title='Evolução das Vendas por Estação',
                          labels={'Ano': 'Ano', 'VendaTotal': 'Vendas Totais', 'Estacao': 'Estação'})

    # Mostrar os gráficos no Streamlit
    st.plotly_chart(fig_tecido)
    st.plotly_chart(fig_estacao)

# Página de Visão Geral
if page == "Visão Geral":
    show_overview()
# Página de Filtros e Dados
elif page == "Filtros e Dados":
    show_filters_data()
