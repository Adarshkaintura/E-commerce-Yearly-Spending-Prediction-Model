import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("archive/ecommerce.csv")

# Define features and target variable
X = df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = df['Yearly Amount Spent']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the Linear Regression model
lm = LinearRegression()
lm.fit(X_train, y_train)

# Streamlit App
st.title("E-commerce Yearly Spending Prediction")
st.write("Enter the details below to predict the yearly amount spent.")

# User inputs for prediction
session_length = st.number_input("Average Session Length", min_value=0.0, max_value=50.0, value=34.0)
time_on_app = st.number_input("Time on App", min_value=0.0, max_value=50.0, value=12.0)
time_on_website = st.number_input("Time on Website", min_value=0.0, max_value=50.0, value=37.0)
length_of_membership = st.number_input("Length of Membership", min_value=0.0, max_value=10.0, value=4.0)

# Prediction button
if st.button("Predict Yearly Amount Spent"):
    # Prepare the input data as a DataFrame
    user_data = pd.DataFrame([[session_length, time_on_app, time_on_website, length_of_membership]], 
                             columns=['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership'])
    
    # Make prediction
    prediction = lm.predict(user_data)
    
    # Display result
    st.write(f"Predicted Yearly Amount Spent: ${prediction[0]:.2f}")
