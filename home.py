import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import cv2
import wikipedia
import base64

st.set_page_config(page_title = 'Jonathan Yarber - Streamlit', layout = "wide", initial_sidebar_state = "expanded", menu_items = None)

# ============================================================================
# HOME WEBPAGE SETUP
# ============================================================================

# Create function for homepage
def home():
    # Set configuration and title(s) for webpage
    st.title("Personal Biography")
    st.sidebar.header("Homepage")

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

# ============================================================================
# CLASSIFY ARCHITECTURAL STYLES WEBPAGE SETUP
# ============================================================================

# Create function for webpage for this project
def classify_architectural_styles():
    # Set configuration and title(s) for webpage
    st.title("Multi-Class Image Classification with a Custom Convolutional Neural Network")
    st.header(":orange[Classifying Architectural Styles]")
    st.write("I built a custom CNN with the ability to predict the architectural style of a building from a given image among 25 popular architectural styles.")
    st.write("Upload a colored picture of a building and see what architectural style the model predicts it is!")
    st.sidebar.header("Classify Architectural Styles")

    # Create function to use model and perform necessary data preprocessing
    def custom_cnn_prediction(upload_img):
        # Load the saved custom CNN model from Jupyter Notebook
        model = tf.keras.models.load_model('ArchiNet2.h5')

        # Set the size
        size = (256, 256)

        # Fit the uploaded image to match size
        img = ImageOps.fit(upload_img, size, Image.LANCZOS)

        # Turn image into Numpy array
        img = np.array(upload_img)

        # Greyscale image array
        img_greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Resize image array for model
        img_resize = cv2.resize(img_greyscale, dsize = (256, 256), interpolation = cv2.INTER_CUBIC)

        # Add one more dimension to image array
        final_img = img_resize[np.newaxis, :]
        
        # Make prediction and return predictions
        model_prediction = model.predict(final_img)
        return model_prediction

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

    background_img('classifying_styles_background_image.jpg') 


    # Create dictionary of label values
    label_dict = {
        "Achaemenid": 0,
        "American Craftsman": 1,
        "American Foursquare": 2,
        "Ancient Egyptian": 3,
        "Art Deco": 4,
        "Art Nouveau": 5,
        "Baroque": 6,
        "Bauhaus": 7,
        "Beaux-Arts": 8,
        "Byzantine": 9,
        "Chicago School": 10,
        "Colonial": 11,
        "Deconstructivism": 12,
        "Edwardian": 13,
        "Georgian": 14,
        "Gothic": 15,
        "Greek Revival": 16,
        "International": 17,
        "Novelty": 18,
        "Palladian": 19,
        "Postmodern": 20,
        "Queen Anne": 21,
        "Romanesque": 22,
        "Russian Revival": 23,
        "Tudor Revival": 24
    }

    # Uploader for image
    upload = st.file_uploader("Choose an image of a building...", type = ["jpg", "png"])
    if upload is not None:
        img = Image.open(upload)
        st.image(img, caption = 'Successfully uploaded image.', use_column_width = False)
        st.markdown("\n")
        
        # Retrieve predicted label from model function
        label = np.argmax(custom_cnn_prediction(img))

        # Match returned predicted label from model to label_dict for predicted output
        st.subheader(f'Classified architectural style: :orange[{list(label_dict.keys())[list(label_dict.values()).index(label)]}], with a model confidence score of {custom_cnn_prediction(img).max():.0%}',
                    divider = 'rainbow')
        #st.write(f'{custom_cnn_prediction(img)}')  -- used in testing to check prediction probabilities for each label
        if label is None:
            st.text("Please upload an image.")
        
        st.markdown("\n")
        st.markdown("\n")

        # Return Wikipedia summary of predicted architectural style
        st.subheader("A brief summary from Wikipedia about this architectural style:")
        original_label = f'{list(label_dict.keys())[list(label_dict.values()).index(label)]}'
        search_query = original_label + (" architecture")
        wiki_result = wikipedia.search(search_query)
        page = wikipedia.page(wiki_result[0])
        summary = page.summary
        st.write(summary)

