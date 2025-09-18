from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/scores')

@router.get('')
def scores_test() -> JSONResponse:
    return JSONResponse({'message': 'Scores, get'}), 200