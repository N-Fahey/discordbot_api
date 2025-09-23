from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from .schemas import HTTPError, UsageSchema, AddUsageRequestSchema
from .functions import AddUsage

router = APIRouter(prefix='/usage')

@router.post('/add_usage', status_code=201, response_model=UsageSchema, responses={404: {'model':HTTPError}})
async def add_usage(data: AddUsageRequestSchema, function: AddUsage = Depends(AddUsage)) -> UsageSchema:
    new_usage = await function.execute(data.uid, data.type, data.tokens)

    return new_usage