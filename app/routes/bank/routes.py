from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/bank')

@router.get('')
def bank_test() -> JSONResponse:
    return JSONResponse({'message': 'Bank, get'}), 200