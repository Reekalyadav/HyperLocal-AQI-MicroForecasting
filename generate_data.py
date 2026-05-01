import pandas as pd
import numpy as np

def generate_ghaziabad_data():
    print("Ghaziabad ka synthetic AQI data ban raha hai...")
    
    # Ghaziabad ke kuch main points ke coordinates
    locations = {
        "Indirapuram": [28.6367, 77.3731],
        "Raj Nagar": [28.6793, 77.4429],
        "Loni": [28.7517, 77.2872],
        "Sanjay Nagar": [28.6888, 77.4520],
        "Vasundhara": [28.6602, 77.3672],
        "Sahibabad": [28.6656, 77.3456],
        "Vijay Nagar": [28.6431, 77.4371],
        "Kavi Nagar": [28.6698, 77.4402]
    }
    
    data_list = []
    
    # Hum 500 rows ka data banayenge taaki model ko sikhne ke liye kaafi material mile
    for i in range(500):
        loc_name = np.random.choice(list(locations.keys()))
        base_lat, base_long = locations[loc_name]
        
        # Thoda sa random variation taaki 500m ke alag alag points bane
        lat = base_lat + np.random.uniform(-0.005, 0.005)
        lon = base_long + np.random.uniform(-0.005, 0.005)
        
        # AQI value (PM2.5): Traffic wale areas me jyada, green areas me kam
        # Hum random value generate kar rahe hain 50 se 350 ke beech
        pm25_value = np.random.randint(50, 350) 
        
        data_list.append({
            "location_cluster": loc_name,
            "latitude": lat,
            "longitude": lon,
            "pm25": pm25_value,
            "unit": "µg/m³"
        })
    
    df = pd.DataFrame(data_list)
    
    # CSV save karna
    df.to_csv("ghaziabad_aqi_data.csv", index=False)
    print("Safalta! 'ghaziabad_aqi_data.csv' ban gayi hai 500 records ke saath.")
    print(df.head())

if __name__ == "__main__":
    generate_ghaziabad_data()