from PIL import Image
import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon=":waving_hand:", layout="wide")

# Use Local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css.txt")

my_portfolio = Image.open("my_portfolio.PNG")
my_facebook = Image.open("facebook-logo.png")
my_github = Image.open("github-logo.png")
my_gmail = Image.open("gmail-logo.png")
my_linkedin = Image.open("linkedin-logo.png")

#----header section----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Hi, I am Dawood Khatri :wave:")
        st.title("A Web Developer from Karachi")
        st.write("I am passionate about finding ways to use python")
        st.write("[Learn more > ](https://github.com/dawoodkhatri1)")

#----What I DO----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I create a website and my skills are backend development.\n
            For further details check out my Github account.
            """
        )
        st.write("[My Github account > ](https://github.com/dawoodkhatri1)")

#----Projects----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(my_portfolio)
    with text_column:
        st.subheader("My Projects of Python, linux and C++")
        st.write(
            """
            You can take a look at my projects 
            """
        )
        st.markdown("[Click the link to proceed...](https://github.com/dawoodkhatri1?tab=repositories)")

#----CONTACT----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.com/dawoodm.shoaib@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder ="Your name" required>
        <input type="email" name="email" placeholder ="Your email" required>
        <textarea name="message" placeholder ="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

#----Contact Info----
st.write("---")
st.header("Connect With Me!")
st.write("##")
st.subheader("Email")
st.image(my_gmail)
st.markdown("[Click the link to proceed...](dawoodm.shoaib@gmail.com)")

st.write("##")
st.subheader("LinkedIn")
st.image(my_linkedin)
st.markdown("[Click the link to proceed...](https://www.linkedin.com/in/dawood-m-shoaib-a6229722a/)")

st.write("##")
st.subheader("Facebook")
st.image(my_facebook)
st.markdown("[Click the link to proceed...](https://www.facebook.com/dawoodm.shoaib?mibextid=ZbWKwL)")

st.write("##")
st.subheader("Gihub")
st.image(my_github)
st.markdown("[Click the link to proceed...](https://github.com/dawoodkhatri1)")

