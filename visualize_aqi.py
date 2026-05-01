import folium
import joblib
import pandas as pd

# 1. Model load karo
model = joblib.load("aqi_model.pkl")

# 2. Map initialize karo (Ghaziabad ke coordinates par)
m = folium.Map(location=[28.6692, 77.4538], zoom_start=12)

# 3. Hum kuch random points par prediction karke unhe map par dikhayenge
# Hum purana data hi load kar lete hain dikhane ke liye
df = pd.read_csv("ghaziabad_final_features.csv").head(50) # Pehle 50 points

for index, row in df.iterrows():
    # Prediction lena
    features = [[row['latitude'], row['longitude'], row['satellite_no2'], 
                 row['traffic_index'], row['dist_to_highway_km'], row['has_park_500m']]]
    
    aqi_val = model.predict(features)[0]
    
    # --- YAHAN HAI COLOR KA LOGIC ---
    if aqi_val > 250:
        color = 'red'
    elif aqi_val > 150:
        color = 'orange'
    else:
        color = 'green'
    
    # Map par circle lagana
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=10,
        popup=f"AQI: {aqi_val:.2f}",
        color=color,
        fill=True,
        fill_color=color
    ).add_to(m)

# 4. Map ko HTML file mein save karna
m.save("aqi_map.html")
print("Visual Map 'aqi_map.html' ke naam se save ho gaya hai. Isse browser me open karo.")