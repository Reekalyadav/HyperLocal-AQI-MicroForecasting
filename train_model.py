import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib # Model ko save karne ke liye

def train_aqi_model():
    # 1. Data Load Karo
    df = pd.read_csv("ghaziabad_final_features.csv")
    
    # 2. Features (X) aur Target (y) select karo
    # Hum latitude/longitude ko bhi features mein rakhenge taaki model area ko samjhe
    X = df[['latitude', 'longitude', 'satellite_no2', 'traffic_index', 'dist_to_highway_km', 'has_park_500m']]
    y = df['pm25']
    
    # 3. Data ko Train aur Test mein baanto (80% seekhne ke liye, 20% test karne ke liye)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Model training shuru ho rahi hai...")
    
    # 4. Random Forest Model banana
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 5. Model ko Check karna (Testing)
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    print(f"Model Training Complete!")
    print(f"Average Error (MAE): {mae:.2f} units") # Jitna kam, utna acha
    print(f"Accuracy Score (R2): {r2:.2f}") # 1.0 ke jitna paas, utna acha
    
    # 6. Model ko save karna taaki baad me use kar sakein
    joblib.dump(model, "aqi_model.pkl")
    print("Model 'aqi_model.pkl' ke naam se save ho gaya hai.")

if __name__ == "__main__":
    train_aqi_model()