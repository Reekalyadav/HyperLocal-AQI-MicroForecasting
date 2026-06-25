import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

print("Naya dataset load ho raha hai...")
# Naya data load karein jo generate_data.py se bana h
df = pd.read_csv('ghaziabad_aqi_data.csv')

# Naye features ke naamon ke hisab se select karein
X = df[['PM2.5', 'NO2', 'Traffic_Index', 'Distance_to_Highway', 'Distance_to_Park']]
y = df['AQI']

# Data ko train aur test mein baantein
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Random Forest Model naye features ke sath train ho raha hai...")
# Model initialize aur train karein
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model ki accuracy check karein
accuracy = model.score(X_test, y_test)
print(f"Model Training Complete! Test Accuracy: {accuracy*100:.2f}%")

# Purani .pkl file ko naye trained brain se replace karein
joblib.dump(model, 'aqi_model.pkl')
print("Naya model 'aqi_model.pkl' successfully save ho gaya hai!")