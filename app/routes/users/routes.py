from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from .functions import CreateUser, GetUserByUID
from .schemas import HTTPError, SingleUserSchema, CreateUserRequestSchema

router = APIRouter(prefix='/users')

@router.post('', status_code=201, response_model=SingleUserSchema)
async def create_new_user(data:CreateUserRequestSchema, function:CreateUser = Depends(CreateUser)) -> SingleUserSchema:
    new_user = await function.execute(data.uid, data.username, data.display_name)
    return new_user

@router.get('/{user_id}', response_model=SingleUserSchema, responses={404: {'model':HTTPError}})
async def get_user_by_uid(user_id, function: GetUserByUID = Depends(GetUserByUID)) -> SingleUserSchema:
    '''Get a single user by Discord unique ID'''
    user = await function.execute(user_id)
    return user
