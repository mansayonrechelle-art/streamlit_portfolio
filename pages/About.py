import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Personal Portfolio",
    page_icon=" ",
    layout="wide"
)


image = Image.open("assets/picture.jpg")

st.title("Personal Portfolio")
st.write("Welcome to my personal page created using Streamlit.")
st.divider()

col1, col2 = st.columns([1,2])

with col1:
    st.image(image, caption="Profile Picture", use_container_width=True)

with col2:
    st.subheader("Rechelle M. Mansayon")

    st.write("""
🎂 **Born on:** December 14, 2004  
📍 **Address:** Buri, Mandaon, Masbate  
🎓 **Course:** Bachelor of Science in Computer Science  
📚 **School:** DEBESMSCAT  
👤 **Age:** 21 years old
""")

st.divider()

st.header("About Myself")

st.write("""
I have big dreams for myself and for my family. I am trying to achieve my goals so I can give them a better life.

However, sometimes my laziness becomes a hindrance and affects my progress. One of my weaknesses is that I tend to overthink, and it sometimes affects my performance in everything I do.

Despite this, I still hope to become successful and achieve what I truly want—not only for myself but also for my family.
""")

st.divider()

st.header("Personal Goal")

if st.button("Show My Goal"):
    st.success("My goal is to become successful and support my family in the future.")

st.divider()


