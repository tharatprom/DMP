import streamlit as st
from PIL import Image, ImageDraw
import requests
from io import BytesIO

# ฟังก์ชันโหลดภาพจาก URL
def load_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

# ฟังก์ชันวาดแกน X และ Y บนภาพ
def draw_axes(image):
    img = image.copy()
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # วาดเส้นแกน
    draw.line([(0, height//2), (width, height//2)], fill="red", width=2)  # แกน X
    draw.line([(width//2, 0), (width//2, height)], fill="green", width=2)  # แกน Y
    return img

# URLs ของรูปภาพ
image_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/b/bf/Bulldog_inglese.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Bulldog_adult_male.jpg/640px-Bulldog_adult_male.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/English_Bulldog_600.jpg/640px-English_Bulldog_600.jpg"
]

# Session state สำหรับเก็บภาพที่เลือก
if "selected_image" not in st.session_state:
    st.session_state.selected_image = None

st.title("📷 แกลเลอรีรูปภาพ (พร้อม Resize และแกน X/Y)")

# สร้างแถวภาพ 3 คอลัมน์
cols = st.columns(3)
for i in range(3):
    with cols[i]:
        img = load_image(image_urls[i])
        st.image(img, use_column_width=True, caption=f"ภาพที่ {i+1}")
        if st.button(f"ดูภาพ {i+1}"):
            st.session_state.selected_image = i

# ถ้ามีภาพที่ถูกเลือก
if st.session_state.selected_image is not None:
    st.subheader("🔍 แสดงภาพขนาดใหญ่")

    # Slider สำหรับปรับขนาด
    scale = st.slider("ปรับขนาด (%)", min_value=10, max_value=200, value=100, step=10)

    # โหลดและปรับขนาดภาพ
    img = load_image(image_urls[st.session_state.selected_image])
    new_size = (int(img.width * scale / 100), int(img.height * scale / 100))
    img_resized = img.resize(new_size)

    # วาดแกน X และ Y
    img_with_axes = draw_axes(img_resized)

    st.image(img_with_axes, caption=f"ภาพที่ {st.session_state.selected_image + 1} ({scale}%)", use_column_width=True)
