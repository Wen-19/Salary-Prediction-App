import streamlit as st  # Import Streamlit library for creating the web app
import numpy as np  # Import NumPy for numerical operations

# Set the title of the app
st.title("Title: Bio Data")

# Display a short introductory message
st.write("This is my first web app.")

# Create input fields for user data collection
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



# Submit Button - When the user clicks Submit, their details are displayed.
if st.button("Submit", key="submit_button"):
    st.success("Here is your bio data:") 

    # Display user details below the success message
    st.write(f"**Name:** {first_name} {last_name}")  
    st.write(f"**Gender:** {gender}")  
    st.write(f"**Age:** {age}")  
    st.write(f"**Date of Birth:** {dob}")  
    st.write(f"**Marital Status:** {marital_status}")  
    st.write(f"**Years of Experience:** {years_of_experience}")  


#Saving User Data
import pandas as pd

# Store data in a dictionary when the user clicks the "Submit" button
if st.button("Submit"):
    user_data = {
        "First Name": first_name,  
        "Last Name": last_name,  
        "Gender": gender, 
        "Age": age,  
        "Date of Birth": str(dob),  
        "Marital Status": marital_status,  
        "Years of Experience": years_of_experience  
    }

    # Convert the dictionary into a Pandas DataFrame 
    df = pd.DataFrame([user_data])

    # Append data to the CSV file
    df.to_csv("user_data.csv", mode="a", header=False, index=False)

    # Show a success message after saving the data
    st.success("Your data has been saved!")

    #Salary Prediction
    import numpy as np
from sklearn.linear_model import LinearRegression

# Sample dataset for training (Years of Experience vs Salary)
data = {
    "Years of Experience": [1, 3, 5, 7, 10, 12, 15, 18, 20],
    "Salary": [30000, 45000, 60000, 75000, 90000, 105000, 120000, 135000, 150000]
}

# Convert data to Pandas DataFrame
df = pd.DataFrame(data)

# Train a simple Linear Regression model
model = LinearRegression()
X = df[["Years of Experience"]]
y = df["Salary"]
model.fit(X, y)

# Salary Prediction Section
if st.button("Predict Salary", key="salary_button"):
    predicted_salary = model.predict(np.array([[years_of_experience]]))[0]
    st.success(f"Estimated Salary: ${predicted_salary:,.2f}")

