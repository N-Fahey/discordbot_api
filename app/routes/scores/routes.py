from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from .schemas import HTTPError, SingleScoreSchema, AddScoreByNameRequestSchema
from .functions import AddScoreByGameName

router = APIRouter(prefix='/scores')

@router.get('')
def scores_test() -> JSONResponse:
    return JSONResponse({'message': 'Scores, get'}), 200

@router.post('/add_score', response_model=SingleScoreSchema, responses={404: {'model':HTTPError}})
async def add_score(data: AddScoreByNameRequestSchema, function: AddScoreByGameName = Depends(AddScoreByGameName)) -> SingleScoreSchema:
    new_score = await function.execute(data.user_id, data.game_name, data.amount_won)

    return SingleScoreSchema.model_validate(new_score)