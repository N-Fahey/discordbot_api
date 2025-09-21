from fastapi import HTTPException

from app.db import DBSessionDep
from app.model import User, AIMessage
from .schemas import SingleMessageSchema, ConversationSchema

class GetConversation:
    def __init__(self, session: DBSessionDep):
        self.session = session
    
    async def execute(self, message_id:int):
        
        async with self.session.begin() as session:
            base_message = await AIMessage.get_message(session, message_id)

            if base_message is None:
                raise HTTPException(status_code=404, detail="Message not found.")

            conversation = [message async for message in AIMessage.get_conversation(session, base_message)]

            return_dict = {
                'conversation': conversation
                }
            
            return ConversationSchema.model_validate(return_dict)

class AddMessage:
    def __init__(self, session: DBSessionDep):
        self.session = session
    
    async def execute(self, uid:int | None, conversation_id:int, message_id:int, text:str):
        
        async with self.session.begin() as session:
            if uid is None:
                user_id = None
            else:
                user = await User.get_user_by_uid(session, uid)
                if user is None:
                    raise HTTPException(status_code=404, detail="User not found.")
                user_id = user.id

            new_message = await AIMessage.add_message(session, user_id, conversation_id, message_id, text)

            return SingleMessageSchema.model_validate(new_message)
