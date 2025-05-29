import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# ฟังก์ชันโหลดภาพจาก URL แบบปลอดภัย
def load_image(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        st.error(f"ไม่สามารถโหลดภาพจาก URL นี้ได้: {url}")
        st.stop()

    return Image.open(BytesIO(response.content)).convert("RGBA")

# URLs ของภาพที่โหลดได้แน่นอน
image_url1 = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Golde33443.jpg/640px-Golde33443.jpg"
image_url2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Golden_Retriever_Carlos_%2810518190846%29.jpg/640px-Golden_Retriever_Carlos_%2810518190846%29.jpg"

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

# ปรับขนาดให้เท่ากัน
if img1.size != img2.size:
    img2 = img2.resize(img1.size)

# ปรับระดับการผสม
st.subheader("ภาพที่ผสม")
alpha = st.slider("ระดับการผสม (0.0 = ภาพ 1, 1.0 = ภาพ 2)", 0.0, 1.0, 0.5, 0.01)

# ผสมภาพ
blended_img = Image.blend(img1, img2, alpha)
st.image(blended_img, caption=f"ภาพที่ผสม (alpha = {alpha})", use_column_width=True)
