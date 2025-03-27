import streamlit as st
from PIL import Image

st.write("Hello camera")

with st.expander("Open the Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_image = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_image)
