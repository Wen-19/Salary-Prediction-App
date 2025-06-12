import streamlit as st
import numpy as np
import pandas as pd
import datetime
from sklearn.linear_model import LinearRegression

# Title and Intro
st.title("Title: Bio Data")
st.write("This is my first web app.")

# Input Fields
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Your Age", 0, 100, 30, 1)
dob = st.date_input(
    "Your Birthday",
    min_value=datetime.date(1950, 1, 1),
    max_value=datetime.date.today()
)
marital_status = st.radio("Marital Status", ["Single", "Married"])
years_of_experience = st.slider("Years of experience", 0, 40)

# Job Role Selection
job_roles = ["Software Developer", "Data Analyst", "Project Manager", "Teacher", "Nurse", "Accountant", "Engineer"]
selected_job = st.selectbox("Select Your Job Role", job_roles)

# Profile Picture
profile_pic = st.file_uploader("Upload Profile Picture", type=["jpg", "png", "jpeg"])
if profile_pic:
    st.image(profile_pic, caption="Profile Picture", width=150)


# Submit and Save
if st.button("Submit", key="submit_button"):
    st.success("Here is your bio data:")

    # Display Details
    st.write(f"*Name:* {first_name} {last_name}")
    st.write(f"*Gender:* {gender}")
    st.write(f"*Age:* {age}")
    st.write(f"*Date of Birth:* {dob}")
    st.write(f"*Marital Status:* {marital_status}")
    st.write(f"*Years of Experience:* {years_of_experience}")
    st.write(f"*Job Role:* {selected_job}")

    # Save Data
    user_data = {
        "First Name": first_name,
        "Last Name": last_name,
        "Gender": gender,
        "Age": age,
        "Date of Birth": str(dob),
        "Marital Status": marital_status,
        "Years of Experience": years_of_experience,
        "Job Role": selected_job
    }

    df = pd.DataFrame([user_data])
    df.to_csv("user_data.csv", mode="a", header=False, index=False)
    st.success("Your data has been saved!")

# Salary Prediction from Experience
experience_data = {
    "Years of Experience": [1, 3, 5, 7, 10, 12, 15, 18, 20],
    "Salary": [30000, 45000, 60000, 75000, 90000, 105000, 120000, 135000, 150000]
}
df_model = pd.DataFrame(experience_data)
model = LinearRegression()
X = df_model[["Years of Experience"]]
y = df_model["Salary"]
model.fit(X, y)

if st.button("Predict Salary", key="salary_button"):
    predicted_salary = model.predict(np.array([[years_of_experience]]))[0]
    st.success(f"Estimated Salary based on experience: ${predicted_salary:,.2f}")

# Job-Based Salary Mapping
job_salary_map = {
    "Software Developer": 95000,
    "Data Analyst": 80000,
    "Project Manager": 90000,
    "Teacher": 50000,
    "Nurse": 65000,
    "Accountant": 70000,
    "Engineer": 85000
}

if st.button("Estimate Job-Based Salary"):
    job_salary = job_salary_map.get(selected_job, 0)
    st.info(f"Estimated Average Salary for a {selected_job}: ${job_salary:,.2f}")



    
