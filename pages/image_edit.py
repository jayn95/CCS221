import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt

uploaded_file = st.file_uploader("Please upload file", type=["jpg", "png"])

if uploaded_file is not None:
    # Convert the file to an opencv image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    st.image(opencv_image)
    
    def translation(opencv_image):
        height, width = opencv_image.shape[:2]
        width = opencv_image.shape[0]
        height = opencv_image.shape[1]
        
        m_translation_ = np.float32([[1,0,100],[0,1,50],[0,0,1]])
        translated_img_ = cv2.warpPerspective(opencv_image, m_translation_, (width,height))
        
        plt.axis('off')
        st.image(translated_img_)
        st.pyplot()
        
    translate = translation(opencv_image)
    st.write(translate)

    def rotation(opencv_image):
        height, width = opencv_image.shape[:2]
        m_rotation_ = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
        
        rotated_img_ = cv2.warpAffine(opencv_image, m_rotation_, (width,height))
        plt.axis('off')
        st.image(rotated_img_)
        st.pyplot()

    rotate = rotation(opencv_image)
    st.write(rotate)
    

