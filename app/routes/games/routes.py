from fastapi import APIRouter, Depends

from .schemas import HTTPError, SingleGameSchema, AddGameRequestSchema
from .functions import AddGame

router = APIRouter(prefix='/games')

@router.post('/add_game', status_code=201, response_model=SingleGameSchema, responses={404: {'model':HTTPError}})
async def add_game(data: AddGameRequestSchema, function: AddGame = Depends(AddGame)) -> SingleGameSchema:
    new_game = await function.execute(data.game_name)

    return new_game