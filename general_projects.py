import streamlit as st
import base64

# Set configuration and title(s) for webpage
st.set_page_config(page_title = 'General Project', layout = "wide", initial_sidebar_state = "expanded", menu_items = None)
st.title("General Projects")

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

background_img('general_projects_background_image.jpg') 

# Text for webpage - links to other projects on Github
st.write("Here, I will place other smaller-scale projects or past projects.  Any projects with its own functionality will have its own page.")
st.markdown('***')
st.subheader(":orange[Setting Up Shop in Rockingham County, VA - Where to Start Your Business  |  May 2020]")
st.write("My first ever data science project was done in 2020, in effort to complete the IBM Data Science Certificate program.  "
         "In this self-devised project with location information, I decided to focus on something close to home.  Or at least what was home at the time.  "
         "That being the Rockingham County area, which housed several cities.  In this project, I leveraged Foursquare's API to determine the most common venue of each city in the county.  "
         "With other data collected from other website sources, I sought to answer a theoretical question: if you were to set up either a new restaurant or contractor firm, what city in the county would be the best for each?")
st.write("For this project, I present a Python notebook of the code used, a CSV file of the minor data collected, PowerPoint presentation slides, and a PDF paper.  Please feel free to check out my project on Github at the below link!")
st.markdown("**[Link to Project on Github](https://github.com/JonathanYarber/Rockingham-County-VA-Best-New-Business-Location/tree/master)**")
st.markdown('***')