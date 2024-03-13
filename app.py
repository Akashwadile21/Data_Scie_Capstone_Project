# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15oPSvbbu5GgYg0lQSgrRXKvaEW98FaOv
"""

pip install streamlit

from google.colab import drive
drive.mount('/content/drive')

import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import math

best_model = pickle.load(open('best_model.pkl','rb'))

brand_names = pickle.load(open('brand_name.pkl','rb'))
model_names = pickle.load(open('model_name.pkl','rb'))


best_model = pickle.load(open('best_model.pkl','rb'))

cleaned_data = pd.read_csv('Eda.csv')

st.title('Car Price Prediction')
# st.sidebar.title('Enter Car Details')

col1, col2 = st.columns(2)

# Input fields for the first column
with col1:
    year = st.slider('Year', min_value= cleaned_data['Year'].min(), max_value= cleaned_data['Year'].max())
    km_driven = st.slider('Kilometers Driven', min_value=cleaned_data['Km_Driven'].min(), max_value=cleaned_data['Km_Driven'].max())
    fuel = st.selectbox('Fuel Type', cleaned_data['Fuel'].unique())
    seller_type = st.selectbox('Seller Type', cleaned_data['Seller_Type'].unique())

# Input fields for the second column
with col2:
    transmission = st.selectbox('Transmission', cleaned_data['Transmission'].unique())
    owner = st.selectbox('Owner', cleaned_data['Owner'].unique())
    brand = st.selectbox('Brand',cleaned_data['Brand'].unique())
    brand_filter = cleaned_data[cleaned_data['Brand'] == brand]
    model = st.selectbox('Model', brand_filter['Model'].unique())




input_data = pd.DataFrame({
    'Year' : [year],
    'Km_Driven' : [km_driven],
    'Fuel' : [fuel],
    'Seller_Type' :[seller_type],
    'Transmission' : [transmission],
    'Owner' : [owner],
    'Brand' : [brand],
    'Model' : [model]

})

encoder = LabelEncoder()
fuel_encoded = encoder.fit_transform([fuel])[0]
seller_type_encoded = encoder.fit_transform([seller_type])[0]
transmission_encoded = encoder.fit_transform([transmission])[0]
owner_encoded = encoder.fit_transform([owner])[0]
brand_encoded = encoder.fit_transform([brand])[0]
model_encoded = encoder.fit_transform([model])[0]
    # Create DataFrame from user inputs
input_data = pd.DataFrame({
        'Year': [year],
        'Km_driven': [km_driven],
        'Fuel': [fuel_encoded],
        'Seller_Type': [seller_type_encoded],
        'Transmission': [transmission_encoded],
        'Owner': [owner_encoded],
        'Brand' : [brand_encoded],
        'Model' : [model_encoded]
    })

# Function to retrieve selling price for selected model
def get_selling_price(model):
    selling_price = Eda.loc[cleaned_data['Model'] == model, 'Selling_Price'].values
    if len(Selling_Price) > 0:
        return Selling_Price[0]
    else:
        return None


if st.button('prediction'):
   # Make prediction
    prediction = best_model.predict(input_data)
    predicted_selling_price = prediction[0]

    # Retrieve actual selling price for the selected model
    actual_selling_price = get_selling_price(Model)

    if actual_selling_price is not None:
        st.success(f'Predicted Selling Price: {predicted_selling_price:.2f} INR')
        st.success(f'Actual Selling Price: {actual_selling_price:.2f} INR')
    else:
        st.error("Actual selling price not available for the selected car model.")

