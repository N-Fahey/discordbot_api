from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class HTTPError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "HTTPException raised."}
        }

class SingleUser(BaseModel):
    id: int
    uid: int
    username: str
    display_name: str
    bank: int
    last_dole: datetime | None

    model_config = ConfigDict(from_attributes=True)

class CreateUserRequest(BaseModel):
    uid: int
    username: str = Field(..., min_length=2, max_length=32)
    display_name: str = Field(..., min_length=2, max_length=32)