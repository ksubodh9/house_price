from fastapi import APIRouter
from pydantic import BaseModel
import joblib
import numpy as np
import os

router = APIRouter()

# Load your model from the utils folder
model_path = os.path.join("utils", "house_price_model.pkl")
model = joblib.load(model_path)

# Input schema for the house data
class HouseFeatures(BaseModel):
    bedrooms: int
    bathrooms: float
    sqft_living: int
    floors: float
    waterfront: int
    view: int
    condition: int
    grade: int
    sqft_above: int
    sqft_basement: int
    yr_built: int
    yr_renovated: int
    lat: float
    sqft_living15: int

@router.post("/predict")
def predict_house_price(data: HouseFeatures):
    features = np.array([[
        data.bedrooms, data.bathrooms, data.sqft_living, data.floors,
        data.waterfront, data.view, data.condition, data.grade,
        data.sqft_above, data.sqft_basement, data.yr_built,
        data.yr_renovated, data.lat, data.sqft_living15
    ]])

    prediction = model.predict(features)
    return {"predicted_price": round(prediction[0], 2)}
