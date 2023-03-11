import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt

# def translation(picture):
#     width = picture.shape[0]
#     height = picture.shape[1]

#     m_translation_ = np.float32([[1,0,100],[0,1,50],[0,0,1]])
#     translated_img_ = cv2.warpPerspective(picture, m_translation_, (width,height))

#     plt.axis('off')
#     st.image(translated_img_)
#     plt.show()

# def rotation(picture):
#     height, width = picture.shape[:2]
#     m_rotation_ = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)

#     rotated_img_ = cv2.warpAffine(picture, m_rotation_, (width,height))
#     plt.axis('off')
#     st.image(rotated_img_) 
#     plt.show()

# def scaling(picture):
#     height, width = picture.shape[:2]
#     resized_img_ = cv2.resize(picture, (0,0), fx=0.45, fy=0.7, interpolation=cv2.INTER_AREA)
#     resized_img_.shape

#     plt.axis('off')
#     st.image(resized_img_)
#     plt.show()

# def reflection(picture):
#     img_flipped_ = cv2.flip(picture, -1)

#     plt.axis('off')
#     st.image(img_flipped_)
#     plt.show()

# def shearing(picture):
#     m_shearing_x = np.float32([[1, 0.5, 0],
#                                [0, 1, 0],
#                                [0, 0, 1]])

#     sheared_image_x = cv2.warpPerspective(picture, m_shearing_x, (int(picture.shape[1]*1.5), int(picture.shape[0]*1.5)))

#     plt.axis('off')
#     st.image(sheared_image_x)
#     plt.show()


uploaded_file = st.file_uploader("Please upload file", type=["jpg", "png"])

if uploaded_file is not None:
    # Convert the file to an opencv image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    
    # Display the image
    st.image(opencv_image, channels="BGR")
    
    # Translate image
    width = picture.shape[0]
    height = picture.shape[1]
    
    m_translation_ = np.float32([[1,0,100],[0,1,50],[0,0,1]])
    translated_img_ = cv2.warpPerspective(opencv_image, m_translation_, (width,height))

    plt.axis('off')
    st.image(translated_img_, channels="BGR")
    
# def main():
# #     picture = ["pic1.jpg", "pic2.png", "pic3.jpg "]

#     for p in picture:
# #         img_ = cv2.imread(f"{p}")
# #         img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
#         st.image(img_)
#         translation(img_)
#         rotation(img_)
#         scaling(img_)
#         reflection(img_)
#         shearing(img_)
        
# if __name__=='__main__':
#     value = main()
#     st.write(value)
