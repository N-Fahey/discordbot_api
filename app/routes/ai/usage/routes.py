from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/usage')

@router.get('')
async def usage_test() -> JSONResponse:
    return JSONResponse({'message': "Usage, get"}), 200

#TODO: Add usage