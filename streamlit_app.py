import streamlit as st  # Import Streamlit library for creating the web app
import numpy as np  # Import NumPy for numerical operations

# Setting the tittle of the app
st.title("Title: Bio Data")

# Displaying a short introductory message
st.write("This is my first web app.")

# Creating inputt fields for user data colllection
first_name = st.text_input("First Name")  # Text input for entering first name
last_name = st.text_input("Last Name")  
gender = st.selectbox("Gender", ["Male", "Female"])  
age = st.number_input("Your Age", 0, 100, 30, 1)  
dob = st.date_input("Your Birthday")  
marital_status = st.radio("Marital Status", ["Single", "Married"])  
years_of_experience = st.slider("Years of experience", 0, 40)  

#Adding a Profile Picture Upload Option
# Profile Picture Upload
profile_pic = st.file_uploader("Upload Profile Picture", type=["jpg", "png", "jpeg"])
# Display the uploaded image
if profile_pic:
    st.image(profile_pic, caption="Profile Picture", width=150)
#- Checks if a file has been uploaded.
# Displays the image using st.image(profile_pic, caption="Profile Picture", width=150).

