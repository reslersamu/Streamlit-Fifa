import streamlit as st
import webbrowser #abre nova aba
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Players",
    page_icon= "🏠",
    layout = 'wide'
)

if "data" not in st.session_state:
    df_data = pd.read_csv (r'C:\Users\Usuario\OneDrive - Governo do Estado do Rio Grande do Sul\Documents\Python\Cursos\Aulas\Projetos\Projeto Dash FIFA\CLEAN_FIFA23_official_data.csv', index_col=0)
    # filtro para contrato valido até a data atual
    df_data = df_data[df_data["Contract Valid Until"]>= datetime.today().year]
    # filtro para valores registrados
    df_data = df_data[df_data["Value(£)"]>0]
    # ordenar por overall
    df_data = df_data.sort_values(by="Overall", ascending=False)
    # salva como df_data para buscar nas outras abas
    st.session_state['data'] = df_data
    

#Texto de intodrução ao "app"
st.markdown("# FIFA23 OFFICIAL DATASET! ⚽")

# Permite a adição de um hiperlink
st.sidebar.markdown("Desenvolvido por [Asimov Acadey](https:\\asimov.academy)")

# Adição de um botão
btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)