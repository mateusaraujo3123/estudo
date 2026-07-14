import streamlit as st

st.set_page_config(
    page_title="MERCADINHO Portal Da Vila",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- COMPONENTE DO CABEÇALHO (HEADER) ---
st.markdown("""
    <div class="header-container">
        <div class="header-title">🛍️ MERCADINHO Portal Da Vila</div>
        <div class="status-badge">🟢 online</div>
    </div>
""", unsafe_allow_html=True)

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
