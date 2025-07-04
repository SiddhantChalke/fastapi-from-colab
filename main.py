from fastapi import FastAPI
from pydantic import BaseModel

# Dummy "ML" function (replace with your actual model later)
def predict_ml(text: str) -> str:
    # Example: Silly sentiment analysis
    if "happy" in text.lower():
        return "Positive 😊"
    elif "sad" in text.lower():
        return "Negative 😢"
    else:
        return "Neutral 😐"

# FastAPI setup
app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(input: InputText):
    prediction = predict_ml(input.text)
    return {"prediction": prediction}
