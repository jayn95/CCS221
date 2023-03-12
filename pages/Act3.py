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
        st.title("Translated Image")
        st.image(translated_img_)
#         st.pyplot()
        
    translate = translation(opencv_image)
    st.write(translate)

    def rotation(opencv_image):
        height, width = opencv_image.shape[:2]
        m_rotation_ = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
        
        rotated_img_ = cv2.warpAffine(opencv_image, m_rotation_, (width,height))
        plt.axis('off')
        st.image(rotated_img_)
#         st.pyplot()

    rotate = rotation(opencv_image)
    st.write(rotate)
    
    def scaling(opencv_image):
        height, width = opencv_image.shape[:2]
        resized_img_ = cv2.resize(opencv_image, (0,0), fx=0.45, fy=0.7, interpolation=cv2.INTER_AREA)
        resized_img_.shape
        
        plt.axis('off')
        st.image(resized_img_)
#         plt.show()

    scale = scaling(opencv_image)
    st.write(scale)

    def reflection(opencv_image):
        img_flipped_ = cv2.flip(opencv_image, -1)
        
        plt.axis('off')
        st.image(img_flipped_)
#         plt.show()

    reflect = reflection(opencv_image)
    st.write(reflect)

    def shearing(opencv_image):
        m_shearing_x = np.float32([[1, 0.5, 0],
                               [0, 1, 0],
                               [0, 0, 1]])
        
        sheared_image_x = cv2.warpPerspective(opencv_image, m_shearing_x, (int(opencv_image.shape[1]*1.5), int(opencv_image.shape[0]*1.5)))
        
        plt.axis('off')
        st.image(sheared_image_x)
#         plt.show()

    shear = shearing(opencv_image)
    st.write(shear)
