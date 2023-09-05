
import streamlit as st

from views.config_page import set_page_config
from views.content_hide import content_hide_streamlit


if __name__ == "__main__":

    set_page_config()
    st.markdown(content_hide_streamlit, unsafe_allow_html=True) 

    st.markdown(
        """
        # Converta suas imagens em texto com Python e Tesseract!
        """
    )

