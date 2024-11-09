# E-commerce Yearly Spending Prediction Model

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Dependencies](#dependencies)
- [Future Improvements](#future-improvements)

## Project Overview
This project is an interactive machine learning application that predicts a customer’s yearly spending on an e-commerce platform based on user behavior and engagement metrics. Using a linear regression model, this project allows users to enter values for key features and receive a spending prediction through a Streamlit-based web interface.

## Features
- **User Input for Predictions**: The app lets users enter values for key metrics:
  - **Average Session Length**: Average time spent per session on the platform.
  - **Time on App**: Average time spent using the mobile app.
  - **Time on Website**: Average time spent on the website.
  - **Length of Membership**: Number of years the customer has been a member.

- **Machine Learning Model**: A linear regression model is trained to predict the `Yearly Amount Spent` based on the above metrics.

- **Interactive Streamlit Interface**: Users can input custom values for each metric, and the app will provide an estimated yearly spending amount in real-time.

## Dataset
The dataset used for training and testing, `ecommerce.csv`, contains anonymized customer data with the following features:
- `Avg. Session Length`
- `Time on App`
- `Time on Website`
- `Length of Membership`
- `Yearly Amount Spent` (Target variable)

## Model Training
The linear regression model is trained on 70% of the dataset, with 30% reserved for testing. The model uses features that correlate with yearly spending to provide accurate predictions.

## Project Structure
```plaintext
.
├── app.py                 # Main Streamlit app file
├── ecommerce.csv          # Dataset file
└── README.md              # Project documentation
How to Run

    Clone this repository and navigate to the project directory:

git clone https://github.com/AdarshKaintura/ecommerce-spending-prediction.git
cd ecommerce-spending-prediction

Install the required dependencies:

pip install -r requirements.txt

Start the Streamlit app:

    streamlit run app.py

    Open the app in your browser at http://localhost:8501.

Dependencies

    Python 3.6+
    pandas
    scikit-learn
    streamlit
    matplotlib
    seaborn

Future Improvements

    Experimenting with more complex models, such as Decision Trees or Random Forests, to improve accuracy.
    Adding more features to capture additional aspects of user behavior.
    Enhancing the app’s UI for a better user experience.
