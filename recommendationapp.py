# Predictive Maintenance Recommendation System Integrated with IoT to Reduce Unplanned Downtime

# Imports
import joblib
import streamlit as st
import numpy as np
import pandas as pd

# Load the saved model and scaler
model_file = 'models/model_v1.pkl'
scaler_file = 'scalers/scaler_v1.pkl'
model = joblib.load(model_file)
scaler = joblib.load(scaler_file)

# Function to make maintenance recommendations
def maintenance_recommendation(new_data):
    # Define column names as per the scaler
    columns = ['vibration', 'temperature', 'pressure', 'humidity', 'working_hours']
    
    # Convert the new data into a DataFrame with correct column names
    new_data_df = pd.DataFrame([new_data], columns=columns)
    
    # Apply the scaler to the new data
    new_data_scaled = scaler.transform(new_data_df)
    
    # Make predictions
    prediction = model.predict(new_data_scaled)
    prediction_proba = model.predict_proba(new_data_scaled)[:, 1]

    # Return the predicted class and probability
    return prediction[0], prediction_proba[0]

# Configure the Streamlit app page
st.set_page_config(page_title="Predictive Maintenance System", page_icon="⚙️", layout="centered")

# Define the app title
st.title("Predictive Maintenance Recommendation System 🌐")

# Define an explanatory caption for the app
st.caption("Integrated IoT and Machine Learning for Business Analytics")

# Input header
st.header("Enter sensor values:")
vibration = st.number_input("Vibration", value=0.0)
temperature = st.number_input("Temperature (°C)", value=0.0)
pressure = st.number_input("Pressure (PSI)", value=0.0)
humidity = st.number_input("Humidity (%)", value=0.0)
working_hours = st.number_input("Working Hours", value=0)

# Button to make a prediction
if st.button("Check Maintenance Need"):
    new_data = [vibration, temperature, pressure, humidity, working_hours]
    prediction_class, prediction_probability = maintenance_recommendation(new_data)
    
    # Display results
    st.write(f"Prediction: {'Perform maintenance' if prediction_class == 1 else 'No maintenance needed'}")
    st.write(f"Maintenance probability: {prediction_probability:.2%}")
