import streamlit as st

st.set_page_config(
    page_title="Reach Me",
    page_icon=" ",
    layout="wide"
)

st.title("Contact Page")
st.write("If you would like to communicate or leave a message, you may use the form below.")

st.divider()

st.header("My Contact Details")

st.write("""
📧 **Email Address:** mansayonrechelle@gmail.com  
🎓 **Status:** Computer Science Student  
📍 **Location:** Buri, Mandaon, Masbate
""")

st.divider()

st.header("Message Form")

with st.form("message_form"):

    fullname = st.text_input("Full Name")
    user_email = st.text_input("Your Email")
    user_message = st.text_area("Write your message here")

    send_btn = st.form_submit_button("Submit Message")

    if send_btn:
        if fullname and user_email and user_message:
            st.success(f"Hello {fullname}, your message was successfully submitted!")
        else:
            st.error("Please complete all fields before submitting.")

st.divider()

st.caption("Thank you for visiting my portfolio page.")
