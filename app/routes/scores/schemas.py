from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class HTTPError(BaseModel):
    detail: str

    class Config:
        json_schema_extra = {
            "example": {"detail": "HTTPException raised."}
        }

class SingleScoreSchema(BaseModel):
    id: int
    user_id: int
    game_id: int
    amount_won: int | None
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)

class AddScoreByNameRequestSchema(BaseModel):
    user_id: int
    game_name: str = Field(..., min_length=1)
    amount_won: int | None = None