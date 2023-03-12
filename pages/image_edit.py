import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt

# uploaded_file = st.file_uploader("Upload your image here", type=['jpg', 'png', 'jpeg'])
                                 
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image)
                                 
# translated_img = np.array(image.convert('RGB'))
# gray_scale = cv2.cvtColor(translated_img, cv2.COLOR_RGB2GRAY)
# st.image(grayscale)

# image = cv2.imread("pic1.jpg", cv2.IMREAD_COLOR)
uploaded_file = st.file_uploader("Please upload file", type=["jpg", "png"])

if uploaded_file is not None:
    # Convert the file to an opencv image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    st.image(opencv_image)

def rotation(opencv_image):
    height, width = opencv_image.shape[:2]
    m_rotation_ = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)

    rotated_img_ = cv2.warpAffine(opencv_image, m_rotation_, (width,height))
    plt.axis('off')
    st.image(rotated_img_) 
    st.pyplot()

rotation()
