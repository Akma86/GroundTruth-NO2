# NO₂ Prediction with Machine Learning

## 📌 Introduction

### 🔎 What is NO₂?
NO₂ (Nitrogen Dioxide) is a gas primarily produced from the combustion of fossil fuels, such as in motor vehicles and power plants. It is one of the major components of air pollution and has detrimental effects on human health, particularly the respiratory system. This project analyzes the concentration levels of NO₂ in various locations to understand its distribution patterns and its impact on air quality.

### 🌍 Importance of Monitoring NO₂
Monitoring NO₂ levels is crucial as it contributes to the formation of secondary pollutants, such as ground-level ozone, which is harmful to human health. By analyzing NO₂ data, we can identify areas with high pollution levels and propose policies or solutions to reduce its impact on public health.

---

## 📊 Data Description

The **GroundTruth-NO₂** dataset contains various environmental factors that affect NO₂ concentration levels, such as temperature, humidity, wind speed, and sensor location. The dataset is time-series based, collected from multiple sensors across different locations.

### 📌 Dataset Features:
- `datetime`: Date and time of measurement  
- `latitude`: Latitude of the sensor  
- `longitude`: Longitude of the sensor  
- `temperature`: Temperature in Celsius  
- `humidity`: Humidity percentage  
- `wind_speed`: Wind speed in meters per second  
- `NO2_level`: Groundtruth NO₂ concentration (target variable)  

---

## 🛠️ Methodology

### 🔎 1. Exploratory Data Analysis (EDA)
- Distribution analysis of NO₂ levels  
- Correlation analysis between features  
- Handling missing values and outliers  
- Geospatial visualization of NO₂ levels  

### 🧹 2. Data Preprocessing
- Handling missing values  
- Feature scaling using **StandardScaler**  
- Feature engineering: **polynomial features & clustering (KMeans)**  
- Splitting data into training and testing sets  

### 🤖 3. Model Development
Several machine learning models are tested, including:
- **Random Forest** 🌲  
- **XGBoost** 🚀  

Feature engineering includes adding:
- **KMeans Clustering**
- **Polynomial features** such as `Precipitation²`, `LST²`, and their interactions  

---

## 📈 Model Evaluation

### 📊 Metrics Used:
- **Mean Absolute Error (MAE)**  
- **Mean Squared Error (MSE)**  
- **R-Squared (R²)**  

---

## 🚀 Deployment with Streamlit

This project is deployed using **Streamlit** to allow users to input environmental factors and get NO₂ predictions.

### 🎨 Features of the Streamlit App:
✅ **User-friendly UI** with a gradient sky-blue theme 🌤️  
✅ **Interactive input fields** for environmental variables 📊  
✅ **Real-time NO₂ predictions** with emoji-based feedback 😃😢  

### 🛠️ How to Run the App:
```bash
pip install -r requirements.txt
streamlit run app.py
