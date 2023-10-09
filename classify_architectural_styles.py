import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import cv2
import wikipedia
import base64

# Set configuration and title(s) for webpage
st.set_page_config(page_title = 'Classifying Architectural Styles', layout = "wide", initial_sidebar_state = "expanded", menu_items = None)
st.title("Multi-Class Image Classification with a Custom Convolutional Neural Network")
st.header(":orange[Classifying Architectural Styles]")
st.write("I built a custom CNN with the ability to predict the architectural style of a building from a given image among 25 popular architectural styles.")
st.write("Upload a colored picture of a building and see what architectural style the model predicts it is!")

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

