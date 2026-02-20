from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
import os

# 1. Initialize the API App
app = FastAPI(title="UK Property AI Engine", description="Real-time house price predictions")

# 2. Dynamic Pathing (The Pro Way)
# Find the exact folder this script is in, then map safely to the models folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '../models/uk_property_model.pkl')
TOWN_AVG_PATH = os.path.join(BASE_DIR, '../models/town_averages.csv')

print("Booting up AI Model...")
model = joblib.load(MODEL_PATH)
town_avg_df = pd.read_csv(TOWN_AVG_PATH)

# If a user types a brand new town we've never seen, we will fallback to the national average
national_avg = town_avg_df['town_avg_price'].mean()

# 3. Define the Input Schema (Strict rules on what data the API accepts)
class PropertyInput(BaseModel):
    year: int
    month: int
    property_type: int   # 0=Detached, 1=Semi, 2=Terraced, 3=Flat, 4=Other
    old_new: int         # 1=New build, 0=Old build
    town_city: str       # e.g., "LONDON", "MANCHESTER"

# 4. Create the Prediction Endpoint
@app.post("/predict")
def predict_price(prop: PropertyInput):
    # A. Clean the town input (make it uppercase to match our dataset)
    town_upper = prop.town_city.upper()
    
    # B. Look up the town's average historical price
    town_data = town_avg_df[town_avg_df['town_city'] == town_upper]
    
    if town_data.empty:
        town_avg_price = national_avg
    else:
        town_avg_price = town_data.iloc[0]['town_avg_price']
        
    # C. Format the features EXACTLY as our Linear Regression model expects:
    # Order: [year, month, property_type_encoded, old_new_encoded, town_avg_price]
    features = np.array([[prop.year, prop.month, prop.property_type, prop.old_new, town_avg_price]])
    
    # D. Make the prediction
    prediction = model.predict(features)[0]
    
    # E. Return the JSON response to the user
    return {
        "town_city": town_upper,
        "estimated_price": round(prediction, 2),
        "currency": "GBP"
    }