# ============================================================================
# GENERAL PROJECTS WEBPAGE SETUP
# ============================================================================

# Create function for webpage for other smaller projects
def general_projects():
    # Set configuration and title(s) for webpage
    st.title("General Projects")
    st.sidebar.header("General Projects")

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

# ============================================================================
# PERSONAL RESUME WEBPAGE SETUP
# ============================================================================

# Create function for webpage for personal resume
def personal_resume():
    # Set configuration and title(s) for webpage
    st.title("Personal Resume")
    st.write("Below are my current and previous positions I've held and the most concurrent responsibilities in each position.")
    st.sidebar.header("Resume")

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

    background_img('resume_background_image.jpg') 

    # Text for webpage
    st.header(":blue[Carter's Inc.]")
    st.subheader("Operational Analytics Manager")
    st.markdown("Sep 2022 - Present")
    st.markdown(":green[Skills: SQL - Tableau - Excel]")
    st.markdown("- Queries data from different databases with SQL to gather information to answer business questions")
    st.markdown("- Creates business reports and dashboards with Tableau to provide users with visiblity and interactivity to business questions or operational performance")
    st.markdown("- Builds warehouse staffing models for future forecasting based on estimated goals and demand")
    st.markdown("- Automates reporting and data acquisition to reduce manual intervention and data-entry errors")
    st.markdown("\n")
    st.subheader("Industrial Engineer")
    st.markdown("Mar 2021 - Sep 2022")
    st.markdown(":green[Skills: Excel - VBA - Standard Time Studies]")
    st.markdown("- Assists in the development of processes and mechanisms for labor forecasting, staffing, modeling, tracking, recognition program and other reporting as required to support management of engineering projects and decisions")
    st.markdown("- Collects and summarizes time study and work sampling data to support development of engineered labor standards, department goal setting and indirect staffing requirements")
    st.markdown("- Builds reusable data entry style templates for Operations, HR, IC, etc. and other departments that helps streamline processes, reduce errors and bring consistency across shifts")
    st.markdown("- Drafts and developments departmental leader guidebooks on how to operate, manage and run Operational departments efficiently and consistently across shifts")
    st.markdown("\n")
    st.markdown('***')
    st.markdown("\n")
    st.header(":red[The TJX Companies, Inc.]")
    st.subheader("Associate Industrial Engineer")
    st.markdown("Jun 2017 - Feb 2021")
    st.markdown(":green[Skills: Excel - Standard Time Studies]")
    st.markdown("- Create reporting and monitoring reports for the distribution network")
    st.markdown("- Initiate continuous improvement/lean concept, identify opportunities for improvement and make constructive suggestions for change")
    st.markdown("- Utilize data to analyze the feasibility or non-feasibility of multiple ROIs for new or updated equipment to improve the Operations in labor cost, material savings, and safety savings")
    st.markdown("- Evaluate, recommend and implement improvements to the execution of software to eliminate manual processes, reduce adjustments to pay accuracy for incentive labor, and reporting gaps")
    st.markdown("\n")
    st.subheader("Industrial Engineering Assistant")
    st.markdown("Jan 2016 - Jun 2017")
    st.markdown(":green[Skills: Excel - Standard Time Studies]")
    st.markdown("- Conducts frequency studies to develop and update standards; or validate frequencies within standards")
    st.markdown("- Assists the IE in the investigation of performance irregularities seen in the Productivity Accountability Tracking System (PATS) reports through observations or statistical analysis")
    st.markdown("- Conducts occurrence studies to determine how often non-MOSTED (work measurement data application system) events occur which must be included in standards")
    st.markdown("- Validates Preferred Methods and Engineered Standards to ensure accuracy and integrity of data")

# ============================================================================
# WEBPAGE SELECTION
# ============================================================================

# Create dictionary to reflect webpage functions
choose_page = {
    "homepage": home,
    "classify architectural styles": classify_architectural_styles,
    "general projects": general_projects,
    "resume": personal_resume}

# Set sidebar to select which webpage to go to
page_name = st.sidebar.selectbox("Select a page", choose_page.keys())
choose_page[page_name]()

