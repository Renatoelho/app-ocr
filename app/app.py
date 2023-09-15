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

process_image = None

if "upload_image" not in st.session_state:
      st.session_state["upload_image"] = "no"
      st.session_state["process_image"] = "no"

def change_upload_image():
    st.session_state["upload_image"] = "yes"

def click_process_image():
    st.session_state["process_image"] = "yes"

def click_restart_process():
    st.session_state["upload_image"] = "no"
    st.session_state["process_image"] = "no"
    sleep(2)

def convert_image_to_text(input_imagem) -> str:       
    return ocr.image_to_string(Image.open(input_imagem), lang="por")

st.markdown(
    """
    # Converta suas imagens em texto com Python e Tesseract!

    ### Faça o upload de uma imagem :arrow_up:

    """
)

input_imagem = st.file_uploader(
    "Texto em formato de imagem",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=False,
    label_visibility = "hidden",
    on_change=change_upload_image,
    key="upload_button"
)   

if input_imagem is not None and st.session_state["upload_image"] == "yes":
    bytes_image = BytesIO(input_imagem.getvalue())
    txt_file = convert_image_to_text(bytes_image)

    if st.session_state["process_image"] == "no":
        progress_text = "Fazendo upload da imagem. Aguarde..."
        progress_bar = st.progress(0)
        
        for perc_completed in range(100):
            sleep(0.05)
            progress_bar.progress(perc_completed+1, text=progress_text)

        st.success(f"Upload feito com sucesso!")

    process_image = st.button("Converter Imagem", on_click=click_process_image)

if process_image is not None and st.session_state["process_image"] == "yes":
    progress_text = "Convertendo imagem em texto. Aguarde..."
    progress_bar = st.progress(0)
    
    for perc_completed in range(100):
        sleep(0.05)
        progress_bar.progress(perc_completed+1, progress_text)

    st.markdown("""### Imagem convertida com sucesso!!! :sunglasses:""")

    st.download_button(
        label="Baixe o arquivo clicando aqui.",
        data=txt_file,
        file_name=f"imagem_convertida_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt",
        on_click=click_restart_process,
        key="download_button"
    )
