import streamlit as st

st.set_page_config(
     page_title="Meu Painel",
     page_icon="💜",
     layout="wide"
)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("teste"):
       st.link_button("entra no YouTube", "HTTPS://www.youTube.com", use_container_width=True)

with col2:
    if st.button("FACEBOOK"):
       st.link_button("entra no Facebook", "HTTPS://www.facebook.com", use_container_width=True
                     )
       
with col3:
    if st.button("google"):
       st.link_button("entra no Google", "HTTPS://www.google.com")
