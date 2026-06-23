import streamlit as st
import pandas as pd
import pickle

# 1. Load the saved brain (Model and Scaler)
with open('insurance_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# 2. Build the User Interface (UI)
st.title("🏥 Insurance Premium Predictor")
st.write("Enter your details below to estimate your annual insurance cost.")

# Create the input fields for the user
input_age = st.number_input("Age", min_value=18, max_value=100, value=30)
input_bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=60.0, value=25.0)
input_children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)

sex = st.selectbox("Gender", ["Female", "Male"])
smoker = st.selectbox("Do you smoke?", ["No", "Yes"])
region = st.selectbox("Region", ["Southeast", "Other Regions"])

# 3. Backend Processing (When user clicks the button)
if st.button("Predict Premium"):
    
    # Map the human words to 1s and 0s just like your notebook did
    input_is_female = 1 if sex == "Female" else 0
    input_is_smoker = 1 if smoker == "Yes" else 0
    input_region_southeast = 1 if region == "Southeast" else 0
    input_bmi_category_obese = 1 if input_bmi >= 30 else 0
    
    # Scale the numeric parts automatically behind the scenes
    raw_numeric_data = pd.DataFrame([{
        'age': input_age,
        'bmi': input_bmi,
        'children': input_children
    }])
    scaled_numeric_values = scaler.transform(raw_numeric_data)
    
    # Structure the processed data perfectly for the machine
    new_person = pd.DataFrame([{
        'age': scaled_numeric_values[0][0],
        'is_smoker': input_is_smoker,
        'children': scaled_numeric_values[0][2],
        'region_southeast': input_region_southeast,
        'is_female': input_is_female,
        'bmi': scaled_numeric_values[0][1],
        'bmi_category_obese': input_bmi_category_obese
    }])
    
    # 4. Generate the Prediction
    prediction = model.predict(new_person)
    
    # Display it beautifully to the user
    st.success(f"### Estimated Annual Insurance Premium: ${prediction[0]:,.2f}")