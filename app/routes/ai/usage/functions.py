from fastapi import HTTPException

from app.database import DBSessionDep
from app.model import User, AIUsage
from .schemas import UsageSchema

class AddUsage:
    def __init__(self, session: DBSessionDep):
        self.session = session
    
    async def execute(self, uid:int, type:str, tokens:int):
        
        async with self.session.begin() as session:
            usage_user = await User.get_user_by_uid(session, uid)
            if usage_user is None:
                raise HTTPException(status_code=404, detail="User not found.")
            
            usage = await AIUsage.add_usage(session, usage_user.id, type, tokens)
            
            return UsageSchema.model_validate(usage)