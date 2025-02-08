import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load Model
model = joblib.load('Saved_Preprocessing/model.pkl')
scaler = joblib.load('Saved_Preprocessing/scaler.pkl')
kmeans = joblib.load('Saved_Preprocessing/kmeans.pkl')
poly = joblib.load('Saved_Preprocessing/poly.pkl')

# Custom CSS untuk UI Streamlit
st.markdown(
    """
    <style>
    body {
        background-color: #87CEEB; /* Warna biru langit */
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background: linear-gradient(to bottom, #87CEEB, #f0f8ff);
    }
    .title {
        text-align: center;
        font-size: 36px;
        color: white;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .container {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Tampilan Awal
st.markdown("<h1 class='title'>Prediksi NO₂ dengan Machine Learning</h1>", unsafe_allow_html=True)
st.markdown("<div class='container'>", unsafe_allow_html=True)

# UI di Streamlit
st.title("NO₂ Prediction App")

# Input user (bisa negatif)
precipitation = st.number_input("Precipitation", min_value=None, value=0.0)
lst = st.number_input("LST", min_value=None, value=0.0)
aai = st.number_input("AAI", min_value=None, value=0.0)
cloud_fraction = st.number_input("Cloud Fraction", min_value=None, value=0.0)
no2_strat = st.number_input("NO2_strat", min_value=None, value=0.0)
no2_total = st.number_input("NO2_total", min_value=None, value=0.0)
no2_trop = st.number_input("NO2_trop", min_value=None, value=0.0)
tropopause_pressure = st.number_input("Tropopause Pressure", min_value=None, value=0.0)

# Tombol prediksi
if st.button("Predict"):
    # Buat DataFrame dari input user
    input_data = pd.DataFrame([[precipitation, lst, aai, cloud_fraction, no2_strat, no2_total, no2_trop, tropopause_pressure]], 
                               columns=['Precipitation', 'LST', 'AAI', 'CloudFraction', 'NO2_strat', 
                                        'NO2_total', 'NO2_trop', 'TropopausePressure'])

    # Transformasi KMeans
    input_data['Kmeans'] = kmeans.predict(input_data[['NO2_strat', 'NO2_total', 'NO2_trop']])

    # Standardize TropopausePressure
    input_data['TropopausePressure'] = scaler.transform(input_data[['TropopausePressure']])

    # Polynomial Features
    poly_features = poly.transform(input_data[['Precipitation', 'LST', 'AAI']])
    poly_feature_columns = poly.get_feature_names_out(['Precipitation', 'LST', 'AAI'])
    poly_data = pd.DataFrame(poly_features, columns=poly_feature_columns)

    # Hapus fitur original yang tidak diperlukan
    poly_data.drop(['1', 'Precipitation', 'LST', 'AAI'], axis=1, inplace=True)

    # Gabungkan hasil polynomial dengan input_data
    final_input = pd.concat([input_data, poly_data], axis=1)

    # Prediksi dengan model
    prediction = model.predict(final_input)[0]

    # Tampilkan hasil prediksi dengan emoticon
    if prediction >= 10:
        st.success(f"Predicted NO₂: {prediction:.5f} 😊")
    else:
        st.error(f"Predicted NO₂: {prediction:.5f} 😞")
