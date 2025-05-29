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

# โหลดรูปภาพทั้งหมดจาก URL
def load_image(url):
    response = requests.get(url)
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
        st.image(img, use_column_width=True, caption=f"ภาพที่ {i+1}")

# แสดงภาพขนาดใหญ่เมื่อมีการคลิก
if st.session_state.selected_image is not None:
    st.subheader("ภาพขนาดใหญ่")
    st.image(
        load_image(image_urls[st.session_state.selected_image]),
        caption=f"ภาพที่ {st.session_state.selected_image + 1}",
        use_column_width=True
    )
