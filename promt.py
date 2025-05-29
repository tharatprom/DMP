import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# ชื่อหน้า
st.title("แสดงภาพจาก URL")

# URL ของภาพ
image_url = "https://upload.wikimedia.org/wikipedia/commons/b/bf/Bulldog_inglese.jpg"

# โหลดภาพจาก URL
try:
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # แสดงภาพ
    st.image(image, caption="Bulldog Inglese", use_column_width=True)

except Exception as e:
    st.error(f"เกิดข้อผิดพลาดในการโหลดภาพ: {e}")
