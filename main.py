import time
import streamlit as st
from getModel import teachable_machine_classification
from PIL import Image

st.title("😄 닮은 동물상 찾기")
st.header("사진을 넣어서 닮은 동물을 찾아보세요!")
st.text("사진을 올려주세요.")

uploaded_file = st.file_uploader("사진 업로드", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='업로드된 얼굴', use_column_width=True)
    st.write("")
    with st.spinner(text = "분석 중..."):
        time.sleep(5)
    label = teachable_machine_classification(image, 'face_matching_model.h5')
    if label == 0:
        st.success("😺 고양이상입니다.")
    elif label == 1:
        st.success("🐶 강아지상입니다.")
    elif label == 2:
        st.success("🐺 늑대상입니다.")
    elif label == 3:
        st.success("🐰 토끼상입니다.")
    elif label == 4:
        st.success("🐻 곰상입니다.")
    else:
        st.success("🦊 여우상입니다.")
    