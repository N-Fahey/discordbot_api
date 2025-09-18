from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/messages')

@router.get('')
async def messages_test() -> JSONResponse:
    return JSONResponse({'message': "Messages, get"}), 200