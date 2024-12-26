# Diabetes-Prediction-Model---Web-Application-Deployment

This repository contains code for building a Diabetes Prediction Machine Learning Model using the Support Vector Machine (SVM) algorithm and deploying it as a web application using Streamlit.

## Process Flow
This project consists of the following key steps:

### 1. Data Collection and Preprocessing

**Dataset**: We use the PIMA Diabetes Dataset to predict the likelihood of a person being diabetic based on various health parameters.
**Data Cleaning**: The data is explored and cleaned (if necessary), followed by separating the features (X) and target variable (Y), where Outcome indicates whether a person has diabetes (1) or not (0).
**Standardization**: We apply standardization to scale the features to have zero mean and unit variance, ensuring that all features contribute equally to the model.

### 2. Model Building (Training the SVM Classifier)
Support Vector Machine (SVM) is chosen for model training. The model is trained on the training data (X_train, Y_train).

**Model Evaluation**: After training, the model’s accuracy is evaluated on both the training and testing data using accuracy scores.

**Saving the Model**: The trained model is saved using pickle for future use, ensuring we can load the model without retraining it each time.

### Data Visualisation

![Heat Map](https://github.com/user-attachments/assets/fa118b15-be22-4b66-b204-76a2c8a7142c)


![Pair Plot](https://github.com/user-attachments/assets/7d282208-2f57-469c-8159-c146b439fddf)


![Distribution of Glucose Level](https://github.com/user-attachments/assets/896f75de-40f6-44df-af80-00b0f83521f0)


![Distribution of BMI](https://github.com/user-attachments/assets/006891e7-f004-4625-b581-42628d83faee)



### 3. Creating a Predictive System

Once the model is trained and saved, we create a Python script (predictive_system.py) for making predictions with the trained model.

The script loads the saved model and accepts new input data to predict if a person is diabetic or not.

### 4. Building the Web Application (Streamlit)

A Streamlit web application (diabetes_predictive_web.py) is built to allow users to input their health parameters through a simple web interface and receive real-time predictions.

Users can enter details like the number of pregnancies, glucose level, BMI, and other features, and upon clicking the "Diabetes Test Result" button, the app displays whether the user is diabetic or not.

### 5. Deploying the Web Application

**Deployment**: The web application is ready to be deployed locally or on a cloud platform (like Heroku or AWS).

**Running Locally**: To run the application locally, you need to install the required libraries and run the Streamlit app using the following commands:

This will start the Streamlit app on your local server.

![Web_Application](https://github.com/user-attachments/assets/61c0c045-feb1-4352-abd5-1cd086f3f331)


## Conclusion

This project demonstrates the process of building and deploying a machine learning model to predict diabetes using SVM, and then integrating it into a web application for real-time predictions.

