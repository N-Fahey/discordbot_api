from fastapi import APIRouter, Depends

from .schemas import HTTPError, SingleMessageSchema, ConversationSchema, AddMessageRequestSchema
from .functions import AddMessage, GetConversation

router = APIRouter(prefix='/messages')

@router.get('/get_conversation', response_model=ConversationSchema, responses={404: {'model':HTTPError}})
async def get_conversation(message_id:int, function: GetConversation = Depends(GetConversation)) -> ConversationSchema:
    #TODO: Get conversation from message ID
    pass

@router.post('/add_message', response_model=SingleMessageSchema, responses={404: {'model':HTTPError}})
async def add_message(data: AddMessageRequestSchema, function: AddMessage = Depends(AddMessage)) -> SingleMessageSchema:
    new_message = await function.execute(data.uid, data.conversation_id, data.message_id, data.text)

    return new_message