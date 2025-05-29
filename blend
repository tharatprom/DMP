import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# ฟังก์ชันโหลดภาพจาก URL
def load_image(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return Image.open(BytesIO(response.content)).convert("RGBA")

# URLs ของภาพ (คุณสามารถเปลี่ยน URL ได้ตามต้องการ)
image_url1 = "https://upload.wikimedia.org/wikipedia/commons/9/99/English_bulldog.jpg"
image_url2 = "https://upload.wikimedia.org/wikipedia/commons/5/56/Bulldog_adult_male.jpg"

st.title("🔀 ผสมภาพ 2 รูป (Blending)")

# โหลดภาพทั้งสอง
img1 = load_image(image_url1)
img2 = load_image(image_url2)

# แสดงภาพต้นฉบับ
st.subheader("ภาพต้นฉบับ")
col1, col2 = st.columns(2)
with col1:
    st.image(img1, caption="ภาพ 1", use_column_width=True)
with col2:
    st.image(img2, caption="ภาพ 2", use_column_width=True)

# ปรับขนาดให้เท่ากัน (ใช้ขนาดภาพแรกเป็นเกณฑ์)
if img1.size != img2.size:
    img2 = img2.resize(img1.size)

# Slider สำหรับปรับความเข้มของการผสม (alpha)
st.subheader("ภาพที่ผสม")
alpha = st.slider("ระดับการผสม (0.0 = ภาพ 1, 1.0 = ภาพ 2)", 0.0, 1.0, 0.5, 0.01)

# ผสมภาพ
blended_img = Image.blend(img1, img2, alpha)

# แสดงภาพที่ผสมแล้ว
st.image(blended_img, caption=f"ภาพที่ผสม (alpha = {alpha})", use_column_width=True)
