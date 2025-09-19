from pydantic import BaseModel, ConfigDict, Field

class HTTPError(BaseModel):
    detail: str

    class Config:
        json_schema_extra = {
            "example": {"detail": "HTTPException raised."}
        }

class SingleMessageSchema(BaseModel):
    id: int
    user_id: int | None
    conversation_id: int
    message_id: int
    text: str

    model_config = ConfigDict(from_attributes=True)

class ConversationSchema(BaseModel):
    conversation: list[SingleMessageSchema]

    model_config = ConfigDict(from_attributes=True)

class AddMessageRequestSchema(BaseModel):
    uid:int | None
    conversation_id:int
    message_id:int
    text:str = Field(..., min_length=1, max_length=2000)