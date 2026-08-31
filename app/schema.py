from typing import Optional
from pydantic import BaseModel, Field


class StudentHealthInput(BaseModel):
    sleep_duration: Optional[float] = None
    heart_rate: Optional[float] = None
    bmi: Optional[float] = None
    calorie_expenditure: Optional[float] = None
    step_count: Optional[float] = None
    exercise_duration: Optional[float] = None
    water_intake: Optional[float] = None

    diet_type: Optional[str] = None
    stress_level: Optional[str] = None
    sleep_quality: Optional[str] = None
    physical_activity_level: Optional[str] = None
    smoking_alcohol: Optional[str] = None
    gender: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "sleep_duration": 6.5,
                "heart_rate": 78.0,
                "bmi": 23.4,
                "calorie_expenditure": 2100.0,
                "step_count": 8500.0,
                "exercise_duration": 30.0,
                "water_intake": 2.1,
                "diet_type": "balanced",
                "stress_level": "medium",
                "sleep_quality": "average",
                "physical_activity_level": "moderate",
                "smoking_alcohol": "no",
                "gender": "male",
            }
        }

class PredictionOutput(BaseModel):
    health_condition: str
    probabilities: dict[str, float]