import streamlit as st

st.set_page_config(
    page_title="FAQs",
    page_icon=" ",
    layout="wide"
)

st.title(" FAQ's Section")
st.write("Select a question and click the button to see the answer.")
st.divider()

question = st.selectbox(
    "Choose a question:",
    [
        "Who are you?",
        "What course are you studying?",
        "Why did you create this portfolio?",
        "What is your goal in life?"
    ]
)


if st.button("Show Answer"):

    if question == "Who are you?":
        st.success("I am Rechelle M. Mansayon, a Computer Science student.")

    elif question == "What course are you studying?":
        st.success("I am currently studying Bachelor of Science in Computer Science.")

    elif question == "Why did you create this portfolio?":
        st.success("I created this portfolio to present my personal information and simple projects.")

    elif question == "What is your goal in life?":
        st.success("My goal is to become successful and give my family a better life.")

st.divider()

st.caption("Thank you for visiting my portfolio page.")
