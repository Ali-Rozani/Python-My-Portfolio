import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    layout="wide"
)

col_photo, col_text = st.columns([1, 2])

with col_photo:
    try:
        st.image("Ali Haider.jpg", width=300)
    except:
        st.error("Add 'Ali Haider.jpg' to your project directory")

with col_text:
    st.title("Welcome to My Portfolio")
    st.subheader("About Me")
    st.write("Hi! I'm Ali Haider. I'm a Programmer & AI Master.")


col1, col2 = st.columns(2)

with col1:
    st.header("Skills")
    st.write("- Python Programming")
    st.write("- Web Development")
    st.write("- MongoDB")
    st.write("- And Many More!!!")
    
    # Simple progress bars for skills
    st.write("Python")
    st.progress(0.9)
    st.write("Web Development")
    st.progress(0.8)
    st.write("MongoDB")
    st.progress(0.85)
    st.write("AI Skills")
    st.progress(1.0)

with col2:
    st.header("Experience")

    with st.expander("Current Role"):
        st.write("2023 - Present")
        st.write("• Developed key features")
        st.write("• Led multiple projects")
        st.write("• Built multiple applications")
    
    with st.expander("Previous Role"):
        st.write("2022 - 2023")
        st.write("• Learned new technologies")
        st.write("• Developed new features")
        st.write("• Learned about databases")
        st.write("• Learned about AI")

# Projects section
st.header("Projects")
project1, project2 = st.columns(2)

with project1:
    st.subheader("Project 1")
    st.write("I made my first CrewAI Flow project in python, which deliver's the best results and responses for the user.")
    if st.button("Learn More", key="btn1"):
        st.write("https://github.com/Ali-Rozani/Python-CrewAI/tree/main/Ultimate%20CrewAI%20Flow")

with project2:
    st.subheader("Project 2")
    st.write("I made a Face Recognition project in python, which is used to recognize the face of a person.")
    if st.button("Learn More", key="btn2"):
        st.write("https://github.com/Ali-Rozani/Python-Projects/tree/main/Face%20Reconigition")

st.header("Contact Me")
contact_form = st.form("contact_form")
name = contact_form.text_input("Your Name")
email = contact_form.text_input("Your Email")
message = contact_form.text_area("Your Message")
submit = contact_form.form_submit_button("Send Message")

if submit:
    st.success("Thanks for reaching out! I'll get back to you soon.")

with st.sidebar:
    st.title("Quick Links")
    st.write("[GitHub](https://github.com/Ali-Rozani)")