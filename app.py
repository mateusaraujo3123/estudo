import streamlit as st

# Configuração da página (deve ser o primeiro comando Streamlit)
st.set_page_config(
    page_title="MERCADINHO Portal Da Vila",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização CSS personalizada para replicar a interface da imagem
st.markdown("""
    <style>
    /* Altera o fundo geral da aplicação para o tom escuro da imagem */
    .stApp {
        background-color: #0b0a14 !important;
    }
    
    /* Remove margens extras do Streamlit para alinhar o topo */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Estilo do cabeçalho roxo principal */
    .header-container {
        background-color: #4a0e7d;
        border-radius: 12px;
        padding: 15px 25px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
    }

    /* Texto do Mercadinho */
    .header-title {
        color: #ffffff;
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 20px;
        font-weight: 700;
        margin: 0;
    }

    /* Botão de status online */
    .status-badge {
        background-color: #143d22;
        color: #5cd67d;
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 14px;
        font-weight: 700;
        padding: 6px 16px;
        border-radius: 20px;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }

    /* Estilo customizado para replicar os botões roxos inferiores */
    div.stButton > button {
        background-color: #3b1175 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 18px 20px !important;
        font-size: 14px !important;
        font-weight: bold !important;
        width: 100% !important;
        transition: background-color 0.2s ease;
    }

    /* Efeito de hover ao passar o mouse nos botões */
    div.stButton > button:hover {
        background-color: #4c1696 !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- COMPONENTE DO CABEÇALHO (HEADER) ---
st.markdown("""
    <div class="header-container">
        <div class="header-title">🛍️ MERCADINHO Portal Da Vila</div>
        <div class="status-badge">🟢 online</div>
    </div>
""", unsafe_allow_html=True)

# --- ÁREA DOS BOTÕES INFERIORES ---
# Divide a tela em 3 colunas iguais
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("👥 FIADOS", key="btn_fiados"):
        st.toast("Abrindo painel de Fiados...")

with col2:
    if st.button("📦 PREÇOS", key="btn_precos"):
        st.toast("Abrindo tabela de Preços...")

with col3:
    if st.button("📋 CONTAS A RECEBER", key="btn_contas"):
        st.toast("Abrindo Contas a Receber...")
