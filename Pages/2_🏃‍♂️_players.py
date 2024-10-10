import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon= "🏃‍♂️",
    layout = 'wide'
)

df_data = st.session_state['data']

# Cria uma lista singular com todos os clubes
clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube",clubes)

# A partir da lista dos clubes, um lista singular com os jogadores
df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador",players)

# Tela individual de cada jogador

# Busca a primeira aparição do nome do jogador
player_stats = df_data[df_data["Name"]== player].iloc[0]

# Randeriza imagens, inclusive de site
st.image(player_stats["Photo"])

st.title(player_stats["Name"])

# Markdown simples e negrito
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

# Criação de 4 coluna em uma linha (1 delas ficará vazia)
col1, col2, col3, col4 = st.columns (4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)']/100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")

# Linha divisória
st.divider()

# Subtítulo
st.subheader(f"Overall {player_stats['Overall']}")
# Barra de progresso
st.progress(int(player_stats["Overall"]))

col1, col2, col3, col4 = st.columns (4)

col1.metric(label = "Valor de mercado", value=f'£ {player_stats['Value(£)']:,}')
col2.metric(label = "Remuneração semanal", value=f'£ {player_stats['Wage(£)']:,}')
col3.metric(label = "Cláusula de rescisão", value=f'£ {player_stats['Release Clause(£)']:,}')