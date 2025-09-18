from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/users')

@router.get('')
def users_test() -> JSONResponse:
    return JSONResponse({'message': 'Users, get'}), 200