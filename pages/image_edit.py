import streamlit as st
import numpy as np
import cv2

uploaded_file = st.file_uploader("Upload your image here", type=['jpg', 'png', 'jpeg']
                                 
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image)
                                 
translated_img = np.array(image.convert('RGB'))
gray_scale = cv2.cvtColor(translated_img, cv2.COLOR_RGB2GRAY)
st.image(grayscale)