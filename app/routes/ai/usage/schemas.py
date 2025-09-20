from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class HTTPError(BaseModel):
    detail: str

    class Config:
        json_schema_extra = {
            "example": {"detail": "HTTPException raised."}
        }

class UsageSchema(BaseModel):
    id: int
    user_id: int
    type: str
    tokens: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)
    

class AddUsageRequestSchema(BaseModel):
    uid:int
    type: str = Field(..., pattern="^(text|image)$", description="Type must be either 'text' or 'image'")
    tokens: int = Field(..., gt=0)