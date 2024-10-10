import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon= "⚽",
    layout = 'wide',
)
df_data = st.session_state["data"]
    
# Cria uma lista única com o nome dos times
clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube",clubes)
    
df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")
    
st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f'## {club}')

# todas as colunas que vão aparecer no df
columns = ['Age', 'Photo', 'Flag', 'Overall', 'Value(£)','Wage(£)', 'Joined', 'Height(cm.)', 
           'Weight(lbs.)', 'Contract Valid Until', 'Release Clause(£)']

# data frame com as colunas escolhidas permitindo seleção de configurações por colunas
st.dataframe(df_filtered [columns],
             column_config={
                 # coluna de progresso no overall, com limite maximo e minimo além da unidade
                 'Overall': st.column_config.ProgressColumn(   
                    "Overall", format= '%d', min_value = 0, max_value=100
                    ),
                 # Faz um filtro usando o valor maximo do maior valor do time
                 'Wage(£)': st.column_config.ProgressColumn("Weekly Wage", format= '£%f', 
                                                            min_value = 0, max_value=df_filtered['Wage(£)'].max()
                 ),
                 # Transforma o caminho da celula na imagem.
                 'Photo': st.column_config.ImageColumn(),
                 'Flag': st.column_config.ImageColumn("Country"),
                 })



