import streamlit as st

# ==============================================================================
# 1. DECLARAÇÃO DAS PÁGINAS DO APLICATIVO
# ==============================================================================
# Criamos uma função separada para a Home para evitar o loop de RecursionError
def mostrar_home():
    # Título da página principal
    st.markdown('<h1 class="titulo">Coisas úteis</h1>', unsafe_allow_html=True)

    # Botão de Navegação Local para a página de IAs
    # (Ele vai usar as configurações visuais do seu style.css automaticamente)
    st.page_link(pagina_ias, label="👥 IA's")

    # Links Externos
    st.markdown("""
       <div class="button-container">
        <a href="https://chatgpt.com/" class="botoes" target="_blank">chatgpt</a>
        <a href="https://GOOGLE.COM" class="botoes" target="_blank">GOOGLE AI</a>
        <a href="https://lovable.dev/" class="botoes" target="_blank">LOVABLE</a>
       </div>
    """, unsafe_allow_html=True)

# Mapeia as páginas do projeto
pagina_principal = st.Page(mostrar_home, title="Home", icon="🏠")
pagina_ias = st.Page("pages/ias.py", title="IA's", icon="👥")

# ==============================================================================
# 2. INICIALIZAÇÃO DO ROTEADOR E CONFIGURAÇÕES
# ==============================================================================
# Configura o menu ocultando a barra lateral nativa padrão
pg = st.navigation([pagina_principal, pagina_ias], position="hidden")

st.set_page_config(
    page_title="Coisas úteis",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Injeta as regras de estilo do seu arquivo CSS externo
with open("style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# Executa a renderização da página ativa sem gerar loops infinitos
pg.run()
