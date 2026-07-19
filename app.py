import streamlit as st

# ==============================================================================
# 1. DECLARAÇÃO EXPLÍCITA DAS PÁGINAS (Resolve o KeyError)
# ==============================================================================
pagina_principal = st.Page("app.py", title="Home", icon="🏠")
pagina_ias = st.Page("pages/ias.py", title="IA's", icon="👥")

# Inicializa o gerenciador de rotas ocultando a barra lateral padrão se preferir
pg = st.navigation([pagina_principal, pagina_ias], position="hidden")
pg.run()

# ==============================================================================
# 2. CONFIGURAÇÃO DA PÁGINA E ESTILOS
# ==============================================================================
st.set_page_config(
    page_title="Coisas úteis",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Carrega o seu arquivo CSS externo
with open("style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# Título da página
st.markdown('<h1 class="titulo">Coisas úteis</h1>', unsafe_allow_html=True)

# ==============================================================================
# 3. BOTÃO DE NAVEGAÇÃO CENTRALIZADO
# ==============================================================================
# Passamos o OBJETO pagina_ias diretamente para que o Streamlit não erre o caminho
st.page_link(pagina_ias, label="👥 IA's")

# ==============================================================================
# 4. LINKS EXTERNOS (CONTEÚDO ANTERIOR)
# ==============================================================================
st.markdown("""
   <div class="button-container">
    <a href="https://chatgpt.com/" class="botoes" target="_blank">chatgpt</a>
    <a href="https://GOOGLE.COM" class="botoes" target="_blank">GOOGLE AI</a>
    <a href="https://lovable.dev/" class="botoes" target="_blank">LOVABLE</a>
   </div>
""", unsafe_allow_html=True)
