from io import BytesIO
from time import sleep
from datetime import datetime

from PIL import Image
import streamlit as st
import pytesseract as ocr

from views.config_page import set_page_config
from views.content_hide import content_hide_streamlit


set_page_config()
st.markdown(content_hide_streamlit, unsafe_allow_html=True) 

st.markdown(
    """
    # Converta suas imagens em texto com Python e Tesseract!
    """
)

def convert_image_to_text(input_imagem) -> str:       
        return ocr.image_to_string(Image.open(input_imagem), lang="por")

st.markdown(
    """
    ### Faça o upload de uma imagem :arrow_up:
    """
)

input_imagem = st.file_uploader(
    "Texto em formato de imagem",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=False,
    label_visibility = "hidden",
    key="upload_button"
)

if input_imagem is not None:
    bytes_image = BytesIO(input_imagem.getvalue())
    txt_file = convert_image_to_text(bytes_image)

    st.success(f"Upload feito com sucesso!")

    sleep(5)

    st.markdown("""### Imagem convertida com sucesso!!! :sunglasses:""")
    st.download_button(
        label="Baixe o arquivo clicando aqui.",
        data=txt_file,
        file_name=f"imagem_convertida_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt",
        key="download_button"
    )
