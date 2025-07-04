from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware 

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

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (replace "*" with your frontend URL in production)
    allow_credentials=True,
    allow_methods=["POST"],  # Allow only POST requests
    allow_headers=["*"],
)

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(input: InputText):
    prediction = predict_ml(input.text)
    return {"prediction": prediction}
