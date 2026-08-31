from fastapi import FastAPI
from app.schema import StudentHealthInput, PredictionOutput
from app.model import predict

app = FastAPI(title="Student Health Risk Predictor")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionOutput)
def make_prediction(data: StudentHealthInput):
    result = predict(data.model_dump())
    return result
