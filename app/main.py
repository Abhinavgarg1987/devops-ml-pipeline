from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict_seniority

app = FastAPI(title="DevOps ML API")

class InputData(BaseModel):
    years_experience: float
    skill_score: float

@app.get("/")
def home():
    return {"status": "healthy", "message": "ML Model DevOps Pipeline API is Live!"}

@app.post("/predict")
def predict(data: InputData):
    result = predict_seniority(data.years_experience, data.skill_score)
    return {
        "years_experience": data.years_experience,
        "skill_score": data.skill_score,
        "prediction": result
    }