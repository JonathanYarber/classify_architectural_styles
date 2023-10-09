import streamlit as st
import base64

# Set configuration and title(s) for webpage
st.set_page_config(page_title = 'Resume', layout = "wide", initial_sidebar_state = "expanded", menu_items = None)
st.title("Personal Resume")
st.write("Below are my current and previous positions I've held and the most concurrent responsibilities in each position.")

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

