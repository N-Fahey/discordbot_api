from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class HTTPError(BaseModel):
    detail: str

    class Config:
        json_schema_extra = {
            "example": {"detail": "HTTPException raised."}
        }

class SingleGameSchema(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

class ManyGamesSchema(BaseModel):
    games: list[SingleGameSchema]

    model_config = ConfigDict(from_attributes=True)

class AddGameRequestSchema(BaseModel):
    game_name: str = Field(..., min_length=1)