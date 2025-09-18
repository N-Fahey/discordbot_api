from datetime import datetime
from pydantic import BaseModel, ConfigDict

class SingleBank(BaseModel):
    id: int
    uid: int
    username: str
    display_name: str
    bank: int
    last_dole: datetime | None

    model_config = ConfigDict(from_attributes=True)