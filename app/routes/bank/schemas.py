from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class HTTPError(BaseModel):
    detail: str

    class Config:
        json_schema_extra = {
            "example": {"detail": "HTTPException raised."}
        }

class SingleBalanceSchema(BaseModel):
    uid: int
    balance: int

    model_config = ConfigDict(from_attributes=True)

class ManyBalanceSchema(BaseModel):
    balances: list[SingleBalanceSchema]

    model_config = ConfigDict(from_attributes=True)

class TransferBalancesSchema(BaseModel):
    from_uid: int
    from_balance: int
    to_uid: int
    to_balance: int

    model_config = ConfigDict(from_attributes=True)

class SingleDoleSchema(BaseModel):
    uid: int
    last_dole: datetime | None

    model_config = ConfigDict(from_attributes=True)

class SingleBalanceRequestSchema(BaseModel):
    uid:int
    amount:int = Field(..., ge=1)

class TransferAmountRequestSchema(BaseModel):
    from_uid: int
    to_uid: int
    amount: int = Field(..., ge=1)

    model_config = ConfigDict(from_attributes=True)