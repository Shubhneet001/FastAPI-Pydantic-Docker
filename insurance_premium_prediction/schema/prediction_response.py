from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_cattegory: str = Field(
        ...,
        description="The predicted insurance premium category",
        example="high"
    )
    confidence: float = Field(
        ...,
        description="Model's confidence score for the predicted class (range: 0 to 1)",
        example=0.8432
    )
    class_probabilities: Dict[str, float] = Field(
        ...,
        description="probability distribution across all possible classes",
        example={"low":0.01, "medium":0.15, "high":0.84}
    )