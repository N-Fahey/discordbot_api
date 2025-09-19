from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from .schemas import HTTPError, SingleMessageSchema, AddMessageRequestSchema
from .functions import AddMessage

router = APIRouter(prefix='/messages')

@router.get('')
async def messages_test() -> JSONResponse:
    return JSONResponse({'message': "Messages, get"}), 200

@router.post('/add_message', response_model=SingleMessageSchema, responses={404: {'model':HTTPError}})
async def add_message(data: AddMessageRequestSchema, function: AddMessage = Depends(AddMessage)) -> SingleMessageSchema:
    new_message = await function.execute(data.uid, data.conversation_id, data.message_id, data.text)

    return new_message

#TODO: Read conversation from message ID