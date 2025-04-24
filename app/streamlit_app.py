import streamlit as st
import numpy as np
import joblib
import os

# Load model
model_path = 'models/best_model.pkl'
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("Model not found! Please train and save your model first.")
    st.stop()

# App config
st.set_page_config(page_title="🏠 Energy Load Predictor", layout="centered")

# Sidebar
st.sidebar.title("🔧 Input Features")
st.title("🏡 Building Energy Efficiency Prediction")
st.markdown("Predict **Heating** and **Cooling Load** of a building based on its features.")

# Input sliders
compactness = st.sidebar.slider('Relative Compactness', 0.5, 1.0, 0.75)
surface_area = st.sidebar.slider('Surface Area (m²)', 400, 800, 600)
wall_area = st.sidebar.slider('Wall Area (m²)', 200, 400, 300)
roof_area = st.sidebar.slider('Roof Area (m²)', 100, 300, 150)
overall_height = st.sidebar.selectbox('Overall Height (m)', [3.5, 7.0])
orientation = st.sidebar.selectbox('Orientation', ['2', '3', '4', '5'])
glazing_area = st.sidebar.slider('Glazing Area (0–1)', 0.0, 0.5, 0.1)
glazing_dist = st.sidebar.selectbox('Glazing Area Distribution', ['0', '1', '2', '3', '4', '5'])

# Encode orientation & glazing_dist (dummy vars)
orientation_dummies = [0, 0, 0]
if orientation == '3':
    orientation_dummies[0] = 1
elif orientation == '4':
    orientation_dummies[1] = 1
elif orientation == '5':
    orientation_dummies[2] = 1

glazing_dummies = [0, 0, 0, 0, 0]
if glazing_dist != '0':
    glazing_dummies[int(glazing_dist) - 1] = 1

# Input vector
input_data = np.array([
    compactness,
    surface_area,
    wall_area,
    roof_area,
    overall_height,
    glazing_area,
    *orientation_dummies,
    *glazing_dummies
]).reshape(1, -1)

# Predict button
if st.button("🔍 Predict Energy Load"):
    prediction = model.predict(input_data)
    heating, cooling = prediction[0]

    st.success("✅ Prediction Completed!")
    st.markdown("---")
    st.subheader("📈 Results")
    st.metric(label="🔥 Heating Load (kWh/m²)", value=f"{heating:.2f}")
    st.metric(label="❄️ Cooling Load (kWh/m²)", value=f"{cooling:.2f}")
    st.markdown("---")
    st.caption("Built by Dipankar Maumdar with ❤️ using Streamlit") 