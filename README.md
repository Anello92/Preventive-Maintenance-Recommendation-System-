# Maintenance Recommendation System with IoT and Machine Learning

## Overview

This project demonstrates the creation of a **Predictive Maintenance Recommendation System**, leveraging **IoT sensor data** and **Machine Learning** to reduce unplanned downtimes. Using simulated datasets, the goal is to develop a system capable of recommending maintenance actions based on historical sensor readings, ensuring improved operational efficiency.

## Key Features

- **Imbalanced Data Handling**: Implementation of five distinct strategies to address class imbalance.
- **Machine Learning Models**: Development and evaluation of five different versions, with the **best model (version 1)** selected for deployment.
- **Web Application Deployment**: An interactive app built with **Streamlit** for user-friendly maintenance recommendations.
- **Performance Metrics**: Analysis based on metrics like **Accuracy** and **AUC-ROC** to ensure model robustness.
- **Scalability**: Designed for integration into real-world industrial scenarios.

## Repository Structure

```plaintext
.
├── dataset.csv                      # Simulated IoT sensor dataset
├── Maintenance_Recommendation_System.ipynb # Complete project notebook
├── models/
│   ├── model_v1.pkl                 # Selected model for deployment
│   ├── model_v2.pkl
│   ├── model_v3.pkl
│   ├── model_v4.pkl
│   └── model_v5.pkl
├── recommendationapp.py             # Streamlit app for deployment
├── scalers/
│   ├── scaler_v1.pkl                # Scaler for version 1
│   ├── scaler_v2.pkl
│   ├── scaler_v3.pkl
│   ├── scaler_v4.pkl
│   └── scaler_v5.pkl

```plaintext


Installation

Clone the repository:
git clone https://github.com/Anello92/Maintenance-Recommendation-System.git
cd Maintenance-Recommendation-System
Install the required Python packages:
pip install -r requirements.txt
Ensure all necessary files (models and scalers directories) are in place.
Usage

Running the Jupyter Notebook
Open the project notebook to explore the entire pipeline:

jupyter notebook Maintenance_Recommendation_System.ipynb
Running the Streamlit App
To deploy the web application:

Navigate to the project directory.
Execute the following command:
streamlit run recommendationapp.py
The app will launch in your default browser, ready to provide maintenance recommendations.
Key Steps in the Project

1. Data Preprocessing
Dataset: Simulated IoT sensor data containing five predictive variables and one target variable (maintenance_required).
Class Imbalance Handling: Techniques such as undersampling, oversampling, and SMOTE were applied to balance the dataset.
2. Model Development
Developed and evaluated five versions using strategies like class balancing, algorithm adjustments, and automated oversampling techniques.
Metrics like Accuracy and AUC-ROC guided model evaluation.
3. Model Selection
Version 1 was selected as the best model due to its simplicity, high performance, and minimal data transformations.
4. Deployment
A Streamlit app provides user-friendly recommendations based on new IoT sensor readings.
Outputs include both class predictions (Yes/No for maintenance) and probabilities for informed decision-making.
Example Outputs

App Interface
Sample Prediction
Input: IoT sensor readings
Output: Recommendation for maintenance with associated probability
Future Enhancements

Feature Engineering: To improve model performance with additional predictive features.
Hyperparameter Optimization: Fine-tune models for better results.
Extended Deployment: Integration into industrial pipelines using tools like Docker or cloud services.
References and Credits

Scikit-learn for machine learning algorithms and utilities.
Streamlit for building the deployment app.
Imbalanced-learn for handling class imbalance with techniques like SMOTE.
Special thanks to the contributors who made this project possible.
