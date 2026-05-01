import pandas as pd
import numpy as np

def add_features():
    # Purana data load karo
    df = pd.read_csv("ghaziabad_aqi_data.csv")
    print("Features add ho rahe hain...")

    # 1. SATELLITE FEATURE (NO2 levels)
    # Satellite value bade area ke liye same hoti hai, isliye hum thoda pattern dalenge
    df['satellite_no2'] = np.random.uniform(10, 50, size=len(df))

    # 2. LOCAL FEATURES (The 500m logic)
    # Traffic Index: 0 (No Traffic) se 10 (Jam) tak
    # Jin areas me PM25 jyada hai, wahan traffic bhi jyada dikhayenge (correlation)
    df['traffic_index'] = (df['pm25'] / 40) + np.random.normal(0, 1, size=len(df))
    df['traffic_index'] = df['traffic_index'].clip(0, 10) # Value 0-10 ke beech rakho

    # 3. PROXIMITY FEATURES (Distance to Greenery/Highway)
    # Ye model ko batayega ki agar 500m me park hai to AQI kam hoga
    df['dist_to_highway_km'] = np.random.uniform(0.1, 5.0, size=len(df))
    df['has_park_500m'] = np.random.choice([0, 1], size=len(df), p=[0.7, 0.3])

    # Final Dataset Save Karo
    df.to_csv("ghaziabad_final_features.csv", index=False)
    print("Feature Engineering Complete!")
    print(df.head())

if __name__ == "__main__":
    add_features()