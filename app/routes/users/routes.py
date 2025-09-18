from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from .functions import CreateUser, GetUserByUID
from .schemas import HTTPError, SingleUser, CreateUserRequest

router = APIRouter(prefix='/users')

@router.get('')
def users_test() -> JSONResponse:
    return JSONResponse({'message': 'Users, get'})

@router.post('', status_code=201, response_model=SingleUser)
async def create_new_user(data:CreateUserRequest, function:CreateUser = Depends(CreateUser)) -> SingleUser:
    new_user = await function.execute(data.uid, data.username, data.display_name)
    return new_user

@router.get('/{user_id}', response_model=SingleUser, responses={404: {'model':HTTPError}})
async def get_user_by_uid(user_id, function: GetUserByUID = Depends(GetUserByUID)) -> SingleUser:
    '''Get a single user by Discord unique ID'''
    user = await function.execute(user_id)
    if user is None:
        #TODO: Implement return to bypass response model?
        pass
    return user