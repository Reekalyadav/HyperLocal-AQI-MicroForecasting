import joblib
import pandas as pd

# 1. Saved model ko load karo
model = joblib.load("aqi_model.pkl")

def predict_local_aqi(lat, lon, no2, traffic, dist_hway, park):
    # Data ko wahi format dena hoga jo training ke waqt tha
    input_data = pd.DataFrame([[lat, lon, no2, traffic, dist_hway, park]], 
                              columns=['latitude', 'longitude', 'satellite_no2', 'traffic_index', 'dist_to_highway_km', 'has_park_500m'])
    
    prediction = model.predict(input_data)
    return prediction[0]

# --- Testing for a specific spot in Ghaziabad ---
# Maan lo hum Indirapuram ke ek intersection ka check kar rahe hain
print("--- Hyper-Local AQI Checker ---")
my_lat = 28.6367
my_lon = 77.3731
satellite_val = 35.0  # Satellite se mili value
traffic_val = 8.5      # Heavy traffic jam
dist_to_road = 0.2    # Highway ke bilkul paas
has_park = 0          # Paas me koi park nahi hai

result = predict_local_aqi(my_lat, my_lon, satellite_val, traffic_val, dist_to_road, has_park)

print(f"Location: {my_lat}, {my_lon}")
print(f"Predicted AQI: {result:.2f}")

# Compare with a 'Green' area nearby
result_green = predict_local_aqi(my_lat, my_lon, satellite_val, 2.0, 2.5, 1)
print(f"Predicted AQI in nearby Green Area: {result_green:.2f}")