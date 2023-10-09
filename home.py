import streamlit as st
import base64

# Set configuration and title(s) for webpage
st.set_page_config(page_title = 'Personal Biography', layout = "wide", initial_sidebar_state = "expanded", menu_items = None)
st.title("Personal Biography")

# Create function to set background image for webpage
# Original source code: https://stackoverflow.com/questions/73019925/how-to-change-the-background 
def background_img(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())

    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
        }}
    </style>
    """, 
    unsafe_allow_html = True)

background_img('home_background_image.jpg') 

# Text for webpage
st.markdown("\n")
fake_code_1 = '''def hello():
    print("Welcome to my website!")'''
st.code(fake_code_1, language = 'python')
st.write("Hello everyone!  My name is Jonathan Yarber.  For the past few years, I've been slowly breaking into the data space.  My aspirations have evolved from my former education and career experience "
         "in the industrial engineering realm to now aiming to become a full-fledged data scientist.  I first learned about this field in early 2020, and am pursuing graduate-level education to hone my "
         "understanding further.  In my current role within operational data analytics, I help supply chain data initiatives, querying information from databases, and creating reliable reports/dashboards "
         "to answer business questions and provide unique insight.  I thoroughly enjoy having the chance to use data in applied ways, and I have created this Streamlit-based website to showcase what I am "
         "learning.")
st.markdown("\n")
st.write("I hope to further develop myself with working on project-based learning by using different kinds of data science techniques and methods in five major areas of interest of mine, those being:")
st.markdown("- Architecture")
st.markdown("- Oceanography")
st.markdown("- Astronomy")
st.markdown("- Entertainment")
st.markdown("- Criminal Justice")
st.markdown("\n")
st.write("From neural networks to large language models, I hope to be able to have a firm understanding and application of each.  Jack of all trades, master of none, as I have often been.")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("Links to my [Github](https://github.com/JonathanYarber) and [Linkedin](https://www.linkedin.com/in/jonathan-yarber/)")

# self note:
# navigate to folder location to run streamlit app with:
# python -m streamlit run filename.py