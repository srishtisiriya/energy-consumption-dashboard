import streamlit as st
import pandas as pd

# Load the household data (make sure to provide the correct path)
household_data_path = r'C:\Users\Srishti\Downloads\electricity_bill_dataset.csv'
household_data = pd.read_csv(household_data_path)

# Title of the app
st.title('Energy Consumption Prediction Dashboard')

# Input for appliance usage
st.header('Input Appliance Usage')
fan = st.number_input('Number of Fans', min_value=0, max_value=10, value=2)
refrigerator = st.number_input('Number of Refrigerators', min_value=0, max_value=5, value=1)
air_conditioner = st.number_input('Number of Air Conditioners', min_value=0, max_value=5, value=1)
television = st.number_input('Number of Televisions', min_value=0, max_value=10, value=2)
monthly_hours = st.number_input('Monthly Hours of Usage', min_value=0, max_value=500, value=100)

# Example: Predict electricity bill based on simple logic
# This should be replaced with your actual model prediction logic
predicted_bill = (fan * 0.5 + refrigerator * 1.2 + air_conditioner * 2.5 + television * 0.3) * monthly_hours

# Display the predicted result
st.write(f'Predicted Electricity Bill: ₹{predicted_bill:.2f}')

# Optional: Display the data
st.subheader('Household Data Preview:')
st.dataframe(household_data.head())
