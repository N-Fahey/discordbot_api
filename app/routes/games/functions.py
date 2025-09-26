from fastapi import HTTPException

from app.db import DBSessionDep
from app.model import Game
from .schemas import SingleGameSchema, ManyGamesSchema

class AddGame:
    def __init__(self, session: DBSessionDep):
        self.session = session
    
    async def execute(self, game_name:str):
        
        async with self.session.begin() as session:
            existing_game = await Game.get_game_by_name(session, game_name)

            if existing_game:
                raise HTTPException(status_code=409, detail=f"Game with name {game_name} already exists.")

            new_game = await Game.add_game(session, game_name)

            return SingleGameSchema.model_validate(new_game)

class GetAllGames:
    def __init__(self, session: DBSessionDep):
        self.session = session

    async def execute(self):
        
        async with self.session.begin() as session:
            games = [game async for game in Game.get_all_games(session)]

            if not games:
                raise HTTPException(status_code=404, detail=f"No games found.")
            
            return_dict = {
                'games': games
            }
            
            return ManyGamesSchema.model_validate(return_dict)