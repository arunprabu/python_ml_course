from fastapi import APIRouter

from app.schemas.prediction_request import PredictionRequest
from app.services.prediction_service import predict

router = APIRouter(prefix="/api/v1/predict")


@router.post("/")
def run_prediction(input: PredictionRequest):
    print("Running Predictions")
    print(input)
    return predict(input.model_dump())
