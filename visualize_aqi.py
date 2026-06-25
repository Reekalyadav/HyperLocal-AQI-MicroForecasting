import pandas as pd
import joblib
import folium

print("Saved Random Forest Model aur dataset load ho raha hai...")
# Model aur current CSV load karein
model = joblib.load('aqi_model.pkl')
df = pd.read_csv('ghaziabad_aqi_data.csv')

# Features select karke model se final predictions nikalte hain
X = df[['PM2.5', 'NO2', 'Traffic_Index', 'Distance_to_Highway', 'Distance_to_Park']]
df['Predicted_AQI'] = model.predict(X)

print("Ghaziabad ke center par Interactive Map ban raha hai...")
# Ghaziabad ke center par map shuru karte hain
m = folium.Map(location=[28.6692, 77.4538], zoom_start=13, tiles="OpenStreetMap")

# Map par color zones chunne ke liye helper function
def get_aqi_color(aqi):
    if aqi <= 50: return 'green'       # Safe
    elif aqi <= 100: return 'yellow'   # Moderate
    elif aqi <= 200: return 'orange'   # Unhealthy
    else: return 'red'                 # Hazardous / Danger

# Har ek coordinate par circle mark lagana
for idx, row in df.iterrows():
    color = get_aqi_color(row['Predicted_AQI'])
    
    popup_text = f"""
    <b>Location Specific Air Quality</b><br>
    Predicted AQI: {row['Predicted_AQI']:.2f}<br>
    PM2.5: {row['PM2.5']:.1f}<br>
    NO2: {row['NO2']:.1f}<br>
    Traffic Index: {row['Traffic_Index']:.1f}
    """
    
    # Galti yahan theek kar di gayi h -> row['Longitude'] direct use kiya h
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=8,
        popup=folium.Popup(popup_text, max_width=250),
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6
    ).add_to(m)

# HTML file save karein
m.save('aqi_map.html')
print("Mubarak ho! 'aqi_map.html' naye live data ke sath successfully ban gaya hai.")