import streamlit as st
from PIL import Image

st.title("Model Performance")
metrics_name = st.selectbox(
    "Select a performance metric to view:",
    ("ROC-AUC Curve", "Confusion Matrix")
)
image_paths = {
    "ROC-AUC Curve": "images/ROC-AUC.png",
    "Confusion Matrix": "images/ConfusionMatrix.png"
}
if metrics_name in image_paths:
        image = Image.open(image_paths[metrics_name])
        st.image(image,caption=f"{metrics_name}")