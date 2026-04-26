import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Rechelle Mansayon Portfolio",
    page_icon=" ",
    layout="wide"
)


image = Image.open("assets/picture.jpg")


st.title("Multipage Streamlit Web Application")
st.write("A simple personal portfolio created with Streamlit.")
st.divider()


col1, col2 = st.columns([1,2])

with col1:
    st.image(image, caption="Profile Photo", use_container_width=True)

with col2:
    st.header("Rechelle M. Mansayon")
    st.write("""
Hi! I am **Rechelle M. Mansayon**, a Computer Science student who is currently studying and improving my knowledge in technology.

I enjoy exploring simple programming projects and learning how systems and websites are created.
""")

    st.write("🎓 **School:** DEBESMSCAT")
    st.write("📘 **Year Level:** 3rd Year College")
    st.write("💡 **Interest:** Learning new technologies")

st.divider()


st.header("Skills Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Python", value="Basic")

with col2:
    st.metric(label="HTML", value="Basic")

with col3:
    st.metric(label="CSS", value="Basic")

st.divider()


st.header("Sample Projects")

project1, project2, project3 = st.columns(3)

with project1:
    st.info("🌼 Teacher's Day Message Card")
    st.caption("A simple web application where students can write and share appreciation messages for their teachers.")


with project2:
    st.info("🧮 **Simple Calculator**")
    st.caption("Performs basic math operations.")

with project3:
    st.info("🌐 **Personal Portfolio**")
    st.caption("A website that shows my projects and skills.")

st.divider()

# ---------------- INTERACTION ----------------
st.header("Personal Motivation")

if st.button("Show Message"):
    st.success("Life isn’t about finding yourself. Life is about creating yourself")

st.divider()



