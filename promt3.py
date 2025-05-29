import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# URLs ของรูปภาพ
image_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/b/bf/Bulldog_inglese.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/b/bf/Bulldog_inglese.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/b/bf/Bulldog_inglese.jpg"
]

# โหลดรูปภาพทั้งหมดจาก URL พร้อม headers
def load_image(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))

# กำหนดชื่อปุ่มที่สัมพันธ์กับรูปแต่ละภาพ
if "selected_image" not in st.session_state:
    st.session_state.selected_image = None

st.title("แกลเลอรีรูปภาพ")

# สร้างคอลัมน์สำหรับรูปภาพ
cols = st.columns(3)
for i in range(3):
    with cols[i]:
        img = load_image(image_urls[i])
        if st.button(f"ดูภาพ {i+1}"):
            st.session_state.selected_image = i
        st.image(img, use_container_width =True, caption=f"ภาพที่ {i+1}")

# แสดงภาพขนาดใหญ่พร้อมปรับขนาด
if st.session_state.selected_image is not None:
    st.subheader("ภาพขนาดใหญ่")

    # Slider สำหรับปรับขนาด (เปอร์เซ็นต์)
    scale = st.slider("ปรับขนาด (%)", min_value=10, max_value=200, value=100, step=10)

    # โหลดและ resize ภาพ
    original_img = load_image(image_urls[st.session_state.selected_image])
    new_size = (
        int(original_img.width * scale / 100),
        int(original_img.height * scale / 100)
    )
    resized_img = original_img.resize(new_size)

    # แสดงภาพที่ปรับขนาดแล้ว
    st.image(resized_img, caption=f"ภาพที่ {st.session_state.selected_image + 1} ({scale}%)", use_column_width=False)
