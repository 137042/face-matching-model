import time
import streamlit as st
from getModel import teachable_machine_classification
from PIL import Image

st.title("đ ëŽė ëëŦŧė ė°žę¸°")
st.header("ėŦė§ė ëŖė´ė ëŽė ëëŦŧė ė°žėëŗ´ė¸ė!")
st.text("ėŦė§ė ėŦë ¤ėŖŧė¸ė.")

uploaded_file = st.file_uploader("ėŦė§ ėëĄë", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='ėëĄëë ėŧęĩ´', use_column_width=True)
    st.write("")
    with st.spinner(text = "ëļė ė¤..."):
        time.sleep(5)
    label = teachable_machine_classification(image, 'face_matching_model.h5')
    if label == 0:
        st.success("đē ęŗ ėė´ėėëë¤.")
    elif label == 1:
        st.success("đļ ę°ėė§ėėëë¤.")
    elif label == 2:
        st.success("đē ëëėėëë¤.")
    elif label == 3:
        st.success("đ° í ëŧėėëë¤.")
    elif label == 4:
        st.success("đģ ęŗ°ėėëë¤.")
    else:
        st.success("đĻ ėŦė°ėėëë¤.")
    