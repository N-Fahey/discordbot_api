from fastapi import APIRouter, Depends

from .schemas import HTTPError, SingleGameSchema, ManyGamesSchema, AddGameRequestSchema
from .functions import AddGame, GetAllGames

router = APIRouter(prefix='/games')

@router.get('/get_games', response_model=ManyGamesSchema, responses={404: {'model':HTTPError}})
async def get_games(function: GetAllGames = Depends(GetAllGames)) -> ManyGamesSchema:
    games = await function.execute()

    return games

@router.post('/add_game', status_code=201, response_model=SingleGameSchema, responses={404: {'model':HTTPError}})
async def add_game(data: AddGameRequestSchema, function: AddGame = Depends(AddGame)) -> SingleGameSchema:
    new_game = await function.execute(data.game_name)

    return new_game
