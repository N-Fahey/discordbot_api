from fastapi import HTTPException

from app.database import DBSessionDep
from app.model import Score, User
from .schemas import SingleScoreSchema

class AddScoreByGameName:
    def __init__(self, session: DBSessionDep):
        self.session = session
    
    async def execute(self, uid:int, game_name:str, amount_won:int | None = None):
        
        async with self.session.begin() as session:
            user = await User.get_user_by_uid(session, uid)
            if user is None:
                raise HTTPException(status_code=404, detail="User not found.")

            try:
                new_score = await Score.add_score_by_game_name(session, user.id, game_name, amount_won)
            except ValueError:
                raise HTTPException(status_code=404, detail=f"Game with name {game_name} not found.")

            return SingleScoreSchema.model_validate(new_score)
