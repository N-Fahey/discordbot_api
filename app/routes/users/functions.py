from fastapi import HTTPException

from app.database import DBSessionDep
from app.model import User
from .schemas import SingleUserSchema


#Test add user
class CreateUser:
    def __init__(self, session: DBSessionDep):
        self.session = session
    
    async def execute(self, uid:int, username:str, display_name:str):

        async with self.session.begin() as session:
            #TODO: Validate user doesnt already exist with uid or username
            new_user = await User.create_user(session, uid, username, display_name)
            return SingleUserSchema.model_validate(new_user)

class GetUserByUID:
    def __init__(self, session: DBSessionDep):
        self.session = session
    
    async def execute(self, uid:int):
        
        async with self.session.begin() as session:
            user = await User.get_user_by_uid(session, uid)

            if user is None:
                raise HTTPException(status_code=404, detail="User not found.")
            return SingleUserSchema.model_validate(user)