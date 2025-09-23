from fastapi import APIRouter, Depends

from .functions import CreateUser, GetUserByUID, GetAllUsers
from .schemas import HTTPError, SingleUserSchema, ManyUserSchema, CreateUserRequestSchema

router = APIRouter(prefix='/users')

@router.get('/get_user', response_model=SingleUserSchema, responses={404: {'model':HTTPError}})
async def get_user_by_uid(user_id:int, function: GetUserByUID = Depends(GetUserByUID)) -> SingleUserSchema:
    '''Get a single user by Discord unique ID'''
    user = await function.execute(user_id)
    return user

@router.get('/get_users')
async def get_all_users(function: GetAllUsers = Depends(GetAllUsers)) -> ManyUserSchema:
    '''Get all users'''
    users = await function.execute()
    return users

@router.post('/create_user', status_code=201, response_model=SingleUserSchema)
async def create_new_user(data:CreateUserRequestSchema, function:CreateUser = Depends(CreateUser)) -> SingleUserSchema:
    '''Create new user'''
    new_user = await function.execute(data.uid, data.username, data.display_name)
    return new_user
