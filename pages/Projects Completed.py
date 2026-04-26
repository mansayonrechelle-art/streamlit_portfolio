import streamlit as st

st.set_page_config(
    page_title="My Portfolio Projects",
    page_icon=" ",
    layout="wide"
)


st.title(" Project Completed")
st.write("Below are some simple applications and projects I created while studying.")
st.divider()


st.subheader("My Sample Projects")

project1, project2, project3 = st.columns(3)

with project1:
    st.info("Teacher's Day Message Card")
    st.caption("A simple web application where students can write and share appreciation messages for their teachers.")

with project2:
    st.info("Simple Calculator")
    st.caption("A basic calculator that can perform addition, subtraction, multiplication, and division.")

with project3:
    st.info("Personal Portfolio")
    st.caption("A small website used to present personal information, skills, and projects.")

st.divider()

st.subheader("Project Summary")

st.write("Total Projects Created: **3**")
st.write("Main Programming Language: **HTML**")
st.write("Development Tool: **Streamlit Framework**")


st.divider()

st.caption("Thank you for visiting my portfolio page.")
